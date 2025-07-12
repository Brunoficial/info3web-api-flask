from ..models import Comentario
from ..repositories import ComentarioRepository, PostRepository
from ..utils import *
from flask import jsonify

def listar_comentarios(post_id):
    try:
        post = PostRepository.find_by_id(post_id)
        if not post:
            return jsonify({"detail": "O post que você está tentando visualizar os comentários não existe ou foi excluído"}), 404
        
        comentarios = serializar_itens(post.comentarios)
        if not comentarios:
            return jsonify(""), 204

        return jsonify(comentarios), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao listar comentários: {e}"}), 500

def criar_comentario(post_id, data):
    try:
        post = PostRepository.find_by_id(post_id)
        if not post:
            return jsonify({"detail": "O post que você está tentando comentar não existe ou foi excluído"}), 404
        
        if validar_dados(data, Comentario.campos_obrigatorios()) == False:
            return jsonify({"detail": "Preencha os campos obrigatórios"}), 400
        novo_comentario = Comentario(data)

        novo_comentario.post = post
        ComentarioRepository.save(novo_comentario)
        return jsonify({"detail": "Comentário criado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao criar comentário: {e}"}), 500

def deletar_comentario(comentario_id):
    try:
        comentario = ComentarioRepository.find_by_id(comentario_id)
        if not comentario:
            return jsonify({"detail": "Comentário não encontrado"}), 404
        
        ComentarioRepository.delete(comentario)
        return jsonify({"detail":"Comentário deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao deletar comentário: {e}"}), 500

def editar_comentario(comentario_id, data):
    try:
        comentario = ComentarioRepository.find_by_id(comentario_id)
        if not comentario:
            return jsonify({"detail": "Esse comentário não foi encontrado"}), 404
        
        if validar_dados(data, Comentario.campos_obrigatorios()) == False:
            return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

        if editar_dados(Comentario.campos_editaveis(), data, comentario): 
            ComentarioRepository.save(comentario)
            return jsonify({"detail": "Comentário editado com sucesso!"}), 200
        
        return jsonify({'detail': 'Comentário não foi alterado'}), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao editar comentário: {e}"}), 500