from Conta import Conta

class SistemaContas:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, tipo, valor, descricao, data_vencimento):
        if tipo not in ("a_pagar", "a_receber"):
            raise ValueError("Tipo de conta inválido. Use 'a_pagar' ou 'a_receber'.")
        conta = Conta(tipo, valor, descricao, data_vencimento)
        self.contas.append(conta)

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta registrada.")
            return
        for idx, conta in enumerate(self.contas, start=1):
            print(f"{idx}. {conta}")

    def pagar_conta(self, indice):
        if 1 <= indice <= len(self.contas):
            conta = self.contas[indice - 1]
            if conta.status == "pendente":
                conta.pagar()
                print(f"Conta '{conta.descricao}' marcada como paga.")
            else:
                print(f"Conta '{conta.descricao}' já está paga.")
        else:
            print("Índice inválido.")

    def total_contas(self, tipo=None):
        total = sum(conta.valor for conta in self.contas if tipo is None or conta.tipo == tipo)
        return total

    def mostrar_totais(self):
        total_a_pagar = self.total_contas("a_pagar")
        total_a_receber = self.total_contas("a_receber")
        total_geral = self.total_contas("a_receber") - self.total_contas("a_pagar")
        print(f"Total a pagar: R${total_a_pagar:.2f}")
        print(f"Total a receber: R${total_a_receber:.2f}")
        print(f"Total geral: R${total_geral:.2f}")