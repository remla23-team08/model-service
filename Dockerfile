FROM python:3.7-slim

# Set working directory to root
WORKDIR /root

# Copy the necessary files
COPY requirements.txt /root/
COPY app.py /root/
COPY model.py /root/
COPY ml-model/c1_BoW_Sentiment_Model.pkl /root/ml-model/c1_BoW_Sentiment_Model.pkl
COPY ml-model/c2_Classifier_Sentiment_Model /root/ml-model/c2_Classifier_Sentiment_Model

# Install the required packages
RUN pip install -r requirements.txt

# Expose the port and run the app
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
