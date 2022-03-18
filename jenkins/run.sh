
sudo docker stop jenkins-master
sudo docker rm jenkins-master
# sudo docker run -p 8080:8080 --name=jenkins-master jenkins/jenkins
sudo docker run -p 8080:8080 -p 50000:50000 --name=jenkins-master -d jenkins/jenkins


