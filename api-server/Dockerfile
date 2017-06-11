FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt
COPY api-server api-server

RUN apk add --no-cache libc6-compat gcc postgresql-dev python3-dev

RUN pip install -r requirements.txt

WORKDIR api-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 api:app