from flask import request, Blueprint, jsonify, abort, session
from ..models import Usuario
from ..repositories import usuarioRepository
from flask_jwt_extended import create_access_token
from ..utils import *

authBP = Blueprint("auth", __name__, url_prefix="/auth")

@authBP.route("/login", methods=["POST"])
def login():
    matricula = request.get_json().get("matricula")
    usuarioLogado = usuarioRepository.find_by_matricula(matricula)

    if not usuarioLogado:
        return jsonify ({"error": "Usuário inexistente"}), 404

    senha = request.get_json().get("senha")

    if not usuarioLogado.check_password(senha):
        return jsonify({"error": "Senha incorreta"}), 403

    session.clear()
    session['usuario_id'] = usuarioLogado.id
    
    return jsonify({"usuario": usuarioLogado.to_dict(), "token": create_access_token(identity=matricula)})
    


@authBP.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()

    if validar_dados(data, Usuario.campos_obrigatorios()) == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    usuario_banco_email = usuarioRepository.find_by_email(data.get("email"))
    usuario_banco_matricula = usuarioRepository.find_by_matricula(data.get("matricula"))
    
    if usuario_banco_matricula and usuario_banco_email:
        return jsonify({"error": "Matrícula e email já registrados"}), 409

    if usuario_banco_matricula:
        return jsonify({"error": "Matrícula já registrada"}), 409
    
    if usuario_banco_email:
        return jsonify({"error": "Email já registrado"}), 409

    novoUsuario = Usuario(data)
    usuarioRepository.save(novoUsuario)

    return jsonify({"message": "Usuário cadastrado"}), 200
