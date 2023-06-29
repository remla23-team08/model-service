import pickle as pkl
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from libpython import preprocessing


def model_predict(review):
    """
    Preprocess the input and make a prediction
    """
    # Load BoW dictionary and classifier
    model = pkl.load(open("ml-model/c1_BoW_Sentiment_Model.pkl", "rb"))
    classifier = joblib.load("ml-model/c2_Classifier_Sentiment_Model")

    # Process input
    preprocess_class = preprocessing.Preprocessing()
    processed = preprocess_class.preprocess_review(review)
    processed = model.transform([processed]).toarray()[0]

    # Make a prediction
    prediction = classifier.predict([processed])[0]

    return prediction
