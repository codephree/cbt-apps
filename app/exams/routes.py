from flask import render_template, redirect, flash, current_app, request, url_for, session
from app.exams import bp
from app.extensions import db
from app.forms.question import ExamForm
from app.models.question import Question, Question_user_answer
from app.models.user import User_results
from flask_login import login_required, current_user
from app.helpers import Helper
import random
from sqlalchemy import insert, exc

@bp.route('/', methods=['GET'])
@login_required
def index():
    Helper().check_not_admin()
    questions = Helper().load_question_to_user()
    split_string_to_radio= Helper().split_string_to_radio
    return render_template('exams/index.html', questions=questions, split_string_to_radio=split_string_to_radio)

@bp.route('/answer', methods=['POST'])
@login_required
def post_to_answer():
    Helper().check_not_admin()
    if request.method == 'POST':
        # result = True
        form_get = request.form
        correct_score = 0
        result = []
        for idx, data in enumerate(iterable=form_get):
                question_answer  = Question_user_answer(**{
                    "user_id": current_user.id,
                    "question_id": data,
                    "answer" : request.form[data]
                })
                # print(Helper().check_answer(data, request.form[data]))
                if(Helper().check_answer(data, request.form[data])):
                    correct_score = correct_score + 1
                
                result.append({
                         "question" : data,
                         'answer' : Helper().check_answer(data, request.form[data])
                    })

                db.session.add(question_answer)
            
        answer = User_results(
               no_question_answered=len(request.form),
               no_of_correct_answered=correct_score,
               user_id=current_user.id)
       
        db.session.add(answer)
        db.session.commit() 

        if session.get("questions") is not None:
          session.clear()       
          
        return render_template('exams/result.html', result=result)


