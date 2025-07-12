import os
from flask import Flask 
from .config.db import db
from .routes import register_routes
from dotenv import load_dotenv
from .config import init_configs

load_dotenv()

def createApp() :
    app = Flask(__name__)
    init_configs(app)
    register_routes(app)

    app.secret_key = os.getenv("APP_SECRET_KEY")

    with app.app_context():
        from . import models
        db.create_all()


    return app 

