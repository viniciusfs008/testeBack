# Sistema de Contas - API Flask

Esta aplicação é uma API simples de gerenciamento de contas a pagar e a receber, onde cada usuário pode adicionar contas, visualizar as contas registradas, pagar contas e visualizar totais.

Utilize Insominia ou Postman para realizar os testes com seu endereço ip local na porta 5000.

exemplo: http://127.0.0.1:5000

## Para iniciar a aplicação

É necessario ter o Docker.

No diretório raiz use: 

    docker compose up --build

## Endpoints da API

A aplicação possui as seguintes rotas:

### 1. **Criar Usuário**
- **Método:** `POST`
- **Rota:** `/usuario/<nome>`
- **Descrição:** Cria um novo usuário com o nome especificado.

#### exemplo de request   
    /usuario/vinicius

#### Exemplo de resposta:
```json
{
  "message": "Usuário 'vinicius' criado com sucesso."
}
```

---

### 2. **Adicionar Conta**
- **Método:** `POST`
- **Rota:** `/<nome>/conta`
- **Descrição:** Adiciona uma conta a pagar ou a receber para o usuário especificado. Os dados da conta devem ser enviados no corpo da requisição em formato JSON.
  
#### Parâmetros JSON esperados:
- `tipo`: Tipo da conta. Pode ser "a_pagar" ou "a_receber".
- `valor`: Valor da conta.
- `descricao`: Descrição da conta.
- `data_vencimento`: Data de vencimento da conta no formato "YYYY-MM-DD".

#### exemplo de request   
    /vinicius/conta

    {
        "tipo": "a_pagar",
        "valor": 100.0,
        "descricao": "Conta de luz",
        "data_vencimento": "2024-12-10"
    }

#### Exemplo de resposta:
```json
{
  "message": "Conta adicionada com sucesso."
}
```

---

### 3. **Listar Contas**
- **Método:** `GET`
- **Rota:** `/<nome>/contas`
- **Descrição:** Lista todas as contas registradas para o usuário especificado.

#### exemplo de request   
    /vinicius/contas

#### Exemplo de resposta (se houver contas registradas):
```json
[
  {
    "tipo": "a_pagar",
    "valor": 100.0,
    "descricao": "Conta de luz",
    "data_vencimento": "2024-12-10",
    "status": "pendente"
  }
]
```

---

### 4. **Pagar Conta**
- **Método:** `POST`
- **Rota:** `/<nome>/contas/<indice>/pagar`
- **Descrição:** Marca a conta do índice especificado como paga para o usuário especificado.

#### exemplo de request   
    /vinicius/contas/1/pagar

#### Exemplo de resposta:
```json
{
  "message": "Conta paga com sucesso."
}
```

---

### 5. **Mostrar Totais**
- **Método:** `GET`
- **Rota:** `/<nome>/totais`
- **Descrição:** Exibe o total de contas a pagar, a receber e o total geral do usuário especificado.

#### exemplo de request   
    /vinicius/totais

#### Exemplo de resposta:
```json
{
  "a_pagar": 100.0,
  "a_receber": 0.0,
  "total_geral": -100.0
}
```

---

## Dependências

- `Flask`: Framework web para Python.
- `json`: Biblioteca para manipulação de dados em formato JSON (já inclusa no Python).

