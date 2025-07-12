from ..config.db import db 
from datetime import date, datetime
from flask import jsonify

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=False)
    conteudo = db.Column(db.String(1000), nullable=False)
    data = db.Column (db.DateTime, nullable=False, default=datetime.now())
    autor_id = db.Column(db.ForeignKey("usuarios.id"), nullable=False)
    curtidas = db.Column(db.Integer, default=0)
    hashtags = db.relationship('Hashtag', secondary='posts_hashtags', backref='posts', lazy='select')
    comentarios = db.relationship('Comentario', backref='post', cascade='all, delete', lazy='select')
    

    def __init__(self, data):
        self.titulo = data.get("titulo") 
        self.conteudo = data.get("conteudo") 
        self.autor_id = data.get("autor_id")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "conteudo": self.conteudo,
            "data": self.data, 
            "autor_id": self.autor_id,
            "hashtags": self.get_hashtags(),
            "curtidas": self.curtidas
        }
    
    def get_hashtags(self):
        return [hashtag.nome for hashtag in self.hashtags]
    
    def get_comentarios(self):
        return [comentario.to_dict() for comentario in self.comentarios]

    @staticmethod
    def campos_obrigatorios():
        return ["titulo", "conteudo", "autor_id"]
    
    @staticmethod
    def campos_editaveis():
        return ["titulo", "conteudo"]



        
        