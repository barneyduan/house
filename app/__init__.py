from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models