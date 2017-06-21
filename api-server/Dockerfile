FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt
RUN apk add --no-cache libc6-compat gcc python3-dev musl-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt

COPY api-server api-server

WORKDIR api-server
ENV PYTHONPATH $PYTHONPATH:/api-server/

CMD gunicorn -c gunicorn_conf.py api:app