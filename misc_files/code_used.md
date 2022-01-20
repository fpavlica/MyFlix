
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

gcloud create dev-frontend server:
    gcloud compute instances create myflix-dev-frontend --project=triple-rookery-294811 --zone=europe-west1-b --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --metadata=ssh-keys=frpavlica:ssh-rsa\ AAAAB3NzaC1yc2EAAAADAQABAAACAQCjVfr10LRgpCaUo6R1pyn6ogaTAjOSxmCPYfmN\+nEQtAO1XTmNGWrucFQALPwFVZlFuUipVQiTc870s\+OQIKSV\+Ye57Wii2xac/zkhJoq9Bi3b124OZWoeD5ft3vg1t5j/uRBt3Bh6\+uVAgorlRDZ6dqOPqj/nSJYyH3iXNzn7tSvh4f6/a1KNM8NPT9VDdTmL6dhdTQOKfjwUTUpMShITh5VMs5/7nnjrIemjYAO609vUkNIPVbbls1OXXDBoWeDirpC6/QMndLyoKfhR4fDF0qSZ2tuNnzH07hfNnVzXmmllRf3ceDfezzn5qQBVLV4tIgu6iZKDw/wzcvtnVfICC7eA\+gXLj0sRI8GYNVYfOGtQXN0uA5z9knb6EhLI4Dy95JNeS4C3hT6F41ieMDLoeewzog3/VYMGZgl0WOP3RlZMqFul2asz\+ettWqUAz45RfvLiup5787\+rJmIVNXU2tj9KjidDmb0DeP0RNgMQUgD/Xiqyp0OeUjHE0wS6xwKDWM4nvF3C8DMzynXiUOAgNYEI5i6k/uvcP9THy\+n2fbZpHZrljGw0ORi7K1s6VXKR4LbQkT9GlOV1a5vpeXoZV8Pkh1ODCHoEUQQJ7ofTEXld3SfKrjb5QMNsCWFQDp0cvlf38AnqhKMBiR6vVEUNFkhGdby09vhysQcM/Ps3WQ==\ frpavlica@jenkins-1 --maintenance-policy=MIGRATE --service-account=755721276176-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server --create-disk=auto-delete=yes,boot=yes,device-name=myflix-dev-frontend,image=projects/cos-cloud/global/images/cos-81-12871-1317-8,mode=rw,size=10,type=projects/triple-rookery-294811/zones/europe-west1-b/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any


jenkins server public SSH key:
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCjVfr10LRgpCaUo6R1pyn6ogaTAjOSxmCPYfmN+nEQtAO1XTmNGWrucFQALPwFVZlFuUipVQiTc870s+OQIKSV+Ye57Wii2xac/zkhJoq9Bi3b124OZWoeD5ft3vg1t5j/uRBt3Bh6+uVAgorlRDZ6dqOPqj/nSJYyH3iXNzn7tSvh4f6/a1KNM8NPT9VDdTmL6dhdTQOKfjwUTUpMShITh5VMs5/7nnjrIemjYAO609vUkNIPVbbls1OXXDBoWeDirpC6/QMndLyoKfhR4fDF0qSZ2tuNnzH07hfNnVzXmmllRf3ceDfezzn5qQBVLV4tIgu6iZKDw/wzcvtnVfICC7eA+gXLj0sRI8GYNVYfOGtQXN0uA5z9knb6EhLI4Dy95JNeS4C3hT6F41ieMDLoeewzog3/VYMGZgl0WOP3RlZMqFul2asz+ettWqUAz45RfvLiup5787+rJmIVNXU2tj9KjidDmb0DeP0RNgMQUgD/Xiqyp0OeUjHE0wS6xwKDWM4nvF3C8DMzynXiUOAgNYEI5i6k/uvcP9THy+n2fbZpHZrljGw0ORi7K1s6VXKR4LbQkT9GlOV1a5vpeXoZV8Pkh1ODCHoEUQQJ7ofTEXld3SfKrjb5QMNsCWFQDp0cvlf38AnqhKMBiR6vVEUNFkhGdby09vhysQcM/Ps3WQ== frpavlica@jenkins-1