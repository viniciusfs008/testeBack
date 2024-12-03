from datetime import datetime

class Conta:
    def __init__(self, tipo, valor, descricao, data_vencimento):
        self.tipo = tipo  # 'a_pagar' ou 'a_receber'
        self.valor = valor
        self.descricao = descricao
        self.data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")
        self.status = "pendente"  # Padrão: todas as contas começam como pendentes

    def pagar(self):
        self.status = "pago"

    def __str__(self):
        return (f"Tipo: {self.tipo}, Valor: R${self.valor:.2f}, "
                f"Descrição: {self.descricao}, Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}, "
                f"Status: {self.status}")