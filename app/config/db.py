from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///info3web.db"
    db.init_app(app)

