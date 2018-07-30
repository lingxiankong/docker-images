FROM python:2.7-alpine
MAINTAINER Lingxian Kong <anlin.kong@gmail.com>

RUN apk --no-cache add --update build-base gcc musl-dev libffi-dev openssl-dev
RUN pip install cryptography

ADD main.py /main.py

ENTRYPOINT ["/usr/local/bin/python","/main.py"]
CMD ["Hello, Qinling"]
