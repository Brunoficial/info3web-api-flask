from ..models import Post
from flask import request, Blueprint, jsonify
from ..repositories import postRepository
from ..repositories import hashtagRepository
from flask_jwt_extended import jwt_required
from flask import abort

postBP = Blueprint("post", __name__, url_prefix="/post")


# Funções auxiliares
def serializar_posts(posts_do_banco):
    return [post.to_dict() for post in posts_do_banco]

def validar_dados(data):
    valid = Post.validate_data(data)
    if valid == False:
        abort(400, description="Preencha os campos obrigatórios")

# Rotas
@postBP.route("/listar", methods=["GET"])
# @jwt_required()
def listar_posts():
    posts_do_banco = postRepository.list_posts()

    posts = serializar_posts(posts_do_banco)
    if not posts:
        return ({"error": "Nenhum post encontrado"}), 404
    
    return jsonify(posts), 200


@postBP.route("/listar_por_hashtag/<string:hashtag>", methods=["GET"])
def listar_por_hashtag(hashtag):
    posts_do_banco = postRepository.find_by_hashtag(hashtag)

    posts = serializar_posts(posts_do_banco)
    if not posts:
        return ({"error": "Nenhum post encontrado"}), 404
    
    return jsonify(posts), 200


@postBP.route("/criar", methods=["POST"])
# @jwt_required()
def criar_post():
    data = request.get_json()
    validar_dados(data)

    novoPost = Post(data)

    hashtags = data.get("hashtags")
    if hashtags:
        novoPost.hashtags = hashtagRepository.save(hashtags)

    postRepository.save(novoPost)

    return jsonify({"message":"Post criado com sucesso!"}), 200


@postBP.route("/deletar/<int:id>", methods=["DELETE"])
# @jwt_required()
def deletar_post(id):
    post = postRepository.find_by_id(id)
    if not post:
        return jsonify ({"error": "Nenhum post encontrado"}), 404

    postRepository.delete(post)
    return ({"message": "Post deletado com sucesso!!!"}), 200


@postBP.route("/atualizar/<int:id>", methods=["PATCH"])
# @jwt_required()
def atualizar_post(id):
    post = postRepository.find_by_id(id)
    if not post:
        return jsonify ({"error": "Nenhum post encontrado"}), 404
    
    data = request.get_json()
    validar_dados(data)

    campos = ["titulo", "conteudo"]
    for campo in campos:
        valor_atualizado = data.get(campo)

        if valor_atualizado != getattr(post, campo):
            setattr(post, campo, valor_atualizado)

    hashtags = data.get("hashtags")
    hashtags_atualizadas = hashtagRepository.save(hashtags)

    if hashtags_atualizadas:
        setattr(post, "hashtags", hashtags_atualizadas)
    
    postRepository.save(post)

    return jsonify({"message": "Post atualizado com sucesso!!!"}), 200