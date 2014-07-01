#/bin/sh

ETCD=${ETCD:-172.17.42.1:4001}
confd -verbose -onetime -node $ETCD

/elasticsearch/bin/elasticsearch $@