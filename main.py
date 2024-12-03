from SistemaContas import SistemaContas

def main():
    sistema = SistemaContas()

    while True:
        print("\n=== Sistema de Contas ===")
        print("1. Adicionar conta")
        print("2. Listar contas")
        print("3. Mostrar totais")
        print("4. Pagar conta")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                tipo = input("Tipo de conta ('a_pagar' ou 'a_receber'): ")
                valor = float(input("Valor: R$"))
                descricao = input("Descrição: ")
                data_vencimento = input("Data de vencimento (YYYY-MM-DD): ")
                try:
                    sistema.adicionar_conta(tipo, valor, descricao, data_vencimento)
                    print("Conta adicionada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")
            case "2":
                print("\n=== Listagem de Contas ===")
                sistema.listar_contas()
            case "3":
                print("\n=== Totais ===")
                sistema.mostrar_totais()
            case "4":
                print("\n=== Pagar Conta ===")
                sistema.listar_contas()
                try:
                    indice = int(input("Digite o número da conta que deseja pagar: "))
                    sistema.pagar_conta(indice)
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")
            case "5":
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
