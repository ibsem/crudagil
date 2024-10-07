from flask_login import UserMixin
from app import db

class Projeto(db.Model):
    projeto_id = db.Column(db.Integer, primary_key=True)
    nome_projeto = db.Column(db.String(255))
    descricao = db.Column(db.String(500))
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)

class Sprint(db.Model):
    sprint_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.projeto_id'))
    nome_sprint = db.Column(db.String(255))
    descricao = db.Column(db.String(500))
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)
    status = db.Column(db.String(10))
    responsavel = db.Column(db.String(255))

class Usuario(db.Model, UserMixin):
    usuario_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    nome = db.Column(db.String(255))
    funcao = db.Column(db.String(100))
    senha = db.Column(db.String(8))

    def is_active(self):
        # Adicione lógica aqui para determinar se o usuário está ativo
        # Por exemplo, você pode verificar se o usuário foi suspenso ou banido
        return True  # Substitua isso pela lógica real

    def get_id(self):
        return str(self.usuario_id)

