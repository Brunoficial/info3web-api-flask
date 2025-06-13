from ..config.db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(60), nullable=False)
    matricula = db.Column(db.String(14), nullable=False)

    def __init__(self, nome, email, senha, matricula):
        self.nome = nome
        self.email = email 
        self.senha = senha 
        self.matricula = matricula 


    

