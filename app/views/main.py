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
        print('token true')
        login = True
    else:
        print('token false')
    return render_template('index.html', login=login)


@bp.route('/storePage', methods=['GET'])
def store():
    return render_template('storeList.html')
