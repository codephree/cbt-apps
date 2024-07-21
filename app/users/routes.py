from flask import render_template
from app.users import bp
from app.extensions import db
# from app.models.post import Post
from app.forms.user import UserLogin, UserSignUp

@bp.route('/')
def index():
    # posts = Post.query.all()
    return render_template('users/index.html')

@bp.route('/login')
def login():
    # posts = Post.query.all()
    form = UserLogin()
    return render_template('users/login.html', form=form)


@bp.route('/signup/')
def signUp():
    form = UserSignUp()
    return render_template('users/signup.html', form=form)
