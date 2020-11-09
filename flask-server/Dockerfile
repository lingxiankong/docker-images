FROM python:3.7-alpine
MAINTAINER Lingxian Kong <anlin.kong@gmail.com>

RUN pip install --no-cache-dir Flask
ADD webserver.py /webserver.py
ENV FLASK_APP /webserver.py

EXPOSE 8080
CMD flask run --host=0.0.0.0 --port 8080
