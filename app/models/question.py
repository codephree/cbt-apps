from app.extensions import db
from datetime import datetime

question_user_answer = db.Table('user_question_answers', 
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('question_id',db.Integer, db.ForeignKey('question.id')),
            db.Column('answer',db.Integer, nullable=True),
            db.Column('created_at',db.DateTime(timezone=True),default=datetime.utcnow)
     )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)
    is_right = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return f'<Question {self.question, self.options, self.is_right}>'

class Question_user_answer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id=  db.Column(db.Integer, db.ForeignKey('user.id'))
        question_id =  db.Column(db.Integer, db.ForeignKey('question.id'))
        answer = db.Column(db.Integer, nullable=True)
        created_at =  db.Column(db.DateTime(timezone=True),default=datetime.utcnow)   
    
        def __repr__(self):
            return f'<Question {self.question_id, self.answer, self.user_id}>'