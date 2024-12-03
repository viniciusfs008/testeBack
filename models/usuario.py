class Usuario:
    def __init__(self, nome, contas=None):
        self.nome = nome
        # Se não houver contas, inicializa com uma lista vazia
        self.contas = contas if contas is not None else []

    def adicionar_conta(self, tipo, valor, descricao, data_vencimento):
        conta = {
            "tipo": tipo,
            "valor": valor,
            "descricao": descricao,
            "data_vencimento": data_vencimento,
            "status": "pendente"  # Por padrão, a conta começa como "pendente"
        }
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas

    def pagar_conta(self, indice):
        try:
            conta = self.contas[indice]
            if conta["status"] == "pendente":
                conta["status"] = "pago"
                return "Conta paga com sucesso."
            else:
                return "A conta já foi paga."
        except IndexError:
            return "Conta não encontrada."

    def totais(self):
        total_a_pagar = sum(conta["valor"] for conta in self.contas if conta["tipo"] == "a_pagar")
        total_a_receber = sum(conta["valor"] for conta in self.contas if conta["tipo"] == "a_receber")
        return {
            "a_pagar": total_a_pagar,
            "a_receber": total_a_receber,
            "total_geral": total_a_receber - total_a_pagar
        }
