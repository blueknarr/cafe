from flask import Blueprint, render_template, request, make_response

from app import db

bp = Blueprint(
    'main',
    __name__,
    url_prefix='/'
)


@bp.route('', methods=['GET'])
def index():
    token = request.cookies.get('loginToken')
    login = False
    if token:
        login = True
    return render_template('index.html', login=login)


@bp.route('/storePage', methods=['GET'])
def store():
    token = request.cookies.get('loginToken')
    login = False
    if token:
        login = True
    return render_template('storeList.html', login=login)


@bp.route('/storeDetails', methods=['GET'])
def detail():
    token = request.cookies.get('loginToken')
    login = False
    if token:
        login = True
    return render_template('storeDetail.html', login=login)
