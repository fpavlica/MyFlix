from flask.blueprints import Blueprint
from flask import jsonify

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

