from flask import render_template, redirect, flash, abort, request, current_app, url_for
from app.question import bp
from app.extensions import db
from app.models.question import Question
from app.forms.question import QuestionCreationForm
from flask_login import login_required
from sqlalchemy import exc
from app.helpers import Helper
from werkzeug.utils import secure_filename
import os
from app.helpers import Helper


@bp.route('/', methods=['POST','GET'])
@login_required
def index():
    Helper().check_admin()
    question = Question.query.all()
    form = QuestionCreationForm()
    if form.validate_on_submit():
        file = request.files['file']
        if file and Helper().allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                        current_app.root_path,
                        current_app.config['UPLOAD_FOLDER'],
                        filename
                    ))
            if Helper().do_bulk_question(filename):
                flash('Question uploaded right file extension', 'success')
                return redirect(url_for('questions.index'))
            else:
                flash('Something is wrong with your file', 'danger')
                return redirect(url_for('questions.index'))
        else:
            flash('You uploaded wrong file extension', 'danger')
            return redirect(url_for('questions.index'))
    return render_template('questions/index.html', questions=question, form=form)

