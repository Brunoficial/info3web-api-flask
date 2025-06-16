from ..config.db import db 
from datetime import date

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=False)
    conteudo = db.Column(db.String(1000), nullable=False)
    data = db.Column (db.Date, nullable=False, default=date.today)
    autor_id = db.Column(db.ForeignKey("usuarios.id"), nullable=False)

    def __init__(self, titulo, conteudo, data, autor_id):
        self.titulo = titulo 
        self.conteudo = conteudo 
        self.data = data 
        self.autor_id = autor_id

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "conteudo": self.conteudo,
            "data": self.data, 
            "autor_id": self.autor_id
        }
        