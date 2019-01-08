FROM python:3.6-slim

# Add our code
ADD ./ /opt/
WORKDIR /opt/

# Install the dependencies
COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r requirements.txt
