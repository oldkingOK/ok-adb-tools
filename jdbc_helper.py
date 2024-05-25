from subprocess import Popen, PIPE
import adb_helper
import atexit

def start_jdbc(device_index, pid):
    adb_helper.forward(device_index, "tcp:8700", f"jdwp:{pid}")
    proc = Popen(f"jdb -connect com.sun.jdi.SocketAttach:hostname=127.0.0.1,port=8700".split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)

    atexit.register(lambda: proc.kill())
    return proc.stdout, proc.stderr

if __name__ == "__main__":
    stdout, stderr = start_jdbc(0, 1234)
    print(stdout.read())
    print(stderr.read().decode('gbk'))
    tmp = ''