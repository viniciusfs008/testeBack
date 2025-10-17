from . import db

class Usuario(db.Model):
    """Modelo de dados para o Usuário."""
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    
    # Relacionamento com as contas
    contas = db.relationship('Conta', back_populates='usuario', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Usuario {self.nome}>'