from database import db


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)
    users = db.relationship("User")
