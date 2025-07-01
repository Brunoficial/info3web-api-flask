from ..config.db import db
from ..models.Comentario import Comentario
from ..models import Post
from ..repositories import comentarioRepository
from ..utils import *
from flask import jsonify, request, Blueprint


comentarioBP = Blueprint("comentario", __name__, url_prefix="/comentario")

@comentarioBP.route("/listar/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
        return jsonify({"error": "Post não encontrado"}), 404
    
    # comentarios = [comentario.to_dict() for comentario in post.comentarios]
    comentarios = serializar_itens(post.comentarios)
    if not comentarios:
        return jsonify({"message": "Não existem comentários para esse post"}), 200

    return jsonify(comentarios), 200
    
@comentarioBP.route("/criar/<int:post_id>", methods=["POST"])
def criar_comentario(post_id):
    data = request.get_json()
    validar_dados(data, ['conteudo', 'autor_id'])
    
    novo_comentario = Comentario(data)

    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
       return jsonify({"error": "Post não encontrado"}), 404
    
    novo_comentario.post = post
    comentarioRepository.save(novo_comentario)
    return jsonify({"message": "Comentário criado com sucesso!"}), 200


@comentarioBP.route("/deletar/<int:comentario_id>", methods=["DELETE"])
def deletar_comentario(comentario_id):
    comentario = db.session.query(Comentario).filter_by(id=comentario_id).first()
    if not comentario:
        return jsonify({"error": "Comentário não encontrado"}), 404
    
    comentarioRepository.delete(comentario)
    return jsonify({"message":"Comentário deletado com sucesso!"}), 200


@comentarioBP.route("/editar/<int:comentario_id>", methods=['PATCH'])
def editar_comentario(comentario_id):
    data = request.get_json()
    valid = validar_dados(data, ['conteudo', 'autor_id'])
    if valid == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    comentario = db.session.query(Comentario).filter_by(id=comentario_id).first()
    if not comentario:
        return jsonify({"error": "Esse comentário não foi encontrado"}), 404
    
    alterado = editar_dados(['conteudo', 'autor_id'], data, comentario) # Substitui aquelas linhas todas
    if alterado: 
        comentarioRepository.save(comentario)
        return jsonify({"message": "Comentário editado com sucesso!"}), 200
    
    return jsonify({'message': 'Comentário não foi alterado'}), 200
    

    

    
    
