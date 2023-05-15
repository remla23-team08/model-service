# MODEL-SERVICE

Contains the wrapper service for the ML model.

## Fetch trained model

To run the service with the latest model, download the latest trained model from the remla23-team08/model-training repository under the res folder.


## How To Run

Clone the repository on your machine by executing the following command

	git clone https://github.com/remla23-team08/model-service.git

While in the root folder install the required packages executing the following command

	pip install -r requirements.txt

Run the application from the root folder by executing the following command

	python app.py

A Flask server will be made available at <http://localhost:8080> where the API documentation is available at <http://localhost:8080/apidocs>.
Application metrics can be accessed at <http://localhost:8080/metrics>.
<!-- 
## Run through Docker

Build and run the Docker image by executing the following commands where ```VERSION``` is the desired release tag

	docker build -t ghcr.io/remla23-team08/model-service:VERSION -->

	

