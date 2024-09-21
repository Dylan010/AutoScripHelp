# actualizador_software.py

import subprocess
import platform
from deteccion_so import obtener_info_sistema

def actualizar_windows():
    print("Buscando actualizaciones de Windows...")
    try:
        subprocess.run(["powershell", "Install-Module PSWindowsUpdate -Force"], check=True)
        subprocess.run(["powershell", "Import-Module PSWindowsUpdate"], check=True)
        subprocess.run(["powershell", "Get-WindowsUpdate"], check=True)
        respuesta = input("¿Desea instalar las actualizaciones? (s/n): ")
        if respuesta.lower() == 's':
            subprocess.run(["powershell", "Install-WindowsUpdate -AcceptAll -AutoReboot"], check=True)
            print("Actualizaciones de Windows instaladas.")
        else:
            print("Instalación de actualizaciones cancelada.")
    except subprocess.CalledProcessError:
        print("Error al buscar o instalar actualizaciones de Windows.")

def actualizar_linux():
    print("Actualizando lista de paquetes...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Buscando actualizaciones...")
        resultado = subprocess.run(["sudo", "apt", "list", "--upgradable"], capture_output=True, text=True, check=True)
        if "upgradable" in resultado.stdout:
            print("Actualizaciones disponibles:")
            print(resultado.stdout)
            respuesta = input("¿Desea instalar las actualizaciones? (s/n): ")
            if respuesta.lower() == 's':
                subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
                print("Actualizaciones instaladas.")
            else:
                print("Instalación de actualizaciones cancelada.")
        else:
            print("No hay actualizaciones disponibles.")
    except subprocess.CalledProcessError:
        print("Error al buscar o instalar actualizaciones.")

def main():
    info_sistema = obtener_info_sistema()
    if info_sistema["Sistema"] == "Windows":
        actualizar_windows()
    elif info_sistema["Sistema"] == "Linux":
        actualizar_linux()
    else:
        print(f"Sistema operativo no soportado: {info_sistema['Sistema']}")

if __name__ == "__main__":
    main()
