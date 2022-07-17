import http
# import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect
from config import Config
from user_api import user_router
from shop_api import shop_router
from database import db

app = Flask(__name__)

# env_type = os.environ.get('FLASK_ENV_TYPE')
# if env_type == 'prod':
#     from config import ProdConfig as Config
# elif env_type == 'dev':
#     from config import DevConfig as Config
# else:
#     from config import Config

app.config.from_object(Config)
app.register_blueprint(user_router)
app.register_blueprint(shop_router)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(user_router)
    app.register_blueprint(shop_router)
    return app


def setup_db(app):
    with app.app_context():

        db.create_all()
        db.session.commit()



if __name__ == '__main__':
    app = create_app()
    setup_db(app)
    app.run(host="0.0.0.0", debug=True)
