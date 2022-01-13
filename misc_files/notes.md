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

## database structure:
### film entries:
ID, name, video file host, video file link, date added, category/ies?, thumbnail file link?, length (auto?)

### user entries:
ID?, username, history?, liked_videos? <- those probs need nosql

### possible categories:
just a list of categories - could be a simple array in a misc table.
Other things in misc table could be 

### operations:
* get all films
* get all films by category
* get film's video link
* add a film with details
* add thumbnail
* register user
* get user pw hash for login
* get/set user's seen videos
* get/set user's liked videos