import http

from flask import request, abort

from db.db import UserDB

db = UserDB()


def check_authenticated(f):
    def wrapper(*args, **kwargs):
        if 'Authorization_email' not in request.headers:
            abort(http.HTTPStatus.UNAUTHORIZED)

        auth_header = request.headers['Authorization_email']

        if user := db.retrieve_by_email(auth_header) is None:
            abort(http.HTTPStatus.UNAUTHORIZED)

        return f(user, *args, **kwargs)
    return wrapper
