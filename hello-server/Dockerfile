FROM python:2.7-alpine
MAINTAINER Lingxian Kong <anlin.kong@gmail.com>

RUN apk --no-cache add curl
ADD webserver.py /webserver.py

EXPOSE 8080
CMD python /webserver.py
