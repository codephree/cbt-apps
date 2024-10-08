from flask_login import UserMixin
from datetime import datetime
from app.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
     # since the user_id is just the primary key of our user table, use it in the query for the user
     return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True),default=datetime.utcnow)
    
    
    def __repr__(self):
        return f'<User {self.firstname, self.email, self.lastname}>'

class User_results(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        no_question_answered = db.Column(db.Integer, nullable=True, default=0)
        no_of_correct_answered = db.Column(db.Integer, nullable=True, default=0)
        created_at = db.Column(db.DateTime(timezone=True),default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




# class User_question_answers(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     answer = db.Column(db.Integer, nullable=True)
#     created_at = db.Column(db.DateTime(timezone=True),default=datetime.utcnow)
