# limpieza_disco.py

import os
import shutil
import platform
from deteccion_so import obtener_info_sistema

def limpiar_windows():
    carpetas_temp = [
        os.path.expanduser("~\\AppData\\Local\\Temp"),
        "C:\\Windows\\Temp"
    ]
    for carpeta in carpetas_temp:
        for root, dirs, files in os.walk(carpeta):
            for file in files:
                try:
                    os.unlink(os.path.join(root, file))
                except:
                    pass
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except:
                    pass
    print("Limpieza de archivos temporales de Windows completada.")

def limpiar_linux():
    carpetas_temp = [
        "/tmp",
        os.path.expanduser("~/.cache")
    ]
    for carpeta in carpetas_temp:
        for root, dirs, files in os.walk(carpeta):
            for file in files:
                try:
                    os.unlink(os.path.join(root, file))
                except:
                    pass
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except:
                    pass
    print("Limpieza de archivos temporales de Linux completada.")

def main():
    info_sistema = obtener_info_sistema()
    if info_sistema["Sistema"] == "Windows":
        limpiar_windows()
    elif info_sistema["Sistema"] == "Linux":
        limpiar_linux()
    else:
        print(f"Sistema operativo no soportado: {info_sistema['Sistema']}")

if __name__ == "__main__":
    main()
