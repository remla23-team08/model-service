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
	prediction = model_predict(review)

	return {
		"review": review,
		"prediction": int(prediction),
	}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
