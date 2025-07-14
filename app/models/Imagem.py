from ..config.db import db
from flask import url_for

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(db.LargeBinary)
    post_id = db.Column(db.ForeignKey("posts.id"), nullable=False)

    def __init__(self, imagem):
        self.imagem = imagem

    def to_dict(self):
        return url_for("imagem", id=self.id, _external=True)