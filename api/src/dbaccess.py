from flask.blueprints import Blueprint
from flask import json, jsonify, request, Response
import pymongo

dbapi = Blueprint("dbaccess", __name__)
mongourl = "mongodb://35.240.101.156:80"
# mongourl = "mongodb://35.240.101.156:80"

tempfilms = [
    {
        "name": "movie1",
        "v_host": "https://storage.cloud.google.com/myflix-video-storage/",
        "v_fname": "video_test.mp4",
    },
    {
        "name":"movie2",
        "v_host": "temp.com",
        "v_fname": "temp.mp4"
    }
]


@dbapi.route("/")
def dbtest():
    return "no api here"


@dbapi.route("/films")
def films():
    return jsonify(tempfilms)


@dbapi.route("/get_film_link/<film_name>")
def get_film_link(film_name):
    film = tempfilms[0]
    # if (film_name == film.name):
    if (film_name == film["name"]):
        print(f"film found: { film_name}")
    else:
        print(f"film not found: {film_name}")

    host = film["v_host"]
    # host = film.v_host
    fname = film["v_fname"]
    # fname = film.v_fname
    return jsonify({"url": host+fname})


@dbapi.route("/add_film", methods=['POST'])
def add_film():
    # data = request.form
    data = request.json

    if (data is None):
        return "no data was provided", 400
    if ("filmname" not in data or
        "vlink" not in data or 
        "credit" not in data):
        return "bad data", 400
    if( data["filmname"] is None or data["filmname"] == "" or 
        data["vlink"]    is None or data["vlink"]    == "" or 
        data["credit"]   is None or data["credit"]   == ""):
        return "empty data", 406

    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"] # todo put these in a function later

    # could also do a check if already exists and send 409
    x = filmscol.insert_one({
        "name": data["filmname"],
        "vlink": data["vlink"],
        "credit": data["credit"]
    })
    print(f'Inserted {data} with id {x.inserted_id}.')

    # implicit 500 on write fail bc insert_one throws an exception on error
    return "", 201

@dbapi.route("/films_in_db_temp/")
def films_in_db_temp():
    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"]
    found = list(filmscol.find())

    # from bson import json_util
    for x in found:
        print(f"found: {x}")
        x.pop("_id")
    return jsonify(found)
    # return Response(json_util.dumps({"temp":found}), mimetype = 'application/json')
