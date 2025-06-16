from ..config.db import db 
from ..models.Post import Post

def find_by_autor(autor_id):
    posts = db.session.query(Post).filter_by(autor_id=autor_id).all()
    return posts

def find_by_titulo(titulo):
    posts = db.session.query(Post).filter_by(titulo=titulo).all()
    return posts

def find_by_data(data):
    posts = db.session.query(Post).filter_by(data=data).all()
    return posts

def save_post(post):
    db.session.add(post)
    db.session.commit()
