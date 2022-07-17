from flask import Flask

from user_api import user_router
from book_api import book_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(book_router)

status_code_failed = 404


@app.route('/')
def index():
    return "hello world"


@app.route('/<smth>')
def fail(smth):
    return "You failed, try another url", status_code_failed


if __name__ == '__main__':
    app.run(debug=True)