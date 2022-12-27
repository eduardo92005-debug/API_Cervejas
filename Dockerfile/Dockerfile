FROM python:3.8

# Cria o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY API_Cervejas/requirements.txt .
COPY API_Cervejas/src/ .
COPY API_Cervejas/run.py .

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Expõe a porta 5000
EXPOSE 4444

# Define o comando para iniciar o aplicativo
CMD ["python3", "run.py"]
