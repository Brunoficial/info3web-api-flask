from flask import jsonify, request, Blueprint
from ..services import ComentarioService

comentarioBP = Blueprint("comentario", __name__, url_prefix="/comentario")

@comentarioBP.route("/listar/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
   comentarios = ComentarioService.listar_comentarios(post_id)
   return comentarios
    
@comentarioBP.route("/criar/<int:post_id>", methods=["POST"])
def criar_comentario(post_id):
    post = postRepository.find_by_id(post_id)
    if not post:
       return jsonify({"error": "Post não encontrado"}), 404
    
    data = request.get_json()
    if validar_dados(data, Comentario.campos_obrigatorios()) == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400
    novo_comentario = Comentario(data)

    novo_comentario.post = post
    comentarioRepository.save(novo_comentario)
    return jsonify({"message": "Comentário criado com sucesso!"}), 200


@comentarioBP.route("/deletar/<int:comentario_id>", methods=["DELETE"])
def deletar_comentario(comentario_id):
    comentario = comentarioRepository.find_by_id(comentario_id)
    if not comentario:
        return jsonify({"error": "Comentário não encontrado"}), 404
    
    comentarioRepository.delete(comentario)
    return jsonify({"message":"Comentário deletado com sucesso!"}), 200


@comentarioBP.route("/editar/<int:comentario_id>", methods=['PATCH'])
def editar_comentario(comentario_id):
    comentario = comentarioRepository.find_by_id(comentario_id)
    if not comentario:
        return jsonify({"error": "Esse comentário não foi encontrado"}), 404
    
    data = request.get_json() 
    if validar_dados(data, Comentario.campos_obrigatorios()) == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    if editar_dados(Comentario.campos_editaveis(), data, comentario): 
        comentarioRepository.save(comentario)
        return jsonify({"message": "Comentário editado com sucesso!"}), 200
    
    return jsonify({'message': 'Comentário não foi alterado'}), 200
    

    

    
    
