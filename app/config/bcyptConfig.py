from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def config_bcrypt(app):
    bcrypt.init_app(app)