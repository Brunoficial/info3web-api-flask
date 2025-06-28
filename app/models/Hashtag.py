from ..config.db import db

class Hashtag(db.Model):
    __tablename__ = 'hashtags'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }
    
    @staticmethod
    def validate_data(data):
        campos = ["nome"]
        for campo in campos:
            if not data.get(campo):
                return False
