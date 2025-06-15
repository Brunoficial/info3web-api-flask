from flask import request, Blueprint, jsonify
from ..models import Usuario
from ..config.db import db


authBP = Blueprint("auth", __name__, url_prefix="/auth")

@authBP.route("/login", methods=["POST"])
def login():
    matricula = request.get_json().get("matricula")
    senha = request.get_json().get("senha")

    usuarioLogado = db.session.query(Usuario).filter_by(matricula=matricula).first()

    if not usuarioLogado:
        return jsonify ({"error": "Usuário inexistente"}), 404

    if not usuarioLogado.senha == senha:
        return jsonify({"error": "Senha incorreta"}), 403

    return jsonify(usuarioLogado.to_dict())
    

@authBP.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    
    valid = Usuario.validateData(data)
    if valid == False:
        return jsonify({"error": "Preencha os campos"}), 400

    usuarioBancoEmail = db.session.query(Usuario).filter_by(email=data.get("email")).first()
    usuarioBancoMatricula = db.session.query(Usuario).filter_by(matricula=data.get("matricula")).first()
    
    if usuarioBancoMatricula or usuarioBancoEmail:
        return jsonify({"error": "Matrícula e/ou email já registrados"}), 409


    novoUsuario = Usuario(data)
    db.session.add(novoUsuario)
    db.session.commit()

    return jsonify({"message": "Usuário cadastrado"}), 200
