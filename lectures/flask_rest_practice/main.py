import http
import os

from flask import Flask, redirect

from user_api import user_router


app = Flask(__name__)

env_type = os.environ.get('FLASK_ENV_TYPE')
if env_type == 'prod':
    from config import ProdConfig as Config
elif env_type == 'dev':
    from config import DevConfig as Config
else:
    from config import Config

app.config.from_object(Config)
app.register_blueprint(user_router)


@app.route('/')
def index():
    return "hello world"


@app.errorhandler(404)
def handle_404(e):
    return 'Sorry, this resource does not exist', http.HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run()
