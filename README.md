# 🚀 Analizador de Logs y Sistema Automatizado de Alertas (Termux / Linux)

Solución profesional de automatización ligera diseñada para ejecutarse en entornos Linux y terminales móviles como **Termux**, optimizando el uso de recursos y lista para despliegue continuo.

## 🛠️ Arquitectura del Proyecto

* **`extractor.py`**: Módulo encargado del raspado, recolección y análisis de logs estructurados.
* **`alertas_telegram.py`**: Integración asíncrona con la API de bots de Telegram para despacho de notificaciones críticas.
* **`automatizacion.py`**: El motor principal que orquesta y programa los flujos de tareas en segundo plano.
* **`mi_api.py`**: Microservicio ligero (API Endpoint) para la consulta externa de datos procesados.
* **`seguridad_auth.py` & `reporte_seguridad.txt`**: Capa dedicada a la validación de accesos seguros (`X-Auth-Token`) y auditoría del sistema.

## 🐳 Infraestructura y Despliegue Continuo (CI/CD)

* **`Dockerfile`**: Configuración lista para empaquetar y migrar este entorno a la nube de forma idéntica mediante contenedores Docker.
* **`.github/flujos de trabajo`**: Automatización de pruebas y despliegue integrado directamente con las herramientas de GitHub Actions.

## 📱 Ejecución Rápida en Termux
```bash
pkg update && pkg install python git
git clone https://github.com
cd analizador-logs
python automatizacion.py
```
