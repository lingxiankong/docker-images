FROM python:3.8-slim-buster
LABEL maintainer="anlin.kong@gmail.com"

RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean
RUN pip install --upgrade --no-cache-dir httpie jq python-openstackclient python-swiftclient python-heatclient python-octaviaclient python-magnumclient aodhclient python-troveclient

copy bashrc /home/bashrc

# Add a volume so that a host filesystem can be mounted 
# Ex. `docker run -v $PWD:/data lingxiankong/openstack-cli`
VOLUME ["/data"]

# Default is to start a shell, e.g.
# docker run -it --rm --name openstack-cli -v /etc/openstack:/etc/openstack lingxiankong/openstack-cli:1.0.0
# source /home/bashrc
# export OS_CLOUD=trove
CMD ["/bin/bash"]
