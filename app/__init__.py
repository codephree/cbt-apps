from flask import Flask, render_template
from config import Config
from app.extensions import db,login_manager,bcrypt
# from app.auth import auth

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

  
    # Initialize Flask extensions here
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/login')

    from app.user import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.question import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    from app.exams import bp as exams_bp
    app.register_blueprint(exams_bp, url_prefix='/exams')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    


    return app
