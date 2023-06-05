import flask
from flask import Flask, request, Response
from model import model_predict
from flask_cors import CORS
from flasgger import Swagger
from prometheus_client import generate_latest
import metrics
import time

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)


@app.before_request
def logging_before():
    metrics.http_requests_counter.labels(api=request.path).inc()
    # Store the start time for the request
    flask.start_time = time.perf_counter()


@app.after_request
def logging_after(response):
    # Get total response time in seconds
    rsp_time = time.perf_counter() - flask.start_time
    metrics.response_time_histogram.labels(api=request.path).observe(rsp_time)
    return response


@app.route("/predict", methods=["POST"])
def predict():
    """
    Make a prediction using the sentiment analysis model.
    Given user review predict the sentiment of that review.
    Predictions can be 0 (negative sentiment) or 1 (positive sentiment).
    Updates metrics about the number of predictions that have been served.
    This includes the total number of predictions, the number of positive predictions,
    and the number of negative predictions.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: review to be classified
          required: True
          schema:
            type: object
            required: review
            properties:
                review:
                    type: string
                    example: This is a bad/good review.
                restaurantName:
                    type: string
                    example: name
        - name: output_data
          in: body
          description: sentiment prediction of the received review
          required: True
          schema:
            type: object
            required: true
            properties:
                review:
                    type: string
                    example: This is a bad/good review.
                prediction:
                    type: integer
                    example: 0
                restaurantName:
                    type: string
                    example: name
    responses:
      200:
        description: Successful response
    """

    # Retrieve review from the request
    review = request.get_json().get("review")
    restaurant_name = request.get_json().get("restaurantName")

    # Make a prediction on the message
    prediction = int(model_predict(review))

    # Update counter based on prediction
    metrics.predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()
    if prediction == 0:
        metrics.neg_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()
    else:
        metrics.pos_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()

    response = flask.jsonify({"review": review, "prediction": prediction, "restaurantName": restaurant_name})

    return response


@app.route("/model-accuracy", methods=["POST"])
def model_feedback():
    """
    Receive feedback that indicates whether the sentiment of the response was correct given the review.
    User rates prediction as either accurate or not accurate.
    Based on the user's feedback update true/false prediction counters.
    Gauge model accuracy is updated based on total number of true/false predictions.
    Returns current model accuracy.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: feedback from the user about the accuracy of the sentiment prediction
          required: True
          schema:
            type: object
            required: true
            properties:
                accurate:
                    type: boolean
                    example: false
                prediction:
                    type: int
                    example: 1
                restaurantName:
                    type: string
                    example: name
        - name: output_data
          in: body
          description: accuracy calculated based on total number of true/false predictions
          required: True
          schema:
            type: object
            required: true
            properties:
                model-accuracy:
                    type: float
                    example: 0.9
                restaurantName:
                    type: string
                    example: name
    responses:
      200:
        description: Successful response
    """

    # Retrieve feedback from the request
    accurate = bool(request.get_json().get("accurate"))
    prediction = int(request.get_json().get("prediction"))
    restaurant_name = request.get_json().get("restaurantName")


    # Depending on whether user thinks model response is accurate, update true/false prediction counter
    if accurate:
        if prediction == 0:
            metrics.true_neg_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()
        else:
            metrics.true_pos_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()
    else:
        if prediction == 0:
            metrics.false_neg_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()
        else:
            metrics.false_pos_predictions_counter.labels(api=request.path, restaurant_name=restaurant_name).inc()

    # calculate current model accuracy based on true/false predictions
    true_neg_predictions = metrics.true_neg_predictions_counter.labels(
        api=request.path, restaurant_name=restaurant_name
    )._value.get()
    true_pos_predictions = metrics.true_pos_predictions_counter.labels(
        api=request.path, restaurant_name=restaurant_name
    )._value.get()
    false_neg_predictions = metrics.false_neg_predictions_counter.labels(
        api=request.path, restaurant_name=restaurant_name
    )._value.get()
    false_pos_predictions = metrics.false_pos_predictions_counter.labels(
        api=request.path, restaurant_name=restaurant_name
    )._value.get()

    total_feedback = (
        true_neg_predictions
        + true_pos_predictions
        + false_neg_predictions
        + false_pos_predictions
    )
    accuracy = (true_neg_predictions + true_pos_predictions) / total_feedback
    metrics.model_accuracy_gauge.labels(api=request.path, restaurant_name=restaurant_name).set(accuracy)

    # return model accuracy
    response = flask.jsonify({"model-accuracy": accuracy, "restaurantName": restaurant_name})

    return response


@app.route("/metrics", methods=["GET"])
def generate_metrics():
    """
    Get all metrics defined using the prometheus client library.
    ---
    parameters:
        - name: output_data
          in: body
          description: prometheus metrics observed from monitoring requests
          required: True
    responses:
      200:
        description: Successful response
    """

    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
