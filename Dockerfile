# Imagem do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do sistema operacional
RUN apt-get update && apt-get install -y curl && apt-get install -y git

# Copia o script wait-for-it.sh para o container
COPY wait-for-it.sh /app/

# Atribui permissão de execução para o wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copia o arquivo requirements.txt com as depedências da aplicação
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o container
COPY . /app/

# Definir variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=config.settings

# Executar os comandos Django necessários
RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput

# Expor na porta 8000 do container
EXPOSE 8000

# Comando para rodar servidor django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
