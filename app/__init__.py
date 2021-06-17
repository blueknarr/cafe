import os

from flask import Flask
from flask.cli import load_dotenv
from pymongo import MongoClient
from flask_cors import CORS
load_dotenv()
JWT_SECRET = os.environ['JWT_SECRET']
MONGODB_HOST = os.environ['MONGODB_HOST']
client = MongoClient(MONGODB_HOST)
db = None


def create_app(database_name='cafe'):
    app = Flask(__name__)
    CORS(app)

    global db
    db = client.get_database(database_name)

    from app.views import main, api, store
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(store.bp)

    return app
