from ..config.db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(60), nullable=False)
    matricula = db.Column(db.String(14), nullable=False, unique=True)

    def __init__(self, data):
        self.nome = data.get("nome")
        self.email = data.get("email")
        self.senha = data.get("senha")
        self.matricula = data.get("matricula") 

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "matricula": self.matricula
        }
    
    @staticmethod
    def validateData(data):
        campos = ["nome", "email", "senha", "matricula"]
        for campo in campos:
            if not data.get(campo):
                return False


    

