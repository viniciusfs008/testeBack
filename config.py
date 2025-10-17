import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Configurações base da aplicação."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'teste-chave'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    ERROR_404_HELP = False


class DevelopmentConfig(Config):
    """Configurações de desenvolvimento."""
    DEBUG = True
    # Usa SQLite para desenvolvimento local se DATABASE_URL não estiver definida
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///./dev.db'


class ProductionConfig(Config):
    """Configurações de produção."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


# Mapeamento das configurações
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

key = Config.SECRET_KEY
