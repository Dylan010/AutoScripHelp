# deteccion_so.py

import platform
import os
import subprocess

def obtener_info_sistema():
    sistema = platform.system()
    version = platform.version()
    maquina = platform.machine()
    
    if sistema == "Windows":
        # Obtener más detalles de Windows
        try:
            info = subprocess.check_output(["systeminfo"], universal_newlines=True)
            for line in info.split("\n"):
                if "OS Name" in line:
                    version = line.split(":")[1].strip()
                elif "System Type" in line:
                    maquina = line.split(":")[1].strip()
        except:
            pass
    elif sistema == "Linux":
        # Obtener más detalles de Linux
        try:
            with open("/etc/os-release") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("PRETTY_NAME="):
                        version = line.split("=")[1].strip().strip('"')
                        break
        except:
            pass

    return {
        "Sistema": sistema,
        "Version": version,
        "Arquitectura": maquina
    }

def main():
    info = obtener_info_sistema()
    print("Información del Sistema:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
