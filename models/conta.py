from datetime import datetime
from . import db

class Conta(db.Model):
    """Modelo de dados para a Conta."""
    __tablename__ = 'contas'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)  # 'a_pagar' ou 'a_receber'
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    data_vencimento = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pendente') # 'pendente' ou 'pago'
    
    # Chave estrangeira para o usuário
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    # Relacionamento com o usuário
    usuario = db.relationship('Usuario', back_populates='contas')

    def __repr__(self):
        return f'<Conta {self.descricao} - {self.valor}>'