# analizador_logs.py

import os
import re
from datetime import datetime, timedelta
from deteccion_so import obtener_info_sistema

def analizar_logs_windows(dias_atras=1):
    try:
        import win32evtlog
    except ImportError:
        print("El módulo win32evtlog no está instalado. Por favor, instálelo con 'pip install pywin32'")
        return

    servidor = 'localhost'
    log_tipo = 'System'
    mano = win32evtlog.OpenEventLog(servidor, log_tipo)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(mano)

    errores = []
    advertencias = []
    fecha_limite = datetime.now() - timedelta(days=dias_atras)

    while True:
        eventos = win32evtlog.ReadEventLog(mano, flags, 0)
        if not eventos:
            break
        for evento in eventos:
            if evento.TimeGenerated < fecha_limite:
                break
            if evento.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
                errores.append(f"Error: {evento.StringInserts}")
            elif evento.EventType == win32evtlog.EVENTLOG_WARNING_TYPE:
                advertencias.append(f"Advertencia: {evento.StringInserts}")

    win32evtlog.CloseEventLog(mano)
    return errores, advertencias

def analizar_logs_linux(dias_atras=1):
    errores = []
    advertencias = []
    fecha_limite = datetime.now() - timedelta(days=dias_atras)
    
    try:
        with open("/var/log/syslog", "r") as f:
            for linea in f:
                match = re.search(r"(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2}).*?(\w+):? (.+)", linea)
                if match:
                    fecha_str, nivel, mensaje = match.groups()
                    fecha = datetime.strptime(f"{datetime.now().year} {fecha_str}", "%Y %b %d %H:%M:%S")
                    if fecha < fecha_limite:
                        continue
                    if "error" in nivel.lower():
                        errores.append(f"Error: {mensaje}")
                    elif "warning" in nivel.lower():
                        advertencias.append(f"Advertencia: {mensaje}")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de log del sistema.")
        
    return errores, advertencias

def main():
    info_sistema = obtener_info_sistema()
    dias_atras = int(input("Ingrese el número de días atrás para analizar los logs: "))
    
    if info_sistema["Sistema"] == "Windows":
        errores, advertencias = analizar_logs_windows(dias_atras)
    elif info_sistema["Sistema"] == "Linux":
        errores, advertencias = analizar_logs_linux(dias_atras)
    else:
        print(f"Sistema operativo no soportado: {info_sistema['Sistema']}")
        return
    
    print(f"\nErrores encontrados (últimos {dias_atras} días):")
    for error in errores[:10]:  # Mostrar solo los primeros 10 errores
        print(error)
    
    print(f"\nAdvertencias encontradas (últimos {dias_atras} días):")
    for advertencia in advertencias[:10]:  # Mostrar solo las primeras 10 advertencias
        print(advertencia)

if __name__ == "__main__":
    main()
