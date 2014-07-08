#/bin/sh

# docker0 is also the default gateway
DOCKER0=$(ip route show | grep ^default | awk '{print $3}')
ETCD=${ETCD:-$DOCKER0:4001}
confd -verbose -onetime -node $ETCD

/elasticsearch/bin/elasticsearch $@