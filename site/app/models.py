from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app.config import Config

class Usuario(UserMixin,db.Model):
    email = db.Column(db.String(256))
    nome = db.Column(db.String,nullable=False)
    senha_hash = db.Column(db.String(256))

    def get_id(self):
        return self.cpf

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)
    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)  

    def __repr__(self):
        return f'<Usuario {self.nome_usuario}>'
