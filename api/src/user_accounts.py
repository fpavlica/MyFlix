from os import getpgid
from bson.objectid import ObjectId
from flask.blueprints import Blueprint
from flask import json, jsonify, request, Response, abort
import pymongo

import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.exceptions import InvalidKey

uaapi = Blueprint("user_access", __name__)
mongourl = "mongodb://35.240.101.156:80"


# some helper functions for password checks
def asBytesIfHexString(s):
    return bytes.fromhex(s) if type(s) is str else s
def asHexStringIfBytes(b):
    return b.hex() if type(b) is bytes else b
    
def pwToBytes(pw):
    return pw.encode('ascii')


def getKDF(salt):
    print(f'in getkdf salt is {salt}, type {type(salt)}')
    salt = asBytesIfHexString(salt)
    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

def getPwHash(pw):
    salt = os.urandom(16)
    kdf = getKDF(salt)
    key = kdf.derive(pwToBytes(pw))
    return key, salt

def verifyPw(pw, salt, expected):
    pw = pwToBytes(pw)
    salt = asBytesIfHexString(salt)
    expected = asBytesIfHexString(expected)
    kdf = getKDF(salt)

    try:
        kdf.verify(key_material=pw, expected_key=expected)
        return True
    except InvalidKey:
        return False


@uaapi.route("/register", methods=["POST"])
def register():
    print(f"register attempt: {request.json}")

    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["usersdb"]
    userscol = mydb["users"]

    # ensure user isn't already registered
    # probably would've been better to use find_one
    try:
        num_existing_u = userscol.count_documents({"username":request.json["username"]})
        if (num_existing_u > 0):
            return "user already exists", 409
    except KeyError as ke:
        print(f"KeyError in register: {ke}")
        pass
    
    # generate password crypto hash of password
    # (in this case the "password" is the hash of the original password)
    pwh, salt = getPwHash(request.json["password"])

    x = userscol.insert_one({
        "username": request.json["username"],
        "password": asHexStringIfBytes(pwh),
        "salt":     asHexStringIfBytes(salt),
    })

    return "", 201

@uaapi.route("/login", methods=["POST"])
def login():
    print(f"login attempt: {request.json}")

    mongoclient = pymongo.MongoClient(mongourl)
    mydb = mongoclient["usersdb"]
    userscol = mydb["users"]

    try:
        users = userscol.find({"username":request.json["username"]})
        users = list(users)
        if (len(users) == 0):
            return "no such user", 404

        user = list(users)[0]

        # if verified legit, send an auth token
        if (verifyPw(
            pw = request.json["password"], 
            salt = user["salt"], 
            expected = user["password"])):
            print(f"authorised user: {request.json['username']}")
            return "authorised", 200
            pass
        else:
            # bad password, send a 401 Unauthorised
            abort(401)  
    except KeyError as ke:
        print(f"KeyError in login, {ke}")
        return "user not found", 404
    

    pass