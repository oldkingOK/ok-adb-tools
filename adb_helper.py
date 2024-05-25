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