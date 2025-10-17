from flask import request
from flask_restx import Namespace, Resource, fields
from models import db
from models.usuario import Usuario

# Define o namespace para os recursos de usuário
ns = Namespace('usuarios', description='Operações relacionadas a usuários')

# Modelo para a criação de um usuário (entrada)
usuario_input_model = ns.model('UsuarioInput', {
    'nome': fields.String(required=True, description='Nome do usuário')
})

# Modelo para a representação de um usuário (saída)
usuario_model = ns.model('Usuario', {
    'id': fields.Integer(readonly=True, description='Identificador único do usuário'),
    'nome': fields.String(required=True, description='Nome do usuário')
})

@ns.route('/')
class UsuarioList(Resource):
    @ns.doc('list_usuarios')
    @ns.marshal_list_with(usuario_model)
    def get(self):
        """Lista todos os usuários."""
        return Usuario.query.all()

    @ns.doc('create_usuario')
    @ns.expect(usuario_input_model)
    @ns.marshal_with(usuario_model, code=201)
    def post(self):
        """Cria um novo usuário."""
        data = request.json
        if Usuario.query.filter_by(nome=data['nome']).first():
            ns.abort(409, f"Usuário com nome '{data['nome']}' já existe.")
        
        novo_usuario = Usuario(nome=data['nome'])
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario, 201

@ns.route('/<int:id>')
@ns.response(404, 'Usuário não encontrado')
@ns.param('id', 'O identificador do usuário')
class UsuarioResource(Resource):
    @ns.doc('get_usuario')
    @ns.marshal_with(usuario_model)
    def get(self, id):
        """Exibe os detalhes de um usuário."""
        usuario = Usuario.query.get_or_404(id)
        return usuario

    @ns.doc('delete_usuario')
    @ns.response(204, 'Usuário deletado com sucesso')
    def delete(self, id):
        """Deleta um usuário."""
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204
