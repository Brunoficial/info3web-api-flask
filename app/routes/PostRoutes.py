from flask import request, Blueprint
from ..services import PostService
from flask_jwt_extended import jwt_required

postBP = Blueprint("post", __name__, url_prefix="/post")

@postBP.route("/listar", methods=["GET"])
@jwt_required()
def listar_posts():
    return PostService.listar_posts()

@postBP.route("/listar_por_hashtag/<string:hashtag>", methods=["GET"])
def listar_por_hashtag(hashtag):
    return PostService.listar_por_hashtag(hashtag)

@postBP.route("/criar", methods=["POST"])
@jwt_required()
def criar_post():
    return PostService.criar_post(request.get_json())

@postBP.route("/deletar/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar_post(id):
    return PostService.deletar_post(id)

@postBP.route("/editar/<int:id>", methods=["PATCH"])
@jwt_required()
def editar_post(id):
    return PostService.editar_post(id, request.get_json())

