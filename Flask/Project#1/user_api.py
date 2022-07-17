import http
from flask import Blueprint, request, render_template, session
from marshmallow import ValidationError
from werkzeug.utils import redirect
from database import db
from models.user import User
from serializers.user import UserSchema

# from flask_session import Session

user_router = Blueprint('', __name__, url_prefix='/')


@user_router.route('', methods=['GET', 'POST'])
def get():
    # if not session.get("email"):
    #     return redirect("")
    return render_template("index.html")


@user_router.route('/login', methods=['GET', 'POST'])
def login():
    user_email = request.form.get("email")
    user_password = request.form.get("password")

    if request.method == "POST":

        try:
            if User.query.filter_by(email=user_email).first():
                try:
                    if User.query.filter_by(password=user_password):
                        session["email"] = request.form.get("email")
                        return redirect("/")
                except ValidationError as e:
                    return {'Invalid Username or Password', e.messages}, http.HTTPStatus.UNAUTHORIZED
        except ValidationError as e:
            return {'Invalid Username or Password', e.messages}, http.HTTPStatus.UNAUTHORIZED
    return render_template("Login.html")


@user_router.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")


@user_router.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session["email"] = request.form.get("email")
        data = request.form
        schema = UserSchema()
        # print(data)
        try:
            user_data = schema.load(data)
            new_user = User(first_name=user_data['first_name'], last_name=user_data['last_name'],
                            email=user_data['email'], password=user_data['password'])
            db.session.add(new_user)
            db.session.commit()

        except ValidationError as e:
            return {'erorrs', e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

        return redirect("/")
    return render_template("Register.html")
