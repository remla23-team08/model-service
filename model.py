import pickle as pkl
import joblib

def model_predict(review):
	'''
	Preprocess the input and make a prediction
	'''
	# Load BoW dictionary and classifier
	model = pkl.load("ml-model/c1_BoW_Sentiment_Model.pkl", "rb")
	classifier = joblib.load("ml_models/c2_Classifier_Sentiment_Model")

	# Process input
	processed = process(review, model)

	# Make a prediction
	prediction = classifier.predict(processed)[0]

	return prediction

def process(review, model):
	'''
	Preprocess the given input
	'''

	return model.transform([review]).toarray()[0]
