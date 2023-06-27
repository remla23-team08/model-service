import os
import gdown

# Define the URLs to download the model files
bow_model_url = "https://drive.google.com/uc?id=15QjYa8HG2cxR-YD-t1dyGH7k5I4EkYl8"
classifier_model_url = (
    "https://drive.google.com/uc?id=1MWO4pqacsHu803RqufcELq0xkKGEfJOr"
)


# Specify the paths to save the downloaded models
model_dir = "ml-model/"
bow_model_name = "c1_BoW_Sentiment_Model.pkl"
classifier_model_name = "c2_Classifier_Sentiment_Model"


def download_model_files():
    """
    Download the sentiment model files on start if they don't exist.
    """
    os.makedirs(model_dir, exist_ok=True)
    bow_model_path = os.path.join(model_dir, bow_model_name)
    classifier_model_path = os.path.join(model_dir, classifier_model_name)

    gdown.download(bow_model_url, bow_model_path, quiet=False)
    gdown.download(classifier_model_url, classifier_model_path, quiet=False)
