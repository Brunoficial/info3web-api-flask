from flask import jsonify, session
from ..models import Usuario
from ..repositories import UsuarioRepository
from flask_jwt_extended import create_access_token
from ..utils import *

def login(data: dict):
    try:
        matricula = data.get("matricula")
        senha = data.get("senha")

        usuarioLogado = UsuarioRepository.find_by_matricula(matricula)

        if not usuarioLogado:
            return jsonify ({"error": "Usuário inexistente"}), 404

        if not usuarioLogado.check_password(senha):
            return jsonify({"error": "Senha incorreta"}), 403

        session.clear()
        session['usuario_id'] = usuarioLogado.id
        
        return jsonify({"usuario": usuarioLogado.to_dict(), "token": create_access_token(identity=matricula)})
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao processar login: {e}"}), 500

def registro(data):
    try:
        if not validar_dados(data, Usuario.campos_obrigatorios()):
            return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

        usuario_banco_email = UsuarioRepository.find_by_email(data.get("email"))
        usuario_banco_matricula = UsuarioRepository.find_by_matricula(data.get("matricula"))
        
        if usuario_banco_matricula and usuario_banco_email:
            return jsonify({"detail": "Matrícula e email já registrados"}), 409

        if usuario_banco_matricula:
            return jsonify({"detail": "Matrícula já registrada"}), 409
        
        if usuario_banco_email:
            return jsonify({"detail": "Email já registrado"}), 409

        novoUsuario = Usuario(data)
        UsuarioRepository.save(novoUsuario)

        return jsonify({"detail": "Usuário cadastrado"}), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao processar registro: {e}"}), 500
        

    
