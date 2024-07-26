from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,DataRequired, Length, EqualTo

class registerForm(FlaskForm):
    firstname = StringField('Enter firstname', validators=[DataRequired()] )
    lastname = StringField('Enter lastname', validators=[DataRequired()] )
    email = StringField('Enter email', validators=[DataRequired()] )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField( "Repeat password",validators=[DataRequired(), EqualTo("password", message="Passwords must match."),], )
    submit = SubmitField("Register")

class loginForm(FlaskForm):
    email = StringField('Enter email', validators=[DataRequired()] )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField("Login")