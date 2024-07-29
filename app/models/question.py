from app.extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)
    is_right = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Question {self.question, self.options}>'
