from flask import Flask

from config import Config
from database import db
from group_api import group_router
from user_api import user_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(user_router)
    app.register_blueprint(group_router)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
