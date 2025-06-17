from ..models import Post
from flask import request, Blueprint, jsonify
from ..repositories import postRepository

postBP = Blueprint("post", __name__, url_prefix="/post")

@postBP.route("/listar", methods=["GET"])
def listar_posts():
    posts_banco = postRepository.list_posts()

    if not posts_banco:
        return jsonify ({"error": "Nenhum post encontrado"}), 404
    
    posts = []
    for post in posts_banco:
        posts.append(post.to_dict())

    return jsonify(posts), 200

@postBP.route("/criar", methods=["POST"])
def criar_post():
    data = request.get_json()

    valid = Post.validate_data(data)
    if valid == False:
        return ({"error": "Preencha os campos"}), 400

    novoPost = Post(data)
    postRepository.save(novoPost)

    return jsonify({"message":"Post criado com sucesso!"}), 200

@postBP.route("/deletar/<int:id>", methods=["DELETE"])
def deletar_post(id):
    post = postRepository.find_by_id(id)

    if not post:
        return jsonify ({"error": "Nenhum post encontrado"}), 404

    postRepository.delete(post)
    return ({"message": "Post deletado com sucesso!!!"}), 200

@postBP.route("/atualizar/<int:id>", methods=["PATCH"])
def atualizar_post(id):
    post = postRepository.find_by_id(id)
    data = request.get_json()

    if not post:
        return jsonify ({"error": "Nenhum post encontrado"}), 404

    campos = ["titulo", "conteudo"]
    for campo in campos:
        if data.get(campo) != post.__getattribute__(campo):
            post.__setattr__(campo, data.get(campo))
    
    postRepository.save(post)

    return jsonify({"message": "Post atualizado com sucesso!!!"}), 200