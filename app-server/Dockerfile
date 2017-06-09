FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt
COPY app-server app-server

RUN apk --update add py-gunicorn

RUN pip install -r requirements.txt

WORKDIR app-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 app:app
