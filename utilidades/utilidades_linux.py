# utilidades/windows_utils.py

import winreg
import subprocess

def get_windows_version():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        version = winreg.QueryValueEx(key, "ProductName")[0]
        return version
    except:
        return "Windows (versión desconocida)"

def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def get_installed_programs():
    command = "Get-WmiObject -Class Win32_Product | Select-Object -Property Name, Version | Format-Table -AutoSize"
    return run_powershell_command(command)

def get_windows_updates():
    command = "Get-Hotfix | Select-Object -Property HotFixID, InstalledOn | Format-Table -AutoSize"
    return run_powershell_command(command)

def get_service_status(service_name):
    command = f"Get-Service -Name {service_name} | Select-Object -Property Name, Status | Format-Table -AutoSize"
    return run_powershell_command(command)
