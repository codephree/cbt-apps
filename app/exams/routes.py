from flask import render_template, redirect, flash, current_app, request, url_for
from app.exams import bp
from app.extensions import db
from app.forms.question import ExamForm
from app.models.question import Question
from flask_login import login_required, current_user
from app.helpers import Helper
import random

@bp.route('/', methods=['POST','GET'])
@login_required
def index():
    Helper().check_not_admin()
    question = db.session.query(Question).filter(
                        Question.id == random.randint(1,50)).first()
    single_question = []
    for options in Helper().split_string_to_radio(question.options):
        single_question.append({
            'question': question.question,
            "option_a": options[0],
            "option_b": options[1],
            "option_c": options[2],
            "option_d": options[3]
        })

    return render_template('exams/index.html', questions=single_question)


# def keep():
#     question = db.session.query(Question).filter(
#                         Question.id == random.randint(1,50)).first()
#     single_question = []
#     for options in Helper().split_string_to_radio(question.options):
#         single_question.append({
#             'question': question.question,
#             "option_a": options[0],
#             "option_b": options[1],
#             "option_c": options[2],
#             "option_d": options[3]
#         })

