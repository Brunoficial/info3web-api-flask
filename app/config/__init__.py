from .bcyptConfig import config_bcrypt
from .jwtConfig import config_jwt
from .db import create_db

def init_configs(app):
  config_jwt(app)
  create_db(app)
  config_bcrypt(app)