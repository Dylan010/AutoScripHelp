# Scripts de Automatización para Helpdesk

```
automatizacion-helpdesk/
│
├── README.md
├── requisitos.txt
├── script_maestro.py
│
├── scripts/
│   ├── deteccion_so.py
│   ├── limpieza_disco.py
│   ├── diagnostico_red.py
│   ├── analizador_logs.py
│   ├── actualizador_software.py
│   ├── creador_copias_seguridad.py
│   ├── reinicio_contraseña.py
│   ├── escaner_malware.py
│   ├── analizador_rendimiento.py
│   ├── busqueda_archivos.py
│   └── info_sistema.sh
│
└── utilidades/
    ├── __init__.py
    ├── utilidades_windows.py
    └── utilidades_linux.py
```

## README.md

# Scripts de Automatización para Helpdesk

Este proyecto contiene una colección de scripts de automatización diseñados para ayudar a los profesionales de helpdesk a resolver rápidamente problemas comunes en sistemas Windows y Linux. Estos scripts pueden identificar el sistema operativo en el que se están ejecutando y realizar tareas específicas para agilizar el proceso de resolución de problemas.

## Scripts

1. **deteccion_so.py**: Identifica el sistema operativo y proporciona información básica del sistema.
2. **limpieza_disco.py**: Realiza operaciones de limpieza de disco, eliminando archivos temporales y liberando espacio.
3. **diagnostico_red.py**: Ejecuta diagnósticos de red, incluyendo pruebas de ping y búsquedas DNS.
4. **analizador_logs.py**: Analiza los registros del sistema para identificar posibles problemas y errores comunes.
5. **actualizador_software.py**: Verifica e instala actualizaciones disponibles para paquetes de software comunes.
6. **creador_copias_seguridad.py**: Crea copias de seguridad de datos importantes del usuario y configuraciones del sistema.
7. **reinicio_contraseña.py**: Ayuda a restablecer contraseñas de usuario en sistemas Windows y Linux.
8. **escaner_malware.py**: Realiza un escaneo básico de malware utilizando herramientas integradas del sistema.
9. **analizador_rendimiento.py**: Analiza el rendimiento del sistema y proporciona recomendaciones para mejorarlo.
10. **busqueda_archivos.py**: Busca archivos específicos o tipos de archivos en todo el sistema.
11. **info_sistema.sh**: Script de Bash para recopilar información detallada del sistema en sistemas Linux.

## Uso

1. Clona el repositorio:
   ```
   git clone https://github.com/Dylan010/AutoScripHelp.git
   ```

2. Instala las dependencias requeridas:
   ```
   pip install -r requisitos.txt
   ```

3. Ejecuta el script deseado con los permisos apropiados:
   ```
   python scripts-maestro.py
   ```

## Requisitos

- Python 3.6+
- Bash (para sistemas Linux)

Consulta `requisitos.txt` para ver las dependencias adicionales de paquetes Python.

