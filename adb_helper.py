# https://github.com/openatx/adbutils

from adbutils import adb
from time import sleep

def get_devices_info():
    devices = []
    for device in adb.device_list():
        id = device.get_serialno()
        state = device.get_state()
        ro_debuggable = device.shell("getprop ro.debuggable").strip()
        devices.append((id, state, ro_debuggable))
    return devices

def install_apk(device_index:int, apk_path: str):
    adb.device_list()[device_index].install(apk_path)

def uninstall_apk(device_index:int, package_name: str):
    adb.device_list()[device_index].uninstall(package_name)

def start_dbgsrv(device_index:int, ida_file_name: str):
    device = adb.device_list()[device_index]
    pid = device.shell("su -c netstat -tunlp | grep :23946 | awk '{print $7}' | cut -d'/' -f1")
    if pid:
        device.shell(f"su -c kill -9 {pid}")
    device.forward("tcp:23946", "tcp:23946")
    if device.shell(f'test -f /data/local/tmp/{ida_file_name} && echo "1" || echo "0"') != '1':
        device.push(f"./dbgsrv/{ida_file_name}", f"/data/local/tmp/{ida_file_name}")
    device.shell(f"su -c chmod +x /data/local/tmp/{ida_file_name}", stream=True)
    return device.shell(f"su -c /data/local/tmp/{ida_file_name}", stream=True)

def start_debug_app(device_index:int, package: str, activity: str):
    device = adb.device_list()[device_index]
    device.shell(f"am start -D -n {package}/{activity}")
    sleep(0.5)
    pid = device.shell(f"pidof {package}")
    return pid, device.shell(f'su -c logcat --pid {pid}', stream=True)

def forward(device_index:int, local: str, remote: str):
    adb.device_list()[device_index].forward(local, remote)