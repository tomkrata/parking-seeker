# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7

WORKDIR /src

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True


# Install production dependencies.
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . ./
CMD [ "python3", "main.py"]