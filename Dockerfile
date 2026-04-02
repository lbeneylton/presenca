# Seleção da linguagem
FROM python:3.11-slim

# Seleção da pasta de trabalho
WORKDIR /app

# Copia as dependencias e instala
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Agora sim copia tudo
COPY ./app /app/

# Gunicorn gerenciando 4 workers Uvicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]