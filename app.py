from flask import Flask, request
from model import model_predict
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.post('/predict', )
def predict():
	"""
	Make a hardcoded prediction
	---
	consumes:
		- application/json
	parameters:
		- name: input_data
		in: body
		description: input to be predicted.
		required: True
		schema:
			type: object
			required: review
			properties:
				review:
					type: string
					example: "this is a good/bad review"
	responses:
		200:
			description: prediction
	"""

	# Retrieve review from the request
	review = request.get_json().get('review')

	# Make a prediction on the message
	prediction = model_predict(review)

	return {
		"review": review,
		"prediction": prediction,
	}