# Usar uma imagem Python leve
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000 para acesso ao Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
