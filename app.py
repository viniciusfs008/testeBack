from flask import Flask, request, jsonify
from models.sistema import Sistema

app = Flask(__name__)
sistema = Sistema()

@app.route("/usuario/<nome>", methods=["POST"])
def adicionar_usuario(nome):
    usuario = sistema.adicionar_usuario(nome)
    return jsonify({"message": f"Usuário '{nome}' criado com sucesso."})

@app.route("/<nome>/conta", methods=["POST"])
def adicionar_conta(nome):
    data = request.json
    usuario = sistema.usuarios.get(nome)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    try:
        usuario.adicionar_conta(data["tipo"], data["valor"], data["descricao"], data["data_vencimento"])
        sistema.salvar_dados()
        return jsonify({"message": "Conta adicionada com sucesso."})
    except KeyError as e:
        return jsonify({"error": f"Campo obrigatório faltando: {str(e)}"}), 400

@app.route("/<nome>/contas", methods=["GET"])
def listar_contas(nome):
    usuario = sistema.usuarios.get(nome)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(usuario.listar_contas())

@app.route("/<nome>/contas/<int:indice>/pagar", methods=["POST"])
def pagar_conta(nome, indice):
    usuario = sistema.usuarios.get(nome)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404

    resultado = usuario.pagar_conta(indice)
    sistema.salvar_dados()
    return jsonify({"message": resultado})

@app.route("/<nome>/totais", methods=["GET"])
def mostrar_totais(nome):
    usuario = sistema.usuarios.get(nome)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(usuario.totais())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
