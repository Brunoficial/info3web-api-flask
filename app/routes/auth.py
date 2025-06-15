from flask import request, Blueprint, jsonify
from ..models import Usuario
from ..repositories import usuarioRepository
from flask_jwt_extended import create_access_token

authBP = Blueprint("auth", __name__, url_prefix="/auth")

@authBP.route("/login", methods=["POST"])
def login():
    matricula = request.get_json().get("matricula")
    senha = request.get_json().get("senha")

    usuarioLogado = usuarioRepository.find_by_matricula(matricula)

    if not usuarioLogado:
        return jsonify ({"error": "Usuário inexistente"}), 404

    if not usuarioLogado.check_password(senha):
        return jsonify({"error": "Senha incorreta"}), 403

    return jsonify({"usuario": usuarioLogado.to_dict(), "token": create_access_token(identity=matricula)})
    

@authBP.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    
    valid = Usuario.validateData(data)
    if valid == False:
        return jsonify({"error": "Preencha os campos"}), 400

    usuarioBancoEmail = usuarioRepository.find_by_email(data.get("email"))
    usuarioBancoMatricula = usuarioRepository.find_by_matricula(data.get("matricula"))
    
    if usuarioBancoMatricula or usuarioBancoEmail:
        return jsonify({"error": "Matrícula e/ou email já registrados"}), 409


    novoUsuario = Usuario(data)
    usuarioRepository.save(novoUsuario)

    return jsonify({"message": "Usuário cadastrado"}), 200
