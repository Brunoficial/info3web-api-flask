from ..config.db import db
from ..models import Comentario

def save(comentario):
    db.session.add(comentario)
    db.session.commit()

def delete(comentario):
    db.session.delete(comentario)
    db.session.commit()