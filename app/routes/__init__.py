from .auth import authBP

def register_routes(app):
    app.register_blueprint(authBP)