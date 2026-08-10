import os
from datetime import datetime

hoy = datetime.now().strftime('%Y-%m-%d')
nombre_carpeta = f'Reporte_{hoy}'

if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)
    print(f'✅ Carpeta creada: {nombre_carpeta}')
else:
    print(f'⚠️ La carpeta {nombre_carpeta} ya existe.')
