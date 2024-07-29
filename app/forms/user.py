from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

class UserCreationForm(FlaskForm):
    file = FileField('Upload sr in csv', validators=[InputRequired()])
    create = SubmitField('Upload')