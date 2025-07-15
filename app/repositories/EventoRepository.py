from ..models.Evento import Evento
from ..config.db import db

def listar_eventos():
    eventos = db.session.query(Evento).all()
    return eventos

def find_by_id(id):
    evento = db.session.query(Evento).filter_by(id=id).first()
    return evento

def save(evento):
    db.session.add(evento)
    db.session.commit()


def delete(post):
    db.session.delete(post)
    db.session.commit()