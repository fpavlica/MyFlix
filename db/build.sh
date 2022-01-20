#docker stop mymysql
#docker rm mymysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=password -d mysql:8

## could have this for the test db server, 
## but for release it's probably best to keep the same one database
## so build one manually

# change port later
# docker run --name mongo -p 80:27017 -d mongo:5
docker run --name mongo -p 27017:27017 -d mongo:5