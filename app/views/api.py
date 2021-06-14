import datetime
import hashlib
import jwt

from flask import Blueprint, request, jsonify
from app import db, JWT_SECRET

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)


@bp.route('/login', methods=['POST'])
def login():
    id_login = request.form['id']
    pw_login = request.form['pw']

    pw_hash = hashlib.sha256(pw_login.encode()).hexdigest()

    user = db.users.find_one({'id': id_login, 'pw': pw_hash}, {'_id': False})

    if user:
        expiration_time = datetime.timedelta(hours=1)
        payload = {
            'id': id_login,
            'exp': datetime.datetime.utcnow() + expiration_time
        }
        token = jwt.encode(payload, JWT_SECRET)
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'failed'})
