from database import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
