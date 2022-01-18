from bson.objectid import ObjectId
from flask.blueprints import Blueprint
from flask import json, jsonify, request, Response
import pymongo

dbapi = Blueprint("dbaccess", __name__)
mongourl = "mongodb://35.240.101.156:80"

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
    return "no api here", 400


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


@dbapi.route("/get_film_by_id/<id>")
def get_film_by_id(id):
    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"]
    film = list(filmscol.find({"_id": ObjectId(id)}))
    film[0]["_id"] = str(film[0]["_id"])
    # todo handle bad request (film not present)
    return jsonify(film[0]), 200

@dbapi.route("/add_film", methods=['POST'])
def add_film():
    # data = request.form
    data = request.json

    if (data is None):
        return "no data was provided", 400
    exp_fields = ["filmname", "categories", "vlink", "thumblink", "credit"]
    for ef in exp_fields:
        if (ef not in data):
            return "bad data", 400
    if( data[ef] is None or data[ef] == ""):
        return "missing or empty data", 406

    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"] # todo put these in a function later

    # later check if thumblink is empty, send 202 accepted, then download file, ffmpeg to generate thumbnail, gcloud upload, and remove video and picture

    # could also do a check if already exists and send 409
    x = filmscol.insert_one({
        "name": data["filmname"],
        "categories": data["categories"],
        "vlink": data["vlink"],
        "thumblink": data["thumblink"],
        "credit": data["credit"]
    })
    print(f'Inserted {data} with id {x.inserted_id}.')

    # implicit 500 on write fail bc insert_one throws an exception on error
    return "", 201

@dbapi.route("/list_films/<category>")
def list_films(category = "all"):
    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"]
    found = list(filmscol.find())

    # from bson import json_util
    for x in found:
        print(f"found: {x}")
        x["_id"] = str(x["_id"])
    return jsonify(found), 200
    # return Response(json_util.dumps({"temp":found}), mimetype = 'application/json')


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
    return jsonify(found), 200
    # return Response(json_util.dumps({"temp":found}), mimetype = 'application/json')
