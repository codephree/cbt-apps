from flask import render_template, redirect, flash, request, abort
from app.auth import bp
from app.extensions import db, login_manager, bcrypt
from app.models.user import User
from app.forms.auth import loginForm
from flask_login import login_user, login_required, logout_user
from sqlalchemy import exc
from datetime import timedelta

@bp.route('/', methods=['POST','GET'])
def index():
    form = loginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()

            if user is None:
                flash("Email address not found in our system", "danger")
                return render_template('auth/login.html', form=form) 
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, duration=timedelta(minutes=3))
               
                flash("You are now logged in successfully.", "success")
                
                next = request.args.get('next')
                return redirect(next or '/')
            else:
                flash("Invalid credential please try again", "danger")
                return render_template('auth/login.html', form=form) 
        except exc.OperationalError as error:
               flash("An error occurred", "danger")
               return render_template('auth/login.html', form=form) 
   
    return render_template('auth/login.html', form=form)

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    # flash('You have logged out successfully', 'success')
    return redirect('/')
