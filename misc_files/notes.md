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
    * done
4. sql server for video metadata inc. filename?
    * done
5. actual myflix html app
    * decide order of login admin displays
    * basic admin page form first [/], then individual movie page [/], then movies list [/], then login feature [-]
6. fill some temp videos
    * include a credits field in db
    * thumbnails
    * category
7. API identification codes (middleware) and security check ups
8. Jenkins/git/gcloud dev and main branches 
    * maybe some env type variables for each if that's easy
    * ^ env won't work, possibly a cookie to switch bw localhost/dev/main
9. security check up
10. make it pretty with CSS
11. ???


### new order:
0. log in redirects and catch db empty errors
    * done
1. flask-login authentication if it's easy
    * maybe do this later
2. thumbnails and category
    * filter by category. maybe later, after server and jenkins reorganisation
3. jenkins server creates. But how kill server? maybe not. maybe just jenkins dev/main servers
    *best do this tomorrow, need sleep and will have time
4. change ports to right ones (mongo server) and open firewall

## website structure:

Index ~~ login 
login -> view catalogue. with thumbnails
catalogue -> movie page. like /video?v=vid_name_or_id, then API to get link and video db to get video link. is this possible?? (also see embeds)   
catalogue -> filter catalogue by category

### in other words, pages:
* user login
* catalogue display with sort [/] sort [-]
* video view [/]
* admin page [/] (also admin login? on separate server?)

## database structure:
### film entries:
ID, name, video file host, video file link, date added, category/ies?, thumbnail file link?, length (auto?)

### user entries:
ID?, username, history?, liked_videos? <- those probs need nosql

### possible categories:
just a list of categories - could be a simple array in a misc table.
Other things in misc table could be 

### operations:
* get all films [/]
* get all films by category
* get film's video link [/]
* add a film with details [/]
* add thumbnail
* login user (send cookie token)
* register user
* get user pw hash for login
* get/set user's seen videos
* get/set user's liked videos


## misc
* other  video link: https://storage.cloud.google.com/myflix-video-storage/video2.mp4
* links to public domain videos: https://guides.library.harvard.edu/c.php?g=310751&p=2072820#s-lg-page-section-2072820
* NPS public domain videos: https://www.nps.gov/grca/learn/photosmultimedia/b-roll_hd_index.htm
* big buck bunny: https://download.blender.org/peach/bigbuckbunny_movies/


Put both catalogue and view film into one file as two components. maybe have one js file for each and then a short connecting one but only if time.