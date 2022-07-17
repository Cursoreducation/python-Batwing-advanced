from flask_sqlalchemy import SQLAlchemy

from database import db
from models.user import User
from main import app
from models.shop import Shop
db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(User(email="yuratsap1999@gmail.com"))
    print("created tables user")
    db.session.add(Shop(name_of_good="caramel", maker="Yura", category_of_good="dessert"))
    db.session.commit()
    print("created tables")
