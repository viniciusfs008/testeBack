from flask import request
from flask_restx import Namespace, Resource, fields
from models import db
from models.usuario import Usuario
from models.conta import Conta
from datetime import datetime

# Define o namespace para os recursos de conta
ns = Namespace('contas', description='Operações relacionadas a contas de um usuário')

# Modelo para entrada de dados de uma conta
conta_input_model = ns.model('ContaInput', {
    'tipo': fields.String(required=True, description='Tipo da conta (a_pagar ou a_receber)', enum=['a_pagar', 'a_receber']),
    'valor': fields.Float(required=True, description='Valor da conta'),
    'descricao': fields.String(required=True, description='Descrição da conta'),
    'data_vencimento': fields.Date(required=True, description='Data de vencimento (YYYY-MM-DD)')
})

# Modelo para representação de uma conta (saída)
conta_model = ns.model('Conta', {
    'id': fields.Integer(readonly=True, description='Identificador único da conta'),
    'tipo': fields.String(required=True, description='Tipo da conta'),
    'valor': fields.Float(required=True, description='Valor da conta'),
    'descricao': fields.String(required=True, description='Descrição da conta'),
    'data_vencimento': fields.Date(required=True, description='Data de vencimento'),
    'status': fields.String(readonly=True, description='Status da conta (pendente ou pago)'),
    'usuario_id': fields.Integer(attribute='usuario.id')
})

# Modelo para os totais
totais_model = ns.model('Totais', {
    'a_pagar': fields.Float(description='Total de contas a pagar pendentes'),
    'a_receber': fields.Float(description='Total de contas a receber pendentes'),
    'total_geral': fields.Float(description='Balanço geral (receber - pagar)')
})


# Helper para verificar se a conta pertence ao usuário
def verificar_pertence(conta, usuario_id):
    if conta.usuario_id != usuario_id:
        # Usamos 404 para não vazar a informação de que a conta existe
        ns.abort(404, f"Conta com id {conta.id} não encontrada para este usuário.")


@ns.route('usuarios/<int:usuario_id>/contas/')
@ns.param('usuario_id', 'O identificador do usuário')
class ContaList(Resource):
    @ns.doc('list_contas_por_usuario')
    @ns.marshal_list_with(conta_model)
    def get(self, usuario_id):
        """Lista todas as contas de um usuário específico."""
        usuario = Usuario.query.get_or_404(usuario_id)
        return usuario.contas

    @ns.doc('create_conta_para_usuario')
    @ns.expect(conta_input_model)
    @ns.marshal_with(conta_model, code=201)
    def post(self, usuario_id):
        """Adiciona uma nova conta para um usuário."""
        usuario = Usuario.query.get_or_404(usuario_id)
        data = request.json
        nova_conta = Conta(
            tipo=data['tipo'],
            valor=data['valor'],
            descricao=data['descricao'],
            data_vencimento=datetime.strptime(data['data_vencimento'], '%Y-%m-%d').date(),
            usuario=usuario
        )
        db.session.add(nova_conta)
        db.session.commit()
        return nova_conta, 201


@ns.route('usuarios/<int:usuario_id>/contas/<int:conta_id>/')
@ns.param('usuario_id', 'O identificador do usuário')
@ns.param('conta_id', 'O identificador da conta')
@ns.response(404, 'Recurso não encontrado')
class ContaResource(Resource):
    @ns.doc('get_conta')
    @ns.marshal_with(conta_model)
    def get(self, usuario_id, conta_id):
        """Exibe os detalhes de uma conta específica de um usuário."""
        Usuario.query.get_or_404(usuario_id)
        conta = Conta.query.get_or_404(conta_id)
        verificar_pertence(conta, usuario_id)
        return conta

    @ns.doc('delete_conta')
    @ns.response(204, 'Conta deletada com sucesso')
    def delete(self, usuario_id, conta_id):
        """Deleta uma conta de um usuário."""
        Usuario.query.get_or_404(usuario_id)
        conta = Conta.query.get_or_404(conta_id)
        verificar_pertence(conta, usuario_id)
        
        db.session.delete(conta)
        db.session.commit()
        return '', 204


@ns.route('usuarios/<int:usuario_id>/contas/<int:conta_id>/pagar')
@ns.param('usuario_id', 'O identificador do usuário')
@ns.param('conta_id', 'O identificador da conta a ser paga')
class PagarConta(Resource):
    @ns.doc('pagar_conta')
    @ns.response(200, 'Conta paga com sucesso')
    @ns.response(400, 'A conta já foi paga')
    @ns.marshal_with(conta_model)
    def post(self, usuario_id, conta_id):
        """Marca uma conta de um usuário como paga."""
        Usuario.query.get_or_404(usuario_id)
        conta = Conta.query.get_or_404(conta_id)
        verificar_pertence(conta, usuario_id)

        if conta.status == 'pago':
            ns.abort(400, 'A conta já foi paga.')
        
        conta.status = 'pago'
        db.session.commit()
        return conta


@ns.route('usuarios/<int:usuario_id>/totais/')
@ns.param('usuario_id', 'O identificador do usuário para calcular os totais')
class TotaisResource(Resource):
    @ns.doc('get_totais_usuario')
    @ns.marshal_with(totais_model)
    def get(self, usuario_id):
        """Calcula e exibe os totais de contas pendentes para um usuário."""
        Usuario.query.get_or_404(usuario_id)
        
        total_a_pagar = db.session.query(db.func.sum(Conta.valor)).filter(
            Conta.usuario_id == usuario_id,
            Conta.tipo == 'a_pagar',
            Conta.status == 'pendente'
        ).scalar() or 0.0

        total_a_receber = db.session.query(db.func.sum(Conta.valor)).filter(
            Conta.usuario_id == usuario_id,
            Conta.tipo == 'a_receber',
            Conta.status == 'pendente'
        ).scalar() or 0.0

        return {
            'a_pagar': total_a_pagar,
            'a_receber': total_a_receber,
            'total_geral': total_a_receber - total_a_pagar
        }