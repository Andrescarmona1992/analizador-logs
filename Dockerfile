
# 1. Usamos una imagen oficial de Python ligera como base
FROM python:3.10-slim

# 2. Creamos y nos movemos a la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalamos las librerías necesarias incluyendo pymongo para la base de datos
RUN pip install --no-cache-dir fastapi uvicorn requests cryptography pymongo[srv]

# 4. Copiamos todos tus scripts de ciberseguridad dentro del contenedor
COPY automatizacion.py mi_api.py alertas_telegram.py ./

# 5. Comando por defecto para arrancar tu API de seguridad con Uvicorn
CMD ["uvicorn", "mi_api:app", "--host", "0.0.0.0", "--port", "8000"]
