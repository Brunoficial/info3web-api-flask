from flask import Flask 
from .config.db import db, create_db  

def createApp() :
    app = Flask(__name__)
    create_db(app)

    with app.app_context():
        from . import models
        db.create_all()


    return app 

