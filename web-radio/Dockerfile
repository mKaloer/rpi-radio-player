FROM python:3

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apt-get update -y
RUN apt-get install -y --fix-missing mpd

COPY requirements.txt requirements.txt
COPY mpdconfig.conf mpdconfig.conf
COPY web-radio web-radio

RUN pip install -r requirements.txt

RUN mpd mpdconfig.conf

WORKDIR web-radio

CMD python radio_server.py
