# reinicio_contrasena.py

import subprocess
import getpass
from deteccion_so import obtener_info_sistema

def reiniciar_contrasena_windows(usuario):
    nueva_contrasena = getpass.getpass("Ingrese la nueva contraseña: ")
    confirmar_contrasena = getpass.getpass("Confirme la nueva contraseña: ")
    
    if nueva_contrasena != confirmar_contrasena:
        print("Las contraseñas no coinciden. Operación cancelada.")
        return
    
    try:
        subprocess.run(["net", "user", usuario, nueva_contrasena], check=True)
        print(f"Contraseña reiniciada exitosamente para el usuario {usuario}")
    except subprocess.CalledProcessError:
        print(f"Error al reiniciar la contraseña para el usuario {usuario}")

def reiniciar_contrasena_linux(usuario):
    print("Para reiniciar la contraseña en Linux, necesitará privilegios de superusuario.")
    print("El script ejecutará el comando 'sudo passwd' para el usuario especificado.")
    
    try:
        subprocess.run(["sudo", "passwd", usuario], check=True)
        print(f"Contraseña reiniciada exitosamente para el usuario {usuario}")
    except subprocess.CalledProcessError:
        print(f"Error al reiniciar la contraseña para el usuario {usuario}")

def main():
    info_sistema = obtener_info_sistema()
    usuario = input("Ingrese el nombre de usuario cuya contraseña desea reiniciar: ")
    
    if info_sistema["Sistema"] == "Windows":
        reiniciar_contrasena_windows(usuario)
    elif info_sistema["Sistema"] == "Linux":
        reiniciar_contrasena_linux(usuario)
    else:
        print(f"Sistema operativo no soportado: {info_sistema['Sistema']}")

if __name__ == "__main__":
    main()
