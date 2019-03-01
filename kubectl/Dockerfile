FROM python:2.7-alpine
MAINTAINER Lingxian Kong <anlin.kong@gmail.com>

RUN apk --no-cache add curl httpie jq && \
    curl -L# https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl

