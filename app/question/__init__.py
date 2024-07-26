from flask import Blueprint

bp = Blueprint('questions', __name__)


from app.question import routes
