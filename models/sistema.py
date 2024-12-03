import json
from models.usuario import Usuario

class Sistema:
    def __init__(self, data_file="data/usuarios.json"):
        self.data_file = data_file
        self.usuarios = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                # Ao carregar o JSON, passamos as contas para o usuário corretamente
                return {nome: Usuario(nome, contas) for nome, contas in data.items()}
        except FileNotFoundError:
            return {}

    def salvar_dados(self):
        with open(self.data_file, "w") as f:
            # Aqui, salvamos tanto o nome quanto as contas de cada usuário
            json.dump({nome: usuario.listar_contas() for nome, usuario in self.usuarios.items()}, f)

    def adicionar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = Usuario(nome)
            self.salvar_dados()
        return self.usuarios[nome]
