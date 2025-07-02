from ..models import Post
from flask import request, Blueprint, jsonify
from ..repositories import postRepository
from ..repositories import hashtagRepository
from flask_jwt_extended import jwt_required
from ..utils import *

postBP = Blueprint("post", __name__, url_prefix="/post")

# Rotas
@postBP.route("/listar", methods=["GET"])
# @jwt_required()
def listar_posts():
    posts_do_banco = postRepository.list_posts()

    posts = serializar_itens(posts_do_banco)
    if not posts:
        return ({"error": "Nenhum post encontrado"}), 404
    
    return jsonify(posts), 200


@postBP.route("/listar_por_hashtag/<string:hashtag>", methods=["GET"])
def listar_por_hashtag(hashtag):
    posts_do_banco = postRepository.find_by_hashtag(hashtag)

    posts = serializar_itens(posts_do_banco)
    if not posts:
        return ({"error": "Nenhum post encontrado"}), 404
    
    return jsonify(posts), 200


@postBP.route("/criar", methods=["POST"])
# @jwt_required()
def criar_post():
    data = request.get_json()
    valid = validar_dados(data, ["titulo", "conteudo", "autor_id"])
    if valid == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

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
    valid = validar_dados(data, ["titulo", "conteudo", "autor_id"])
    if valid == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    editar_dados(["titulo", "conteudo", "autor_id"], data, post)

    # Não dá pra colocar essa parte também dentro da função save?
    hashtags_strings = data.get("hashtags")
    hashtags_entidades = hashtagRepository.save(hashtags_strings)

    if hashtags_entidades:
        setattr(post, "hashtags", hashtags_entidades) # Acho que também dava pra fazer post.hashtags = hashtags_entidades
    
    postRepository.save(post)

    return jsonify({"message": "Post atualizado com sucesso!!!"}), 200

'''
Coisas que eu acho que dá pra mudar nessa função de hashtags 
A função save() do hashtagsRepository está fazendo mais do que ela deveia. Ela deveria ter o estrito 
propósito de salvar as hashtags no banco. Ela está também atribuindo aos posts, e tá ficando um pouco
confuso. 
Ideia: Separar em duas funções, save() e atualizar_hashtags(). E aquela parte de hashtags_strings e
hashtag_entidades estariam dentro dessa função -> save(hashtags_strings), atualizar_hashtags(data, hashtags_strings)
'''