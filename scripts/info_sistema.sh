#!/bin/bash

# info_sistema.sh

echo "Información del Sistema"
echo "======================="

# Información del sistema operativo
echo "Sistema Operativo:"
uname -a

# Información de la CPU
echo -e "\nInformación de la CPU:"
lscpu | grep "Model name"
lscpu | grep "CPU(s):"

# Información de la memoria
echo -e "\nInformación de la Memoria:"
free -h

# Información del disco
echo -e "\nInformación del Disco:"
df -h

# Procesos en ejecución
echo -e "\nProcesos principales en ejecución:"
ps aux --sort=-%cpu | head -n 6

# Información de red
echo -e "\nInformación de Red:"
ip addr show

# Temperatura del sistema (si sensors está instalado)
if command -v sensors &> /dev/null
then
    echo -e "\nTemperatura del Sistema:"
    sensors
else
    echo -e "\nEl comando 'sensors' no está instalado. No se puede mostrar la temperatura del sistema."
fi

echo -e "\nFin del informe"
