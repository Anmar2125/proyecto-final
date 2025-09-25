# Proyecto Final – Automatización y Predicción de Microgrid

## Integrantes del Grupo 4
- Mario Pérez  
- Han Ruiz
- Angello Romero

## Docker Hub
La imagen pública del proyecto está disponible en:  
👉 [https://hub.docker.com/r/marq2530/proyecto-final](https://hub.docker.com/r/marq2530/proyecto-final)

## Dockerfile Final
```dockerfile
FROM python:3.11-slim

# Instalar dependencias de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY src/requerimientos.txt .
RUN pip install --no-cache-dir -r requerimientos.txt

# Copiar el código de la aplicación
COPY src/ ./src/

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "src/app.py"]
