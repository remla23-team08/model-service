FROM python:3.7-slim

# Set working directory to root
WORKDIR /root

# Install additional helper packages
RUN apt-get update && apt-get install -y \
  openssl \
  vim \
  wget \
  curl \
  lsof \
  iputils-ping

LABEL authors="Team 08 REMLA" \
  description="Model Service API for Sentiment Analysis"

# Copy the necessary files
COPY requirements.txt /root/
COPY app.py /root/
COPY model.py /root/
COPY metrics.py /root/
COPY utils.py /root/

# Install the required packages
RUN pip install -r requirements.txt

# Expose the port and run the app
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
