from os import path

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from src.import_db.create_db import create_engine
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "AppData"


def create_app():

    app = Flask(__name__)
    create_engine(app)


    from flask_login import LoginManager
    from src.after_login.after_login_routes import views
    from src.after_login.lectures import lectures
    from src.after_login.tests import tests
    from src.auth.authentification import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(lectures, url_prefix='/')
    app.register_blueprint(tests, url_prefix='/')

    from src.import_db.tables import User

    create_tables(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_tables(app):
    if not path.exists('website/' + DB_NAME):
        print('table was created! ')
        db.create_all(app=app)  # create all tables