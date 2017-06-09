FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apk add --no-cache mpd libc6-compat supervisord
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY mpdconfig.conf mpdconfig.conf

COPY requirements.txt requirements.txt
COPY web-radio web-radio

RUN pip install -r requirements.txt

CMD ["/usr/bin/supervisord"]
