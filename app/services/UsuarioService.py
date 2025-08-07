from ..repositories import UsuarioRepository
from ..utils import *
from flask import jsonify

def listar_usuarios():
    try:
        usuarios_do_banco = UsuarioRepository.list_usuarios()
        usuarios = serializar_itens(usuarios_do_banco)
        if not usuarios:
            return jsonify({"detail": "Nenhum usuário encontrado"}), 204
        
        return jsonify(usuarios), 200
    
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao listar posts: {e}"}), 500

def listar_usuario_por_id(id):
    try: 
        usuario_do_banco = UsuarioRepository.find_by_id(id)
        usuario = usuario_do_banco.to_dict()
        if not usuario:
            return jsonify({"detail": "Usuário não encontrado"}), 404
        
        return usuario
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao procurar usuário: {e}"}), 500

