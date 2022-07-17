from database import db


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_good = db.Column(db.String(300), nullable=False, unique=True)
    maker = db.Column(db.String(300), nullable=False, unique=True)
    category_of_good = db.Column(db.String(300), nullable=False, unique=True)