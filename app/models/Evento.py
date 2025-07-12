from ..config.db import db
from datetime import datetime

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(1000), nullable=True)
    data_evento =  db.Column(db.String(12), nullable=False)
    data_postagem = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, data):
        self.nome = data.get("nome")
        self.descricao = data.get("descricao")
        self.data_evento = data.get("data_evento")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_evento": self.data_evento,
            "data_postagem": self.data_postagem
        }
    
    @staticmethod
    def campos_obrigatorios():
        return ["nome", "data_evento"]

    @staticmethod
    def campos_editaveis():
        return ["nome", "descricao", "data_evento"]