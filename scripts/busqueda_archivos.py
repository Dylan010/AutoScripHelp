# busqueda_archivos.py

import os
import fnmatch
from deteccion_so import obtener_info_sistema

def buscar_archivos(directorio_inicio, patron):
    resultados = []
    for raiz, dirs, archivos in os.walk(directorio_inicio):
        for nombre in fnmatch.filter(archivos, patron):
            resultados.append(os.path.join(raiz, nombre))
    return resultados

def obtener_directorio_inicio(sistema):
    if sistema == "Windows":
        return os.path.expanduser("~")  # Directorio del usuario en Windows
    elif sistema == "Linux":
        return "/"  # Directorio raíz en Linux
    else:
        return os.getcwd()  # Directorio actual como fallback

def main():
    info_sistema = obtener_info_sistema()
    directorio_inicio = obtener_directorio_inicio(info_sistema["Sistema"])
    
    patron = input("Ingrese el patrón de búsqueda (por ejemplo, *.txt para buscar archivos de texto): ")
    print(f"Buscando archivos que coincidan con '{patron}' en {directorio_inicio}...")
    
    resultados = buscar_archivos(directorio_inicio, patron)
    
    if resultados:
        print(f"Se encontraron {len(resultados)} archivos:")
        for archivo in resultados[:10]:  # Mostrar solo los primeros 10 resultados
            print(archivo)
        if len(resultados) > 10:
            print(f"... y {len(resultados) - 10} más.")
    else:
        print("No se encontraron archivos que coincidan con el patrón de búsqueda.")

if __name__ == "__main__":
    main()
