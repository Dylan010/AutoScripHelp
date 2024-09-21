# creador_copias_seguridad.py

import os
import shutil
import datetime
from deteccion_so import obtener_info_sistema

def crear_copia_seguridad(origen, destino):
    fecha_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_copia = f"backup_{fecha_actual}"
    ruta_copia = os.path.join(destino, nombre_copia)
    
    try:
        shutil.copytree(origen, ruta_copia)
        print(f"Copia de seguridad creada exitosamente en: {ruta_copia}")
    except Exception as e:
        print(f"Error al crear la copia de seguridad: {e}")

def obtener_rutas_windows():
    origen = os.path.expanduser("~\\Documents")
    destino = os.path.expanduser("~\\Backups")
    return origen, destino

def obtener_rutas_linux():
    origen = os.path.expanduser("~/Documents")
    destino = os.path.expanduser("~/Backups")
    return origen, destino

def main():
    info_sistema = obtener_info_sistema()
    
    if info_sistema["Sistema"] == "Windows":
        origen, destino = obtener_rutas_windows()
    elif info_sistema["Sistema"] == "Linux":
        origen, destino = obtener_rutas_linux()
    else:
        print(f"Sistema operativo no soportado: {info_sistema['Sistema']}")
        return
    
    print(f"Se creará una copia de seguridad de: {origen}")
    print(f"La copia se guardará en: {destino}")
    
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 's':
        if not os.path.exists(destino):
            os.makedirs(destino)
        crear_copia_seguridad(origen, destino)
    else:
        print("Operación de copia de seguridad cancelada.")

if __name__ == "__main__":
    main()
