import os

def analizar_log(archivo):
    """
    Escanea archivos del sistema en busca de patrones sospechosos.
   
    """
    palabras_alerta = ["ERROR", "FAILED", "CRITICAL", "INTRUSION", "PASSWORD"]
    
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            print(f"--- Iniciando análisis de: {archivo} ---")
            for linea in f:
                # Convertimos a mayúsculas para no perder ninguna alerta
                if any(alerta in linea.upper() for alerta in palabras_alerta):
                    print(f"[!] ALERTA SEGURIDAD: {linea.strip()}")
    else:
        print("❌ Archivo no encontrado. Crea un archivo 'log.txt' para probar.")

# --- PRUEBA DEL SISTEMA ---
# 1. Crea un archivo llamado log.txt
# 2. Escribe dentro: "FAILED login attempt from admin"
# 3. Ejecuta este código
analizar_log("log.txt")