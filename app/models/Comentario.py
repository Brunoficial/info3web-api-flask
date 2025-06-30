from ..config.db import db
from flask import datetime

class Comentario(db.Model):
    __tablename__ = "comentarios"

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(1000), nullable=False)
    curtidas = db.Column(db.Integer, default=0)
    autor_id = db.Column(db.ForeignKey("usuarios.id"), nullable=False)
    post_id = db.Column(db.ForeignKey("posts.id"), nullable=False)
    data = db.Column(db.Datetime, nullable=False, default=datetime.now())

    def __init__(self, data):
        self.conteudo = data.get("conteudo")
        self.autor_id = data.get("autor_id")
        self.post_id = data.get("post_id")
        self.data = data.get("data")

    def to_dict(self):
        return {
            "conteudo": self.conteudo,
            "autor_id": self.autor_id,
            "post_id": self.post_id
        }
    
    @staticmethod
    def validate_data(data):
        campos = ["conteudo", "autor_id", "post_id"]
        for campo in campos:
            if not data.get(campo):
                return False
    