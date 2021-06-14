import pytest
import os

from flask.cli import load_dotenv

import app as flask_app
from pymongo import MongoClient

load_dotenv()
MONGODB_HOST = os.environ['MONGODB_HOST']
test_database_name = 'cafetest'
client = MongoClient(MONGODB_HOST)


@pytest.fixture()
def app():
    test_app = flask_app.create_app((test_database_name))

    yield test_app

    client.drop_database(test_database_name)
    print('테스트 DB 제거 완료')