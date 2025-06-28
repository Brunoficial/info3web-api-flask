from ..config.db import db
from ..config.extensions import bcrypt

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(260), nullable=False)
    matricula = db.Column(db.String(14), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    bio = db.Column(db.String(600), nullable=True)
    posts = db.relationship('Post', backref='autor', lazy='select')

    def __init__(self, data):
        self.nome = data.get("nome")
        self.email = data.get("email")
        self.senha = bcrypt.generate_password_hash(data.get("senha"))
        self.matricula = data.get("matricula") 

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "matricula": self.matricula
        }

    def set_password(self, senha):
        self.senha = bcrypt.generate_password_hash(senha)

    def check_password(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)
    
    @staticmethod
    def validate_data(data):
        campos = ["nome", "email", "senha", "matricula"]
        for campo in campos:
            if not data.get(campo):
                return False


    

