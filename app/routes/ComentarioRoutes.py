from flask import Blueprint, request
from ..services import ComentarioService
from flask_jwt_extended import jwt_required

comentarioBP = Blueprint("comentario", __name__, url_prefix="/comentario")

@comentarioBP.route("/listar/<int:post_id>", methods=["GET"])
@jwt_required()
def listar_comentarios(post_id):
   return ComentarioService.listar_comentarios(post_id)
    
@comentarioBP.route("/criar/<int:post_id>", methods=["POST"])
@jwt_required()
def criar_comentario(post_id):
    return ComentarioService.criar_comentario(post_id, request.get_json())

@comentarioBP.route("/deletar/<int:comentario_id>", methods=["DELETE"])
@jwt_required()
def deletar_comentario(comentario_id):
    return ComentarioService.deletar_comentario(comentario_id)

@comentarioBP.route("/editar/<int:comentario_id>", methods=['PATCH'])
@jwt_required()
def editar_comentario(comentario_id):
    return ComentarioService.editar_comentario(comentario_id, request.get_json())