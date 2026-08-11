import os
from fastapi import FastAPI
from pymongo import MongoClient
import requests

# Inicializamos la API
app = FastAPI(title="API de Ciberseguridad con MongoDB y Telegram")

# Conexión a MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["analizador_logs_db"]
coleccion_logs = db["registro_alertas"]

# Credenciales de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_alerta_telegram(tipo, ip):
    # Estructuramos el mensaje de ciberseguridad
    mensaje = (
        f"🚨 *ALERTA DE SEGURIDAD DETECTADA* 🚨\n\n"
        f"⚠️ *Tipo:* {tipo}\n"
        f"🌐 *IP Atacante:* {ip}\n"
        f"🔒 *Acción:* Bloqueo preventivo aplicado."
    )
    url = f"https://telegram.org{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error al enviar a Telegram: {e}")

# Ruta principal (Bienvenida)
@app.get("/")
def inicio():
    return {
        "mensaje": "¡API REST de Seguridad Operativa!",
        "estado": "Conectado a MongoDB y Telegram",
        "desarrollador": "Andrescarmona1992"
    }

# Ruta de alertas (Guarda en base de datos y notifica al celular)
@app.get("/alerta")
def registrar_alerta(tipo: str = "Desconocido", ip: str = "0.0.0.0"):
    nuevo_registro = {
        "tipo_ataque": tipo,
        "ip_atacante": ip,
        "accion": "Bloqueo preventivo en cola"
    }
    
    # 1. Guarda en la base de datos en la nube
    coleccion_logs.insert_one(nuevo_registro)
    
    # 2. Envía la alerta instantánea a tu Telegram
    enviar_alerta_telegram(tipo, ip)
    
    return {
        "status": "Procesado",
        "base_de_datos": "Guardado exitoso",
        "notificacion": "Enviada a Telegram"
    }
