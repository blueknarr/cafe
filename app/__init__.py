import os

from flask import Flask
from flask.cli import load_dotenv
from pymongo import MongoClient

load_dotenv()
JWT_SECRET = os.environ['JWT_SECRET']
MONGODB_HOST = os.environ['MONGODB_HOST']
client = MongoClient(MONGODB_HOST)
db = None


def create_app(database_name='cafe'):
    app = Flask(__name__)
    global db
    db = client.get_database(database_name)

    from app.views import main, api
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)

    return app
