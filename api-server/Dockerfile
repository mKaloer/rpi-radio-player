FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt
COPY api-server api-server

RUN apk --update add py-gunicorn

RUN pip install -r requirements.txt
RUN cp /usr/glibc-compat/lib/ld-linux-armhf.so.3 /lib

WORKDIR api-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 api:app