import os

from flask import Flask
from flask.cli import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_HOST = os.environ['MONGODB_HOST']

client = MongoClient(MONGODB_HOST)


def create_app(database_name='cafe'):
    app = Flask(__name__)
    db = client.get_database(database_name)

    return app
