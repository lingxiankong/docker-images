FROM python:3.8-slim-buster
LABEL maintainer="anlin.kong@gmail.com"

RUN apt-get update \
  && apt-get install gcc curl jq -y \
  && apt-get clean
RUN pip install --upgrade --no-cache-dir \
  httpie \
  python-openstackclient \
  python-swiftclient \
  python-heatclient \
  python-octaviaclient \
  python-magnumclient \
  aodhclient \
  python-troveclient \
  python-barbicanclient

# Put everything (bashrc, clouds.yaml, scripts, etc.) inside the openstack_shared_dir
# docker run -it --rm --name openstack -v openstack_shared_dir:/etc/openstack lingxiankong/openstack-cli:1.0.0
# source /etc/openstack/bashrc
ENTRYPOINT ["/bin/bash"]
