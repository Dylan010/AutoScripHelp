# script_maestro.py

import os
import subprocess
from scripts.deteccion_so import obtener_info_sistema


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_script(script):
    try:
        subprocess.run(['python', f'scripts/{script}'])
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
    input("\nPresione Enter para continuar...")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("=== Automatización para Helpdesk ===")
        print("1. Detección del Sistema Operativo")
        print("2. Limpieza de Disco")
        print("3. Diagnóstico de Red")
        print("4. Analizador de Logs")
        print("5. Actualizador de Software")
        print("6. Creador de Copias de Seguridad")
        print("7. Reinicio de Contraseña")
        print("8. Escáner de Malware")
        print("9. Analizador de Rendimiento")
        print("10. Búsqueda de Archivos")
        print("11. Información del Sistema (solo Linux)")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '0':
            break
        elif opcion == '1':
            ejecutar_script('deteccion_so.py')
        elif opcion == '2':
            ejecutar_script('limpieza_disco.py')
        elif opcion == '3':
            ejecutar_script('diagnostico_red.py')
        elif opcion == '4':
            ejecutar_script('analizador_logs.py')
        elif opcion == '5':
            ejecutar_script('actualizador_software.py')
        elif opcion == '6':
            ejecutar_script('creador_copias_seguridad.py')
        elif opcion == '7':
            ejecutar_script('reinicio_contrasena.py')
        elif opcion == '8':
            ejecutar_script('escaner_malware.py')
        elif opcion == '9':
            ejecutar_script('analizador_rendimiento.py')
        elif opcion == '10':
            ejecutar_script('busqueda_archivos.py')
        elif opcion == '11':
            info_sistema = obtener_info_sistema()
            if info_sistema["Sistema"] == "Linux":
                subprocess.run(['bash', 'scripts/info_sistema.sh'])
                input("\nPresione Enter para continuar...")
            else:
                print("Este script solo está disponible en sistemas Linux.")
                input("\nPresione Enter para continuar...")
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
