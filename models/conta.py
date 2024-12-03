class Conta:
    def __init__(self, tipo, valor, descricao, data_vencimento):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.status = "pendente"

    def pagar(self):
        self.status = "pago"

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "descricao": self.descricao,
            "data_vencimento": self.data_vencimento,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        conta = cls(data["tipo"], data["valor"], data["descricao"], data["data_vencimento"])
        conta.status = data.get("status", "pendente")
        return conta
