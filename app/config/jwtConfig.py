import os
from flask_jwt_extended import JWTManager
from flask import jsonify
from datetime import timedelta

jwt = JWTManager()

def config_jwt(app):
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
    app.secret_key = os.getenv("APP_SECRET_KEY")
    jwt.init_app(app)

@jwt.unauthorized_loader
def custom_missing_token(err_msg):
    return jsonify({"detail": "Token de autenticação não enviado. (Ausente)"}), 401

@jwt.expired_token_loader
def custom_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"detail": "Token expirado"}), 401

@jwt.invalid_token_loader
def custom_invalid_token(err_msg):
    return jsonify({"detail": "Token inválido ou mal formatado"}), 401