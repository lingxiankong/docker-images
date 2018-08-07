FROM python:alpine
MAINTAINER Lingxian Kong <lingxiankong@catalyst.net.nz>

ARG barbican_branch=master
ARG barbican_repo=https://github.com/openstack/barbican.git
ARG barbican_wsgi_ini=/etc/barbican/barbican-uwsgi.ini

ENV BARBICAN_WSGI_INI ${barbican_wsgi_ini}
USER root

COPY ./docker-entrypoint.sh /
RUN adduser -HDs /bin/sh barbican

RUN apk add --no-cache \
      dpkg \
      curl \
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
    curl -sSL -o /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \
    chmod +x /usr/local/bin/gosu && \
    pip install --upgrade pip && \
    pip install pymysql uwsgi python-openstackclient python-barbicanclient && \
    git clone -b $barbican_branch --single-branch $barbican_repo /opt/barbican && \
    pip install -e /opt/barbican/

EXPOSE 9311

ENTRYPOINT ["/docker-entrypoint.sh"]
