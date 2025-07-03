from ..config.db import db
from ..models import Comentario

def find_by_id(id):
    comentario = db.session.query(Comentario).filter_by(id=id).first()
    return comentario

def save(comentario):
    db.session.add(comentario)
    db.session.commit()

def delete(comentario):
    db.session.delete(comentario)
    db.session.commit()