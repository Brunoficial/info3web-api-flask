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
        return "Usuário inexistente"

    if not usuarioLogado.senha == senha:
        return "Senha incorreta"

    return jsonify(usuarioLogado.to_dict())
    

@authBP.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()

    valid = Usuario.validateData(data)
    if valid == False:
        return "Preencha os campos"

    novoUsuario = Usuario(data)
    db.session.add(novoUsuario)
    db.session.commit()

    return "Usuário cadastrado"
