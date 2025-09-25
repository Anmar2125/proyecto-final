# Dockerfile
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias Python
COPY requerimientos.txt .
RUN pip install --no-cache-dir -r requerimientos.txt

# Copiar código de la aplicación
COPY src/ .

# Exponer puerto (ajustar según tu app)
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]