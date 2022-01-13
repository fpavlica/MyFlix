#docker stop mymysql
#docker rm mymysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=password -d mysql:8

## could have this for the test db server, 
## but for release it's probably best to keep the same one database
## so build one manually

# change port later
docker run --name mymongo -p 80:8081 -d mongo:5