from flask import render_template, redirect, flash
from app.user import bp
from app.extensions import db
from app.models.user import User
from flask_login import login_required
from sqlalchemy import exc


@bp.route('/', methods=['POST','GET'])
@login_required
def index():
    return render_template('users/index.html')