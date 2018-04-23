from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  account = StringField('account', validators = [DataRequired()])
  passwrd = StringField('passwrd', validators = [DataRequired()])

