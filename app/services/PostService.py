from ..models import Post
from flask import jsonify
from ..repositories import PostRepository, HashtagRepository
from ..utils import *

def listar_posts():
    try:
        posts_do_banco = PostRepository.list_posts()

        posts = serializar_itens(posts_do_banco)
        if not posts:
            return jsonify({"detail": "Nenhum post encontrado"}), 204
        
        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao listar posts: {e}"}), 500

def listar_por_hashtag(hashtag):
    try:
      posts_do_banco = PostRepository.find_by_hashtag(hashtag)

      posts = serializar_itens(posts_do_banco)
      if not posts:
          return jsonify({"detail": "Nenhum post encontrado"}), 404
      
      return jsonify(posts), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao listar posts por hashtag: {e}"}), 500

def criar_post(data):
    try:
      if not validar_dados(data, Post.campos_obrigatorios()):
        return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

      novoPost = Post(data)
      lidar_com_hashtags(data.get("hashtags"), novoPost)
      
      PostRepository.save(novoPost)
      return jsonify({"detail":"Post criado com sucesso!"}), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao criar post: {e}"}), 500
 
def deletar_post(id):
    try:
      post = PostRepository.find_by_id(id)
      usuario_logado = get_usuario_logado()

      if not post:
          return jsonify({"detail": "Nenhum post encontrado"}), 404

      if post.autor_id != usuario_logado:
          return jsonify({"detail": "Você não tem permissão para deletar o post de outra pessoa"}), 403
      
      PostRepository.delete(post)
      return jsonify({"detail": "Post deletado com sucesso"}), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao deletar post: {e}"}), 500
 
def editar_post(id, data):
    try:
      post = PostRepository.find_by_id(id)
      usuario_logado = get_usuario_logado()

      if not post:
          return jsonify({"detail": "Nenhum post encontrado"}), 404
      
      if post.autor_id != usuario_logado:
          return jsonify({"detail": "Você não tem permissão para editar o post de outra pessoa"}), 403

      if not validar_dados(data, Post.campos_obrigatorios()):
          return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

      editar_dados(Post.campos_editaveis(), data, post)
      lidar_com_hashtags(data.get("hashtags"), post)

      PostRepository.save(post)
      return jsonify({"detail": "Post atualizado com sucesso"}), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao atualizar post: {e}"}), 500

def lidar_com_hashtags(hashtags_strings, post):
    hashtags_entidades = HashtagRepository.processar_hashtags(hashtags_strings)

    if hashtags_entidades:
        post.hashtags = hashtags_entidades