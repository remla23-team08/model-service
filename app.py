import flask
from flask import Flask, request, Response
from model import model_predict
from flask_cors import CORS
from flasgger import Swagger
from prometheus_client import generate_latest
from metrics import *
import time

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)


@app.before_request
def logging_before():
    # Store the start time for the request
    flask.start_time = time.perf_counter()


@app.after_request
def logging_after(response):
    # Get total response time in seconds
    rsp_time = time.perf_counter() - flask.start_time
    response_time_histogram.labels(api=request.path).observe(rsp_time)
    return response


@app.route('/predict', methods=['POST'])
def predict():
    """
    Make a hardcoded prediction
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: review to be classified.
          required: True
          schema:
            type: object
            required: review
            properties:
                review:
                    type: string
                    example: This is a bad/good review
    responses:
      200:
        description: Some result
    """

    # Retrieve review from the request
    review = request.get_json().get('review')

    # Make a prediction on the message
    prediction = int(model_predict(review))

    # Update counter based on prediction
    predictions_counter.labels(api='predict').inc()
    if prediction == 0:
        neg_predictions_counter.labels(api='predict').inc()
    else:
        pos_predictions_counter.labels(api='predict').inc()

    response = flask.jsonify({
        "review": review,
        "prediction": prediction,
        "time": 0
    })

    return response


@app.route('/model-feedback', methods=['POST'])
def model_feedback():
    # Retrieve feedback from the request
    satisfied = bool(request.get_json().get('satisfied'))
    prediction = int(request.get_json().get('prediction'))

    # Depending on whether user is satisfied with model response, update true/false prediction counter
    if satisfied:
        if prediction == 0:
            true_neg_predictions_counter.labels(api='model-feedback').inc()
        else:
            true_pos_predictions_counter.labels(api='model-feedback').inc()
    else:
        if prediction == 0:
            false_neg_predictions_counter.labels(api='model-feedback').inc()
        else:
            false_pos_predictions_counter.labels(api='model-feedback').inc()

    # calculate current model accuracy based on true/false predictions
    true_neg_predictions = true_neg_predictions_counter.labels(api='model-feedback')._value.get()
    true_pos_predictions = true_pos_predictions_counter.labels(api='model-feedback')._value.get()
    false_neg_predictions = false_neg_predictions_counter.labels(api='model-feedback')._value.get()
    false_pos_predictions = false_pos_predictions_counter.labels(api='model-feedback')._value.get()

    total_feedback = true_neg_predictions + true_pos_predictions + false_neg_predictions + false_pos_predictions
    accuracy = (true_neg_predictions + true_pos_predictions) / total_feedback
    model_accuracy_gauge.labels(api='model-feedback').set(accuracy)

    # return model accuracy
    response = flask.jsonify({
        "model-accuracy": accuracy
    })

    return response


@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
