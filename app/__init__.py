from flask import Flask 
from .config.db import db, create_db  
from .routes import register_routes
from .config.extensions import init_extensions

def createApp() :
    app = Flask(__name__)
    init_extensions(app)
    register_routes(app)
    create_db(app)

    with app.app_context():
        from . import models
        db.create_all()


    return app 

