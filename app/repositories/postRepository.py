from ..config.db import db 
from ..models.Post import Post
from ..models.Hashtag import Hashtag

def list_posts():
    posts = db.session.query(Post).all()
    return posts

def find_by_id(id):
    post = db.session.query(Post).filter_by(id=id).first()
    return post

def find_by_autor(autor_id):
    posts = db.session.query(Post).filter_by(autor_id=autor_id).all()
    return posts

def find_by_hashtag(hashtag):
    hashtag = "#" + hashtag
    posts = db.session.query(Post).filter(Post.hashtags.any(Hashtag.nome == hashtag)).all()
    return posts

def save(post):
    db.session.add(post)
    db.session.commit()

def delete(post):
    db.session.delete(post)
    db.session.commit()

