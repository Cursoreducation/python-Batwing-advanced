from flask import Flask

from user_api import user_router

app = Flask(__name__)
app.register_blueprint(user_router)

status_code_created = 201


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
