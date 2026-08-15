# 1. Imagen oficial de Python ligera como base
FROM python:3.10-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias primero (Optimiza la caché de Docker)
COPY requirements.txt ./

# 4. Instalar todas las librerías necesarias de forma automática
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto de los scripts del proyecto al contenedor
COPY . .

# 6. Comando por defecto para arrancar tu API con Uvicorn de forma profesional
CMD ["uvicorn", "mi_api:app", "--host", "0.0.0.0", "--port", "8000"]
