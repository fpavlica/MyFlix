# Structure

## repo directories:
* / : readme, other dirs
* /web : html and js files that will be served on nginx. also dockerfile, docker run command and such?
* /api : Flask API, also with dockerfile
* /sql ? for sql commands setting up the mysql db
* /video_links ? for links to open source videos, maybe the script to download them to the video storage server


## git branches:
main (release) <- dev <- whatever_im_working_on

Jenkins build jobs on both main and test. Maybe on working??
A server for both main and test?

## servers:
* Nginx server for /web
* Flask server for /api
* SQL server for /sql things
* Storage place for the videos
* possibly one for admin stuff: app that adds videos to storage and/or db
* later possibly also recomm engine, login service, load balancer

Possible extra one of each for dev branch for nginx, flask, sql

## order of work:

1. jenkins set up to deploy hello_world from /web onto its server
    * test if this works with git updates
    * done
2. jenkins set up to deploy api, temporary API with hard-coded things
    * done
3. video server
    * try make it fetch the video link from the api
4. sql server for video metadata inc. filename?
5. actual myflix html app
6. ???

## website structure:

Index ~~ login 
login -> view catalogue. with thumbnails
catalogue -> movie page. like /video?v=vid_name_or_id, then API to get link and video db to get video link. is this possible??   
catalogue -> filter catalogue by category