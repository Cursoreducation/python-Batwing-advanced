import http

from flask import Blueprint, Response, request

from db.db import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)

    if not new_user:
        return "This user is already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_user, http.HTTPStatus.CREATED


@user_router.route('', methods=['PUT'])
def update():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    upd_user = db.update_by_email(name, email, password)

    if not upd_user:
        return "This user doesn't exists", http.HTTPStatus.BAD_REQUEST
    else:
        return "User's data has been changed", http.HTTPStatus.CREATED


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    res = db.delete_by_email(email)
    return res