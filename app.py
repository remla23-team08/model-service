from flask import Flask, request
from model import model_predict
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.post('/Predict', )
def predict():
	"""
	Make a hardcoded prediction
	---
	consumes:
		- application/json
	parameters:
		- name: input_data
		in: body
		description: input to get predicted.
		required: True
		schema:
			type: object
			properties:
				input: TBD
				example: TBD
	responses:
		200:
			description: prediction
	"""

	input = request.get_json().get('input')
	return model_predict(input)