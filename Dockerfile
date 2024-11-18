# Imagem do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /code-assistent

# Instala as dependências do sistema operacional
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o script wait-for-it.sh para o container
COPY wait-for-it.sh /code-assistent/

# Atribui permissão de execução para o wait-for-it.sh
RUN chmod +x /code-assistent/wait-for-it.sh

# Copia o arquivo requirements.txt com as depedências da aplicação
COPY requirements.txt /code-assistent/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install uwsgi

# Copia o código da aplicação para o container
COPY . /code-assistent/

# Definir variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=config.settings \
    PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expor na porta 8000 do container
EXPOSE 8000

# Comando para rodar servidor django
CMD ["uwsgi", "--ini", "code-assistent_uwsgi.ini"]
