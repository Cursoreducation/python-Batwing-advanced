from database import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(300), nullable=False, unique=True)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    groups = db.relationship("Group", secondary="UserGroup")
