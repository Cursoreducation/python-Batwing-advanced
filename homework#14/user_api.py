import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from database import db
from models.user import User
from serializers.user import UserSchema

user_router = Blueprint('user', __name__, url_prefix='/user')


@user_router.route('')
def get():
    user_schema = UserSchema()

    users = User.query.order_by(User.email)
    users_json = user_schema.dump(users, many=True)
    return jsonify(users_json)


@user_router.route('/<int:id_>')
def retrieve(id_):
    user_schema = UserSchema()
    user = User.query.filter_by(id=id_).first()
    user_json = user_schema.dump(user)
    return jsonify(user_json)


@user_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = UserSchema()
    try:
        user_data = schema.load(data)
        new_user = User(email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()

        new_user_json = schema.dump(new_user)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_user_json


@user_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = UserSchema()
    try:
        user_data = schema.load(data)
        user = User.query.filter_by(id=id_).first()
        user.email = user_data['email']
        db.session.add(user)
        db.session.commit()

        new_user_json = schema.dump(user)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_user_json


@user_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    User.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT