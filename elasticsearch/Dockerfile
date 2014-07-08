FROM dockerfile/java
MAINTAINER Johnny Bergström <johnny@joonix.se>

# Install ElasticSearch.
RUN \
  cd /tmp && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.1.tar.gz && \
  tar xvzf elasticsearch-1.2.1.tar.gz && \
  rm -f elasticsearch-1.2.1.tar.gz && \
  mv /tmp/elasticsearch-1.2.1 /elasticsearch

# Setup configuration from etcd
RUN \
  wget https://github.com/kelseyhightower/confd/releases/download/v0.2.0/confd_0.2.0_linux_amd64.tar.gz && \
  tar xzf confd_0.2.0_linux_amd64.tar.gz && \
  rm -f confd_0.2.0_linux_amd64.tar.gz && \
  mv confd /usr/local/bin/confd

ADD conf.d /etc/confd/conf.d
ADD templates /etc/confd/templates
ADD start.sh /elasticsearch/start.sh

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
ENTRYPOINT ["/bin/sh", "/elasticsearch/start.sh"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300