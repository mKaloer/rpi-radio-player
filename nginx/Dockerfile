FROM cyrhenry/rpi-alpine-nginx

COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx

CMD ["nginx", "-g", "daemon off;"]
