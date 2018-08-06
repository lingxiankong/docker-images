FROM python:alpine
MAINTAINER Lingxian Kong <lingxiankong@catalyst.net.nz>

ARG barbican_branch=master
ARG barbican_repo=https://github.com/openstack/barbican.git
ARG barbican_wsgi_ini=/etc/barbican/barbican-uwsgi.ini

ENV BARBICAN_WSGI_INI ${barbican_wsgi_ini}

WORKDIR /opt
RUN apk add --no-cache \
      git \
      linux-headers \
      build-base \
      gcc \
      openssl-dev \
      libffi-dev \
      libxslt-dev \
      libxml2-dev \
      musl-dev \
      uwsgi && \
    pip install --upgrade pip && \
    pip install pymysql uwsgi python-openstackclient python-barbicanclient && \
    git clone -b $barbican_branch --single-branch $barbican_repo /opt/barbican && \
    mkdir -p /etc/barbican /var/log/barbican && \
    pip install -e /opt/barbican/

EXPOSE 9311

CMD uwsgi --ini $BARBICAN_WSGI_INI

