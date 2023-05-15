import pickle as pkl
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def model_predict(review):
    """
    Preprocess the input and make a prediction
    """
    # Load BoW dictionary and classifier
    model = pkl.load(open("ml-model/c1_BoW_Sentiment_Model.pkl", "rb"))
    classifier = joblib.load("ml-model/c2_Classifier_Sentiment_Model")

    # Process input
    processed = process(review)
    processed = model.transform([processed]).toarray()[0]

    # Make a prediction
    prediction = classifier.predict([processed])[0]

    return prediction


def process(review):
    """
    Preprocess the given input
    """

    nltk.download("stopwords")
    ps = PorterStemmer()

    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")

    review = re.sub("[^a-zA-Z]", " ", review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
    review = " ".join(review)

    return review
