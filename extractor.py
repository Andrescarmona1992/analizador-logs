import urllib.request
from bs4 import BeautifulSoup

def ejecutar_web_scraping():
    print("🤖 [SISTEMA] Iniciando robot de Web Scraping Avanzado...")
    print("🌐 Conectando a la página web de seguridad para extraer datos...")
    
    # URL de prueba simulada (página de documentación de Python)
    url = "https://python.org"
    
    try:
        # Simulamos un navegador real para evitar bloqueos de seguridad
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        
        # El cerebro de BeautifulSoup empieza a analizar el código de la página
        soup = BeautifulSoup(html, 'html.parser')
        
        print("\n🎯 [ÉXITO] ¡Datos extraídos de forma estructurada!")
        print("📝 Últimas noticias y eventos encontrados:")
        
        # Buscamos elementos reales de la página (los títulos de las secciones)
        for link in soup.find_all('a', limit=5):
            texto = link.text.strip()
            enlace = link.get('href')
            if texto and enlace:
                print(f"🔹 {texto} -> Enlace: {enlace}")
                
    except Exception as e:
        print(f"[ERROR] No se pudo extraer la información: {e}")

if __name__ == "__main__":
    ejecutar_web_scraping()
