import http

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from database import db
from user_api import user_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(user_router)
    return app


def setup_db(app):
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    setup_db(app)
    app.run(host="0.0.0.0")
