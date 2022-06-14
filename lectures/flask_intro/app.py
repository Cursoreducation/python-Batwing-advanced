from flask import Flask

app = Flask(__name__)

with app.app_context():
    from routes.main import *

if __name__ == "__main__":
    app.run(port=5000,  host='0.0.0.0', debug=True)