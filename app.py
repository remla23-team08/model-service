import flask
from flask import Flask, request, Response
from model import model_predict
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

countPosPredictions = 0
countNegPredictions = 0


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
	if prediction == 0:
		global countNegPredictions
		countNegPredictions += 1
	else:
		global countPosPredictions
		countPosPredictions += 1

	response = flask.jsonify({
		"review": review,
		"prediction": prediction,
	})

	return response


@app.route('/metrics', methods=['GET'])
def metrics():
	global countNegPredictions, countPosPredictions
	m = "# HELP num_predictions The number of predictions that have been served.\n"
	m += "# TYPE num_predictions counter\n"
	m += "num_predictions{{page=\"predict\"}} {}\n".format(countPosPredictions + countNegPredictions)

	m += "# HELP num_pos_predictions The number of positive predictions that have been served.\n"
	m += "# TYPE num_pos_predictions counter\n"
	m += "num_pos_predictions{{page=\"predict\"}} {}\n".format(countPosPredictions)

	m += "# HELP num_neg_predictions The number of negative predictions that have been served.\n"
	m += "# TYPE num_neg_predictions counter\n"
	m += "num_neg_predictions{{page=\"predict\"}} {}\n".format(countNegPredictions)

	return Response(m, mimetype="text/plain")


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)
