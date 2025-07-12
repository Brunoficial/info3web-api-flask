from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from datetime import timedelta

bcrypt = Bcrypt()
jwt = JWTManager()

def init_extensions(app):
    bcrypt.init_app(app)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
    app.secret_key = os.getenv("APP_SECRET_KEY")
    jwt.init_app(app)