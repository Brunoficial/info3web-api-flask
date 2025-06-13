from flask import Flask 
from .config.db import create_db, db 

def createApp() :
    app = Flask(__name__)
    create_db(app)

    with app.app_context():
        db.create_all()

    return app 



