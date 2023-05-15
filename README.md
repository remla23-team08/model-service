# Model-Service

Contains the wrapper service for an embedded ML model used for performing sentiment analysis on reviews for restaurants.

## **Pre-requisites**

Before following the steps elicited in the upcoming sections, you need to download the latest trained model from the [remla23-team08/model-training](https://github.com/remla23-team08/model-training) repository. 

## **Usage**

1. Clone the repository on your machine by executing the following command(s):

```bash
# When using SSH keys (recommended)
git clone git@github.com:remla23-team08/model-service.git

# When using HTTPS
git clone https://github.com/remla23-team08/model-service.git
```

2. While in the root folder of this repository, install the required packages by executing the following command (not recommended):

```bash
pip install -r requirements.txt
```

> **NOTE**: It is, however, preferred to use a virtual environment to install the required packages. To do so, execute the following commands:

```bash
# Create a virtual environment
# Actual pyton binary may vary depending on your system
# We do recommend using at least Python 3.7
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

3. Run the application from the root folder by executing the following command:

```bash
python app.py
```

## **Available endpoints**

After successfully following the instructions in the previous section, the following endpoints will be available:

* The flask server will be made available at <http://localhost:8080>
* The Swagger API documentation is automatically generated and available at <http://localhost:8080/apidocs>.
* Application metrics can be accessed at <http://localhost:8080/metrics>.

## **Docker Setup**

The `model-service` application is also available as a Docker image. To manually build the docker image from your local environment, follow the steps below:

```bash
docker build -t ghcr.io/remla23-team08/model-service:VERSION .
```

> **NOTE**: Build the docker image while located in the root folder of this repository. The `VERSION` string is the desired tag and should be in the format of `x.y.z`, following the [Semantic Versioning](https://semver.org/) standard.

Once properly built, to run the docker image, execute the following command:

```bash
docker run -p 8080:8080 ghcr.io/remla23-team08/model-service:VERSION
```

> **NOTES**: 
> * The first port number in the `-p` flag is the port on your local machine, while the second port number is the port on the docker container. The two port numbers should be the same, however, if the local port is already in use, you can change it to any other port number (consider taking a look at port numbering conventions depending on your operating system).
> * You can also run the docker image in detached mode by adding the `-d` flag to the `docker run` command. This is helpful when you want to issue other commands in the same terminal window.

## **Code Style**

For coding style, we are following the [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). For automatic detection, 
we are using the [flake8](https://flake8.pycqa.org/en/latest/) tool. To install it, execute the following command:

```bash
pip install flake8
```

> **NOTE**: It is preffered to use a `venv` to install packages, as mentioned in the [Usage](#usage) section.

To run the flake8 tool on the python files using our custom configuration, execute the following command from within the root folder of this repository:

```bash
flake8 --config=config/flake8.cfg *.py
```

To automatically enforce the code style, we are using the [black](https://black.readthedocs.io/en/stable/) tool. To install it, execute the following command:

```bash
pip install black
```

Afterwards, simply run the following command from within the root folder of this repository:

```bash
black *.py
```

## **Versioning**

Versioning of this repository is done automatically using GitHub Actions. The versioning is done using the standard Semantic Versioning (SemVer) format. Version bumps are done automatically when a PR is merged to the `main` branch. To achieve this, we are using the GitVersion tool. For more information on how to use GitVersion, see [this link](https://gitversion.net/docs/).

## **Additional Information**

* [Swagger API Documentation](https://swagger.io/docs/specification/about/)
* [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
* [Docker Documentation](https://docs.docker.com/)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
