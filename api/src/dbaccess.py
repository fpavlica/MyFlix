from flask.blueprints import Blueprint
from flask import json, jsonify, request, Response
import pymongo

dbapi = Blueprint("dbaccess", __name__)

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
    data = request.form
    jsondata = request.json
    print(f'Request to add film: {data}')
    print(f'in json: {jsondata}')

    mongoclient = pymongo.MongoClient("mongodb://35.240.101.156:80")
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"]
    x = filmscol.insert_one({"name": "film5", "v_fname":"film5.mp4"})
    print(x.inserted_id)
    print(f'x is {x}')

    return "", 200
    # print(f'Request to add film. Name {data.name}, host {v_host}, fname {v_fname}')

@dbapi.route("/films_in_db_temp/")
def films_in_db_temp():
    mongoclient = pymongo.MongoClient("mongodb://35.240.101.156:80")
    mydb = mongoclient["filmsdb"]
    filmscol = mydb["films"]
    found = list(filmscol.find())

    # from bson import json_util
    for x in found:
        print(f"found: {x}")
        x.pop("_id")
    return jsonify(found)
    # return Response(json_util.dumps({"temp":found}), mimetype = 'application/json')