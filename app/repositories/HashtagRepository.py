from ..config.db import db
from ..models import Hashtag

def processar_hashtags(hashtags_strings):
    hashtags_do_post = []

    for nome in hashtags_strings:
        hashtag_banco = find_by_nome(nome)

        if not hashtag_banco:
            hashtag_banco = Hashtag(nome=nome) # Transforma a string hashtag em um objeto
            save(hashtag_banco)
            
        hashtags_do_post.append(hashtag_banco)

    return hashtags_do_post

def find_by_nome(nome:str):
    if not nome.startswith("#"):
        nome = "#" + nome
    hashtag = db.session.query(Hashtag).filter_by(nome=nome).first()
    
    return hashtag

def save(hashtag):
    db.session.add(hashtag)
    db.session.commit()