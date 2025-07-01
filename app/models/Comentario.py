from ..config.db import db
from datetime import datetime

class Comentario(db.Model):
    __tablename__ = "comentarios"

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(1000), nullable=False)
    curtidas = db.Column(db.Integer, default=0)
    autor_id = db.Column(db.ForeignKey("usuarios.id"), nullable=False)
    post_id = db.Column(db.ForeignKey("posts.id"), nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, data):
        self.conteudo = data.get("conteudo")
        self.autor_id = data.get("autor_id")
        self.data = data.get("data")

    def to_dict(self):
        return {
            "id": self.id,
            "conteudo": self.conteudo,
            "autor_id": self.autor_id,
            "post_id": self.post_id
        }
    