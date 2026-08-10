from fastapi import FastAPI

# Inicializamos el servidor de la API
app = FastAPI(title="Mi API Profesional de Ciberseguridad")

# Ruta principal de bienvenida (Ruta raíz)
@app.get("/")
def inicio():
    return {
        "mensaje": "¡Bienvenido a mi API REST de Seguridad!",
        "estado": "Activo",
        "desarrollador": "Andrescarmona1992",
        "version": "1.0.0"
    }

# Ruta secundaria para recibir datos de ataques
@app.get("/alerta")
def registrar_alerta(tipo: str = "Desconocido", ip: str = "0.0.0.0"):
    return {
        "evento": "Registro Exitoso",
        "tipo_ataque": tipo,
        "ip_atacante": ip,
        "accion": "Bloqueo preventivo en cola"
    }
