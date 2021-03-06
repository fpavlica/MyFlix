from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Blueprint('api', 'api')

from dbaccess import dbapi
api.register_blueprint(dbapi, url_prefix='/db')

from user_accounts import uaapi
api.register_blueprint(uaapi, url_prefix='/accounts')

app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

