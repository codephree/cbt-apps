from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class UserLogin(FlaskForm):
    username = StringField('Enter Username', validators=[InputRequired()])
    password = PasswordField('Enter password', validators=[InputRequired()])
    login = SubmitField('Sign in')

class UserSignUp(FlaskForm):
    fullname = StringField('Enter Full Name', validators=[InputRequired()])
    email = StringField('Enter Email', validators=[InputRequired()])
    username = StringField('Enter Username', validators=[InputRequired()])
    password = PasswordField('Enter password', validators=[InputRequired()])
    signup = SubmitField('Sign up')