# API de Sistema de Contas - Versão Refatorada

Esta aplicação é uma API RESTful para gerenciamento de contas a pagar e a receber, construída com foco em boas práticas de desenvolvimento, escalabilidade e documentação. O projeto foi completamente refatorado para utilizar uma arquitetura moderna e robusta, ideal para ambientes de produção.

## Tecnologias Utilizadas

- **Backend:** Python, Flask
- **API e Documentação:** Flask-RestX (para endpoints estruturados e geração automática de documentação Swagger)
- **Banco de Dados:** PostgreSQL (orquestrado via Docker)
- **ORM:** SQLAlchemy (para mapeamento objeto-relacional e interação com o banco de dados)
- **Containerização:** Docker e Docker Compose (com ambientes separados para desenvolvimento e produção)
- **Servidor de Produção:** Gunicorn (WSGI)

---

## Como Executar (Ambiente de Desenvolvimento)

O ambiente de desenvolvimento é totalmente containerizado e configurado com hot-reload, permitindo que as alterações no código sejam aplicadas instantaneamente.

### Pré-requisitos

- Docker
- Docker Compose

### Passos para Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/viniciusfs008/testeBack.git
    cd testeBack
    ```

2.  **Crie o arquivo de configuração da API:**
    Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`. Ele define a URL de conexão que a API usará para se comunicar com o banco de dados.
    ```bash
    cp .env.example .env
    ```
    *Nenhuma alteração é necessária no `.env` para o ambiente de desenvolvimento padrão.*

3.  **Crie o arquivo de configuração do Banco de Dados:**
    Copie o arquivo de exemplo `.env.db.example` para um novo arquivo chamado `.env.db`. Este arquivo fornecerá as credenciais para o container do PostgreSQL criar o banco de dados inicial.
    ```bash
    cp .env.db.example .env.db
    ```
    *Você pode alterar as credenciais no arquivo `.env.db` se desejar, mas lembre-se de atualizar a `DATABASE_URL` no arquivo `.env` para corresponder.*

4.  **Suba os containers (Desenvolvimento):**
    Execute o comando a seguir para iniciar o ambiente de desenvolvimento:
    ```bash
    docker-compose -f docker-compose.dev.yaml up --build
    ```

A API estará disponível em `http://localhost:5000`.

---

## Documentação da API (Swagger)

Uma das principais vantagens desta arquitetura é a documentação interativa gerada automaticamente.

- **Acesse a documentação em:** `http://localhost:5000/swagger/`

Nesta página, você pode visualizar todos os endpoints disponíveis, seus parâmetros, os modelos de dados de entrada e saída, e até mesmo **executar requisições de teste diretamente pelo navegador**.

---

## Ambiente de Produção

Para produção, foi criado um `Dockerfile` otimizado que utiliza uma abordagem **multi-stage**:

1.  **Estágio de Build:** As dependências são instaladas em um ambiente temporário.
2.  **Estágio de Run:** Apenas o código da aplicação e as dependências já instaladas são copiados para uma imagem final limpa e enxuta, resultando em uma imagem menor e mais segura.

O servidor utilizado em produção é o **Gunicorn**, um servidor WSGI robusto, em vez do servidor de desenvolvimento do Flask.

Para construir e rodar a imagem de produção, utilize o arquivo `docker-compose.prod.yaml`:

    ```bash
    docker-compose -f docker-compose.prod.yaml up -d --build
    ```

---

## Estrutura do Projeto

```
/Users/viniciusferrari/dev/testeBack/
├───app.py                  # Ponto de entrada da aplicação, cria e configura o Flask.
├───config.py               # Classes de configuração (Dev, Prod).
├───requirements.txt        # Lista de dependências Python.
├───docker-compose.yaml     # Orquestra os serviços de API e banco de dados.
├───Dockerfile.prod         # Dockerfile otimizado para produção (multi-stage).
├───Dockerfile.dev          # Dockerfile para desenvolvimento com hot-reload.
├───.dockerignore           # Arquivos a serem ignorados pelo Docker.
├───.env.example            # Exemplo de variáveis de ambiente para a API.
├───.env.db.example         # Exemplo de variáveis de ambiente para o banco de dados.
├───README.md               # Esta documentação.
├───models/                 # Contém os modelos de dados SQLAlchemy.
│   ├───__init__.py         # Inicializa o objeto SQLAlchemy (db).
│   ├───conta.py            # Modelo da tabela 'contas'.
│   └───usuario.py          # Modelo da tabela 'usuarios'.
└───routes/                 # Contém a lógica dos endpoints da API.
    ├───__init__.py         # Inicializa a API Flask-RestX e registra os namespaces.
    ├───conta.py            # Endpoints e DTOs relacionados a contas.
    └───usuario.py          # Endpoints e DTOs relacionados a usuários.
```