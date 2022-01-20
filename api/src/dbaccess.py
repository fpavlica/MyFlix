from bson.objectid import ObjectId
from flask.blueprints import Blueprint
from flask import json, jsonify, request, Response
import pymongo

dbapi = Blueprint("dbaccess", __name__)
from env import mongourl


@dbapi.route("/")
def dbtest():
    return "no api here", 400

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
