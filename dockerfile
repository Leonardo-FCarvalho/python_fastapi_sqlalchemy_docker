# dockerfile

# Baixar a imagem oficial do docker
FROM python:3.11.2

# Configurar diretório de trabalho
WORKDIR /app

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o projeto
COPY . .