
sudo docker stop jenkins-master
sudo docker rm jenkins-master
# sudo docker run -p 8080:8080 --name=jenkins-master jenkins/jenkins
sudo docker run -p 8080:8080 -p 50000:50000 --name=jenkins-master -d jenkins/jenkins

# To execute jenkins in interactive shell
# docker exec -it jenkins-master bash

# To run existing jenkins docker image
sudo docker run -p 8080:8080 -p5000:5000 -d jenkins/jenkins

