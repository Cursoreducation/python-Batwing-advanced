from flask_sqlalchemy import SQLAlchemy

from main import app

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    # db.session.add(User(email="yuratsap1999@gmail.com", password = "123",first_name = "yura", last_name = "tsap"))
    # print("created tables user")

