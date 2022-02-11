from mimetypes import init
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
BASEDIR = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisaverysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
        
    from .models import Users
    
    init_db(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(id)
    
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

def init_db(app):
    if not os.path.lexists(os.path.join(BASEDIR, '\movies.db')):
        db.create_all(app=app)