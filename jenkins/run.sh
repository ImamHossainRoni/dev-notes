
sudo docker stop jenkins-master
sudo docker rm jenkins-master
sudo docker run -p 8080:8080 --name=jenkins-master jenkins/jenkins


