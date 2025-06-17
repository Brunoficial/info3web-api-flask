from .auth import authBP
from .post import postBP

def register_routes(app):
    app.register_blueprint(authBP)
    app.register_blueprint(postBP)