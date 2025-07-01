from ..config.db import db
from ..models.Comentario import Comentario
from ..models import Post
from ..repositories import comentarioRepository
from flask import jsonify, abort, request, Blueprint


comentarioBP = Blueprint("comentario", __name__, url_prefix="/comentario")

def validar_dados(data):
    valid = Comentario.validate_data(data)
    if valid == False:
        abort(400, description="Escreva alguma coisa no seu comentário" )

@comentarioBP.route("/listar/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="Esse post não existe mais")
    comentarios = [comentario.to_dict() for comentario in post.comentarios]
    if not comentarios:
        return ({"message": "Não existem comentários para esse post"}), 204

    return jsonify(comentarios), 200
    
@comentarioBP.route("/criar/<int:post_id>", methods=["POST"])
def criar_comentario(post_id):
    data = request.get_json()
    validar_dados(data)
    
    novo_comentario = Comentario(data)
    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="De alguma forma, você tentou fazer um comentário em um post que não existe mais")
    
    novo_comentario.post = post
    comentarioRepository.save(novo_comentario)
    return jsonify({"message": "Comentário criado com sucesso!"}), 200

@comentarioBP.route("/deletar/<int:post_id>/<int:comentario_id>", methods=["DELETE"])
def deletar_comentario(post_id, comentario_id):
    comentario = db.session.query(Comentario).filter_by(post_id=post_id, id=comentario_id).first()
    if not comentario:
        return jsonify({"error": "Comentário não encontrado"}), 404
    
    comentarioRepository.delete(comentario)
    return jsonify({"message":"Comentário deletado com sucesso!"}), 200

@comentarioBP.route("/editar/<int:post_id>/<int:comentario_id>", methods=['PATCH'])
def editar_comentario(post_id, comentario_id):
    data = request.get_json()
    validar_dados(data)

    comentario = db.session.query(Comentario).filter_by(post_id=post_id, id=comentario_id).first()
    if not comentario:
        return jsonify({"error": "Esse comentário não foi encontrado"}), 404
    
    campos = ['conteudo', 'autor_id']
    for campo in campos:
        valor_atualizado = data.get(campo)

        if valor_atualizado != getattr(comentario, campo):
            setattr(comentario, campo, valor_atualizado)

    comentarioRepository.save(comentario)
    return jsonify({"message": "Comentário editado com sucesso!"}), 200
    

    

    
    
