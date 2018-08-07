#!/bin/sh

mkdir -p /opt/barbican /etc/barbican /var/log/barbican
chown -R barbican:1000 /opt/barbican /etc/barbican /var/log/barbican

exec gosu barbican uwsgi --ini $BARBICAN_WSGI_INI