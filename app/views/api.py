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


@bp.route('/register', methods=['POST'])
def register():
    id_register = request.form['id']
    pw_register = request.form['pw']
    place_register = request.form['place']

    pw_hash = hashlib.sha256(pw_register.encode()).hexdigest()
    db.users.insert_one({'id': id_register, 'pw': pw_hash, 'place': place_register})

    return jsonify({'result': 'success', 'msg': '회원 가입을 축하합니다.'})


@bp.route('/checkId', methods=['POST'])
def check_id():
    id_check = request.form['id']

    if db.users.find_one({'id': id_check}, {'_id': False}):
        return jsonify({'result': 'failed', 'msg': '사용중인 아이디입니다.'})
    else:
        return jsonify({'result':'success','msg':'사용 가능한 아이디입니다.'})