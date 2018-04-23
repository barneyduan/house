from datetime import datetime
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  name = db.Column(db.String(20), index = True)
  email = db.Column(db.String(64), index = True)
  account = db.Column(db.String(64), index = True, unique = True)
  passwrd = db.Column(db.String(64), index = True)

  def __repr__(self):
    return '<User %r>' % (self.name)

