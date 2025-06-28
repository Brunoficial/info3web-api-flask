from ..config.db import db
from ..models import Hashtag

def save(hashtags):
    hashtags_do_post = []
    for hashtag in hashtags:
        hashtag_banco = db.session.query(Hashtag).filter_by(nome=hashtag).first()
        if not hashtag_banco:
            hashtag_banco = Hashtag(nome=hashtag)
            db.session.add(hashtag_banco)
            db.session.commit()
        
        hashtags_do_post.append(hashtag_banco)
    return hashtags_do_post

def find_by_nome(nome):
    nome = "#" + nome
    hashtag = db.session.query(Hashtag).filter_by(nome=nome).first()
    return hashtag


        