FROM ubuntu:14.04
MAINTAINER Johnny Bergström <johnny@joonix.se>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y upgrade

# Setup dependencies of aws client
RUN apt-get -y install python-pip
RUN pip install boto

VOLUME /mnt

ADD client.py /data/client.py

ENTRYPOINT ["python", "/data/client.py"]