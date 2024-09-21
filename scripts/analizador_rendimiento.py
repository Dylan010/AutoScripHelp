# analizador_rendimiento.py

import psutil
import platform
from deteccion_so import obtener_info_sistema

def obtener_uso_cpu():
    return psutil.cpu_percent(interval=1)

def obtener_uso_memoria():
    memoria = psutil.virtual_memory()
    return memoria.percent, memoria.used / (1024 * 1024 * 1024), memoria.total / (1024 * 1024 * 1024)

def obtener_uso_disco():
    disco = psutil.disk_usage('/')
    return disco.percent, disco.used / (1024 * 1024 * 1024), disco.total / (1024 * 1024 * 1024)

def obtener_procesos_top():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        procesos.append(proc.info)
    return sorted(procesos, key=lambda x: x['cpu_percent'], reverse=True)[:5]

def main():
    info_sistema = obtener_info_sistema()
    print(f"Sistema: {info_sistema['Sistema']} {info_sistema['Version']}")
    print(f"Arquitectura: {info_sistema['Arquitectura']}")
    
    print("\nUso de CPU:")
    print(f"{obtener_uso_cpu()}%")
    
    memoria_percent, memoria_usada, memoria_total = obtener_uso_memoria()
    print(f"\nUso de Memoria: {memoria_percent}%")
    print(f"Memoria usada: {memoria_usada:.2f} GB / {memoria_total:.2f} GB")
    
    disco_percent, disco_usado, disco_total = obtener_uso_disco()
    print(f"\nUso de Disco: {disco_percent}%")
    print(f"Espacio usado: {disco_usado:.2f} GB / {disco_total:.2f} GB")
    
    print("\nProcesos top por uso de CPU:")
    for proc in obtener_procesos_top():
        print(f"PID: {proc['pid']}, Nombre: {proc['name']}, CPU: {proc['cpu_percent']}%, Memoria: {proc['memory_percent']:.2f}%")

if __name__ == "__main__":
    main()
