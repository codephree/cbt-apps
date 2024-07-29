from flask_wtf import FlaskForm
from wtforms import FileField,RadioField, SubmitField
from wtforms.validators import InputRequired

class QuestionCreationForm(FlaskForm):
    file = FileField('Upload sr in csv', validators=[InputRequired()])
    create = SubmitField('Upload')

class ExamForm(FlaskForm):
    question = RadioField("What is your name?",choices=[("option_0",'Oluwafemi'),
                                                         ("option_1",'Oluwafemi1'),
                                                         ("option_2",'Oluwafemi2'),
                                                         ("option_2",'Oluwafemi3')])
    Submit = SubmitField('Submit')