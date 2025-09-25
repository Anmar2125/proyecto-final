# Dockerfile
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY src/requerimientos.txt .
RUN pip install --no-cache-dir -r requerimientos.txt

# Copiar aplicación
COPY src/ ./src/

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "src/app.py"]
