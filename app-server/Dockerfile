FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app-server app-server

WORKDIR app-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 app:app
