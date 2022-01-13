
docker run -p 80:8080 -d --name jenkins jenkins/jenkins:lts-jdk11

https://www.twilio.com/blog/2018/06/continuous-delivery-with-jenkins-and-github-2.html

on jenkins server:
    ssh-keygen -m PEM -t rsa -b 4096 # PEM to make it compatible with jenkins. also later do -C jenkins@jenkins-1
    cat ~/.ssh/id_rsa.pub # copy from here
    # later ssh -T 10.132.0.7 # to test connection

    docker exec jenkins mkdir /var/jenkins_home/.ssh
    docker cp ~/.ssh/id_rsa jenkins:/var/jenkins_home/.ssh/id_rsa
    docker cp ~/.ssh/id_rsa.pub jenkins:/var/jenkins_home/.ssh/id_rsa.pub
    docker exec --user root jenkins chown -R jenkins /var/jenkins_home/.ssh
    # alternatively just copy the key into the field? :|

on nginx and flask servers:
    # paste ssh keys into VM metadata
    # not sudo nano ~/.ssh/authorized_keys # paste pub key in here

nginx server via jenkins:
    rm -rf MyFlix
    git clone https://github.com/fpavlica/MyFlix.git 
    chmod u+x ./MyFlix/api/build.sh # or MyFlix/web/build.sh
    bash ./MyFlix/api/build.sh # as above

jenkins plugins:
 * publish over SSH