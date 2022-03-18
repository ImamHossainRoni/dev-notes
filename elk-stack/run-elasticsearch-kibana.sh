
start_elasticseatch_kibana {
    sudo docker rm es
    sudo docker run --name es -d -p 127.0.0.1:2048:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.1

    es_ip=$(sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' es)

    sudo docker rm kibana
    sudo docker run --name kibana -d -p 127.0.0.1:4096:5601 -e "ELASTICSEARCH_HOSTS=http://$es_ip:9200" docker.elastic.co/kibana/kibana:7.12.1

}

start_elasticseatch_kibana