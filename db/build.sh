#docker stop mymysql
#docker rm mymysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=password -d mysql:8

## could have this for the test db server, 
## but for release it's probably best to keep the same one database
## so build one manually

# change port later
docker run --name mongo -p 27017:27017 -d mongo:5

# # to export database:
# mongoexport --host="35.195.52.146:27017" --forceTableScan --db=filmsdb --collection=films --out=films.json
# mongoexport --host="35.195.52.146:27017" --forceTableScan --db=usersdb --collection=users --out=users.json

# # to re-import. may need to drop first.
# mongoimport --host="35.195.52.146:27017" --db=filmsdb --collection=films films.json
# mongoimport --host="35.195.52.146:27017" --db=usersdb --collection=users users.json