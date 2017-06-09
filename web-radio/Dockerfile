FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

RUN apk add --no-cache mpd

RUN apk add --no-cache ca-certificates openssl wget
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-2.25-r0.apk
RUN apk add glibc-2.25-r0.apk

COPY requirements.txt requirements.txt
COPY mpdconfig.conf mpdconfig.conf
COPY web-radio web-radio

RUN pip install -r requirements.txt

RUN mpd mpdconfig.conf

WORKDIR web-radio

CMD python3 radio_server.py
