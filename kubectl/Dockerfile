FROM python:3.8-alpine
MAINTAINER Lingxian Kong <anlin.kong@gmail.com>

RUN apk --no-cache add curl httpie jq && pip install pyyaml && \
    curl -L# https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl
