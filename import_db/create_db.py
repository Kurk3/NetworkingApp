from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "AppData"


def create_engine(app):
    app.config['SECRET_KEY'] = 'abcdefghfijklmnoprsqxyz'  # ked stranka ide do produkcie (heslo)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'
    db.init_app(app)