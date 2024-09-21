# utilidades/linux_utils.py

import subprocess
import os

def get_linux_distribution():
    try:
        with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("PRETTY_NAME="):
                    return line.split("=")[1].strip().strip('"')
    except:
        return "Linux (distribución desconocida)"

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def get_installed_packages():
    if os.path.exists("/usr/bin/dpkg"):
        return run_shell_command("dpkg -l | tail -n +6 | awk '{print $2, $3}'")
    elif os.path.exists("/usr/bin/rpm"):
        return run_shell_command("rpm -qa --qf '%{NAME} %{VERSION}\\n'")
    else:
        return "No se pudo determinar el gestor de paquetes"

def get_system_updates():
    if os.path.exists("/usr/bin/apt"):
        return run_shell_command("apt list --upgradable 2>/dev/null | tail -n +2")
    elif os.path.exists("/usr/bin/yum"):
        return run_shell_command("yum check-update")
    else:
        return "No se pudo determinar el gestor de paquetes"

def get_service_status(service_name):
    return run_shell_command(f"systemctl status {service_name}")

def get_disk_usage():
    return run_shell_command("df -h")
