# import os
from flask import Flask
from config import Config
from user_api import user_router
from flask_session import Session
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


def create_app():
    app = Flask(__name__)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(user_router)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
