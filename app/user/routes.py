from flask import render_template, redirect, flash, current_app, request, url_for
from app.user import bp
from app.extensions import db
from app.models.user import User
from app.forms.user import UserCreationForm
from flask_login import login_required, current_user
from sqlalchemy import exc
from werkzeug.utils import secure_filename
import os
from app.helpers import Helper


@bp.route('/', methods=['POST','GET'])
@login_required
def index():
    Helper().check_admin()
    form = UserCreationForm()
    users = db.session.query(User).filter(
                        User.id != current_user.id,
                        User.is_admin == 0
                    ).limit(20).offset(0)
    if form.validate_on_submit():
        file = request.files['file']
        if file and Helper().allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                        current_app.root_path,
                        current_app.config['UPLOAD_FOLDER'],
                        filename
                    ))
            if Helper().do_bulk_user(filename):
                flash('You uploaded right file extension', 'success')
                return redirect(url_for('users.index'))
            else:
                flash('Something is wrong with your file', 'danger')
                return redirect(url_for('users.index'))
        else:
            flash('You uploaded wrong file extension', 'danger')
            return redirect(url_for('users.index'))
    return render_template('users/index.html', users=users, form=form)


# def keep():
#      filename = secure_filename(file.filename)
#            file.save(os.path.join(
#                         bp.config['UPLOAD_FOLDER'],
#                         filename
#                     ))
#            # do users on the database if return fine 
#            if do_bulk_user(filename):
#             flash('Successfully uploaded', 'success')