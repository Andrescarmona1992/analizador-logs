import os
from fastapi import FastAPI
from pymongo import MongoClient

# Inicializamos el servidor de la API
app = FastAPI(title="Mi API Profesional de Ciberseguridad")

# Conexión segura a MongoDB Atlas usando la variable de Render
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["analizador_logs_db"]
coleccion_logs = db["registro_alertas"]

# Ruta principal de bienvenida (Ruta raíz)
@app.get("/")
def inicio():
    return {
        "mensaje": "¡Bienvenido a mi API REST de Seguridad!",
        "estado": "Activo",
        "desarrollador": "Andrescarmona1992",
        "version": "1.0.0"
    }

# Ruta secundaria para recibir datos de ataques y guardarlos en MongoDB
@app.get("/alerta")
def registrar_alerta(tipo: str = "Desconocido", ip: str = "0.0.0.0"):
    # Estructuramos el registro que se guardará en internet
    nuevo_registro = {
        "tipo_ataque": tipo,
        "ip_atacante": ip,
        "accion": "Bloqueo preventivo en cola"
    }
    
    # Guardamos el log de ciberseguridad en la base de datos de MongoDB
    coleccion_logs.insert_one(nuevo_registro)
    
    # Respondemos al usuario de forma exitosa
    return {
        "evento": "Registro Exitoso",
        "tipo_ataque": tipo,
        "ip_atacante": ip,
        "accion": "Bloqueo preventivo en cola"
    }
