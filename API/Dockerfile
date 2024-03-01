FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install nginx python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

RUN pip3 install -U pip setuptools wheel
RUN pip3 install flask

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx.crt /etc/ssl/certs/nginx.crt
COPY ./nginx.key /etc/ssl/private/nginx.key

COPY ./entrypoint.sh /entrypoint.sh
WORKDIR /code

RUN chmod ug+x /entrypoint.sh

CMD /entrypoint.sh