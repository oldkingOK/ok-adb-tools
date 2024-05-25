# https://github.com/openatx/adbutils

from adbutils import adb

def get_devices_info():
    devices = []
    for device in adb.device_list():
        id = device.get_serialno()
        state = device.get_state()
        ro_debuggable = device.shell("getprop ro.debuggable").strip()
        devices.append((id, state, ro_debuggable))
    return devices

def install_apk(apk_path: str):
    for device in adb.device_list():
        device.install(apk_path)

def uninstall_apk(package_name: str):
    for device in adb.device_list():
        device.uninstall(package_name)

def start_dbgsrv(ida_file_name: str):
    for device in adb.device_list():
        pid = device.shell("su -c netstat -tunlp | grep :23946 | awk '{print $7}' | cut -d'/' -f1")
        if pid:
            device.shell(f"su -c kill -9 {pid}")
        device.forward("tcp:23946", "tcp:23946")
        if device.shell(f'test -f /data/local/tmp/{ida_file_name} && echo "1" || echo "0"') != '1':
            device.push(f"./dbgsrv/{ida_file_name}", f"/data/local/tmp/{ida_file_name}")
        device.shell(f"su -c chmod +x /data/local/tmp/{ida_file_name}", stream=True)
        yield device.shell(f"su -c /data/local/tmp/{ida_file_name}", stream=True)