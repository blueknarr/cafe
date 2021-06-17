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
