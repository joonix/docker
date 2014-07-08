# ElasticSearch

This container is for creating a [ElasticSearch][es] cluster utilizing [etcd][etcd] for discovery and configuration.

These configuration values are fetched from etcd and added as configuration:

**/elasticsearch/name** -> cluster.name  
**/services/elasticsearch/node1** -> discovery.zen.ping.unicast.hosts

[etcd]: https://github.com/coreos/etcd
[es]: http://www.elasticsearch.org/

## Example

Map same port numbers on host and configure what hostname to publish to other nodes in the cluster:

```bash
docker run -p 9200:9200 -p 9300:9300 joonix/elasticsearch -Des.network.publish_host=reachable.host.name
```

## Plugins

You can choose to install plugins before elasticsearch starts by setting `PLUGINS` variable:

```bash
docker run -ti -e PLUGINS="mobz/elasticsearch-head" -p 9200:9200 -p 9300:9300 joonix/elasticsearch
```