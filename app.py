import os
from flask import Flask
from models import db
from routes import api
from config import config_by_name

def create_app(config_name):
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Inicializa as extensões
    db.init_app(app)
    api.init_app(app)

    with app.app_context():
        # Cria as tabelas do banco de dados, se não existirem
        db.create_all()

    return app

# Obtém a configuração (development ou production) a partir de variável de ambiente
config_name = os.getenv('FLASK_CONFIG') or 'development'
app = create_app(config_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)