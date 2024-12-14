# Use a imagem oficial do Python
FROM python:3.9-slim

# Crie o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY ./project /app/project
COPY requirements.txt /app/requirements.txt

# Configure o PYTHONPATH para incluir o diretório do projeto
ENV PYTHONPATH=/app

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r /app/requirements.txt

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "project.__main__:app", "--host", "0.0.0.0", "--port", "8080"]
