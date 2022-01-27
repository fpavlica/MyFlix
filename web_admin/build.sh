docker stop nginx
docker rm nginx
docker build -t myflix MyFlix/web_admin
docker run --name nginx -d -p 80:80 myflix