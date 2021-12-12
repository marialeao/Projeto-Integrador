from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
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
# # teste    
# if __name__ == "__main__":
#     # criar tabelas
#     db.create_all()

#     # teste da classe Pessoa
#     p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
#         telefone = "47 99012 3232")
#     p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
#         telefone = "47 98822 2531")        
    
#     # persistir
#     db.session.add(p1)
#     db.session.add(p2)
#     db.session.commit()
    
#     # exibir a pessoa
#     print(p2)

#     # exibir a pessoa no format json
#     print(p2.json())