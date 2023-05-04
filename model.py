from preprocessing import process
import pickle as pkl

def model_predict(input):
	'''
	Preprocess the input and make a prediction
	'''
	# Load model
	model = pkl.load(model.pkl)

	# Process input
	processed = process(input)

	# Make a prediction
	prediction = model.predict(processed)

	return prediction

