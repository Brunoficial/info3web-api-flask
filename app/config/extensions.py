from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def init_extensions(app):
    bcrypt.init_app(app)