FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apk add --no-cache mpd libc6-compat supervisor

COPY supervisord.conf supervisord.conf
COPY mpdconfig.conf mpdconfig.conf

COPY requirements.txt requirements.txt
COPY web-radio web-radio

RUN pip install -r requirements.txt

CMD supervisord -c supervisord.conf
