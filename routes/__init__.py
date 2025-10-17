from flask_restx import Api

# Inicializa a API do Flask-RestX
api = Api(
    title='API de Sistema de Contas',
    version='1.0',
    description='Uma API para gerenciamento de contas a pagar e a receber.',
    doc='/swagger/'  # URL para a documentação do Swagger UI
)

# Importa os namespaces para que sejam registrados na API
from .usuario import ns as usuario_ns
from .conta import ns as conta_ns

# Adiciona os namespaces à API
api.add_namespace(usuario_ns, path='/usuarios')
api.add_namespace(conta_ns, path='/')
