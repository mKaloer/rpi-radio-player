FROM python:3

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apt-get update -y

COPY requirements.txt requirements.txt
COPY api-server api-server

RUN pip install -r requirements.txt

WORKDIR api-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 api:app