from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager =  LoginManager()
login_manager.login_view = 'auth.index'
login_manager.refresh_view  = 'auth.index'
login_manager.needs_refresh_message = (u"Session timedout, please re-login")
login_manager.needs_refresh_message_category = "info"
bcrypt = Bcrypt()


