FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apk add --no-cache mpd libc6-compat

COPY requirements.txt requirements.txt
COPY mpdconfig.conf mpdconfig.conf
COPY web-radio web-radio

RUN pip install -r requirements.txt

RUN mpd mpdconfig.conf

WORKDIR web-radio

CMD python3 radio_server.py
