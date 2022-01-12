docker stop flask
docker rm flask
docker build -t myflask MyFlix/api
docker run --name flask -d -p 80:5000 myflask