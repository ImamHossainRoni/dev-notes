pull_elasticsearch() {
    sudo docker network create elastic
    sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.1

}

pull_elasticsearch
