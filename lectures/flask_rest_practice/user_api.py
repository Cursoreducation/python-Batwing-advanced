import http

from flask import Blueprint, Response, request
from marshmallow import ValidationError

from auth import check_authenticated
from db.db import UserDB
from serializers.user import UserSchema

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
@check_authenticated
def get(user):
    print(f'{user} called get_users endpoint')
    users = db.get_all()
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user


@user_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = UserSchema()
    try:
        user = schema.load(data)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    # if name and isinstance(name, str) and len(name) >= 2 and
    new_user = db.add(user)
    user_json = schema.dump(new_user)
    return user_json, http.HTTPStatus.CREATED


@user_router.route('', methods=['PUT'])
def update():
    return


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
