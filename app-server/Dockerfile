FROM mielune/alpine-python3-arm

MAINTAINER Mads Kalør "mads@kaloer.com"

COPY requirements.txt requirements.txt
COPY app-server app-server

# Install glibc
apk --no-cache add ca-certificates
wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-2.25-r0.apk
apk add glibc-2.25-r0.apk
RUN apk --update add py-gunicorn

RUN pip install -r requirements.txt

WORKDIR app-server

CMD gunicorn -w 4 -b 0.0.0.0:8080 app:app
