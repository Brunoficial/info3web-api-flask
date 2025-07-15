from ..config.db import db
from ..models import Usuario

def list_usuarios():
    usuarios = db.session.query(Usuario).all()
    return usuarios

def find_by_id(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario 

def find_by_email(email):
    usuario = db.session.query(Usuario).filter_by(email=email).first()
    return usuario 

def find_by_matricula(matricula):
    usuario = db.session.query(Usuario).filter_by(matricula=matricula).first()
    return usuario 

def save(usuario):
    db.session.add(usuario)
    db.session.commit()