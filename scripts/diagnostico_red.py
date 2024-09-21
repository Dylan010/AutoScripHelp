# diagnostico_red.py

import subprocess
import platform
import socket

def ejecutar_comando(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        resultado = e.output
    return resultado

def ping(host):
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = f"ping {parametro} 4 {host}"
    return ejecutar_comando(comando)

def traceroute(host):
    comando = f"tracert" if platform.system().lower() == "windows" else f"traceroute"
    comando += f" {host}"
    return ejecutar_comando(comando)

def nslookup(host):
    comando = f"nslookup {host}"
    return ejecutar_comando(comando)

def verificar_puertos_comunes(host):
    puertos_comunes = [80, 443, 22, 21, 25, 3306, 3389]
    resultados = []
    for puerto in puertos_comunes:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((host, puerto))
        if resultado == 0:
            resultados.append(f"Puerto {puerto}: Abierto")
        else:
            resultados.append(f"Puerto {puerto}: Cerrado")
        sock.close()
    return "\n".join(resultados)

def main():
    host = input("Ingrese el host para diagnosticar (por ejemplo, www.google.com): ")
    
    print("\n--- Ejecutando ping ---")
    print(ping(host))
    
    print("\n--- Ejecutando traceroute ---")
    print(traceroute(host))
    
    print("\n--- Ejecutando nslookup ---")
    print(nslookup(host))
    
    print("\n--- Verificando puertos comunes ---")
    print(verificar_puertos_comunes(host))

if __name__ == "__main__":
    main()
