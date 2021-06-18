from flask import Blueprint, request, jsonify
from app import db

bp = Blueprint(
    'store',
    __name__,
    url_prefix='/store'
)


@bp.route('/list', methods=['POST'])
def store_list():
    parameter = request.form['parameter']
    pair = parameter.split('+')
    stores = list(db.cafes.find({pair[0]: pair[1]}, {'_id': False}))
    return jsonify({'result': 'success', 'stores': stores})


@bp.route('/detail', methods=['POST'])
def store_detail():
    title = request.form['title']
    store = db.cafes.find_one({'title': title}, {'_id': False})
    return jsonify({'result': 'success', 'store': store})
