from flask import Blueprint, request
from ..services import ComentarioService

comentarioBP = Blueprint("comentario", __name__, url_prefix="/comentario")

@comentarioBP.route("/listar/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
   return ComentarioService.listar_comentarios(post_id)
    
@comentarioBP.route("/criar/<int:post_id>", methods=["POST"])
def criar_comentario(post_id):
    return ComentarioService.criar_comentario(post_id, request.get_json())

@comentarioBP.route("/deletar/<int:comentario_id>", methods=["DELETE"])
def deletar_comentario(comentario_id):
    return ComentarioService.deletar_comentario(comentario_id)

@comentarioBP.route("/editar/<int:comentario_id>", methods=['PATCH'])
def editar_comentario(comentario_id):
    return ComentarioService.editar_comentario(comentario_id, request.get_json())