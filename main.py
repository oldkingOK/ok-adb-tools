from resource.ok_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from apk_helper import get_apk_info
from constants import IDA
import PyQt5.QtCore as QtCore
import adb_helper
import threading

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def on_open_apk():
    """
    当按下“打开”Apk按钮时触发
    """

    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    file_name, _ = QFileDialog.getOpenFileName(None, "打开Apk文件", "", "Apk Files (*.apk)", options=options)
    if file_name:
        print(file_name)
    else:
        print("No file selected")
        return

    global window, package, activity, apk_selected

    apk_selected = True
    package, activity = get_apk_info(file_name)
    label_package_name: QLabel = window.label_package_name
    label_package_name.setText(package)

    comboBox_open_apk: QComboBox = window.comboBox_open_apk
    comboBox_open_apk.addItem(file_name)

def install_apk():
    comboBox_open_apk: QComboBox = window.comboBox_open_apk
    text = comboBox_open_apk.currentText()
    if text == "":
        QMessageBox.warning(None, "警告", "No file selected")
        return
    adb_helper.install_apk(text)
    
def uninstall_apk():
    label_package_name: QLabel = window.label_package_name
    text = label_package_name.text()
    if text == "包名":
        QMessageBox.warning(None, "警告", "No file selected")
        return
    adb_helper.uninstall_apk(text)


def reading_stream(stream, textBrowser):
    """
    读取流并将其显示在textBrowser中
    """
    tmp = b""
    while True:
        try:
            b = stream.read(1)
        except Exception as e:
            break
        if b == b"\n":
            textBrowser.append(tmp.decode())
            tmp = b""
            textBrowser.moveCursor(QTextCursor.End)
        else:
            tmp += b

if __name__ == "__main__":
    # Set High DPI
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QApplication(sys.argv)
    window = Window()

    # Table
    table: QTableWidget = window.table_devices

    def refresh_devices():
        device_info = adb_helper.get_devices_info()
        table.setRowCount(len(device_info))
        for i, (id, state, ro_debuggable) in enumerate(device_info):
            table.setItem(i, 0, QTableWidgetItem(id))
            table.setItem(i, 1, QTableWidgetItem(state))
            table.setItem(i, 2, QTableWidgetItem(ro_debuggable))

    refresh_Button: QPushButton = window.pushButton_refresh_device
    refresh_Button.clicked.connect(refresh_devices)
    refresh_devices()
    # Table End

    # Select Apk
    apk_selected = False
    openApk_Button: QPushButton = window.pushButton_open_apk
    openApk_Button.clicked.connect(on_open_apk)
    # Select Apk End

    # Apk install and uninstall Apk
    pushButton_adb_install: QPushButton = window.pushButton_adb_install
    pushButton_adb_install.clicked.connect(install_apk)
    pushButton_adb_uninstall: QPushButton = window.pushButton_adb_uninstall
    pushButton_adb_uninstall.clicked.connect(uninstall_apk)
    # Apk install and uninstall Apk End

    # IDA Version
    comboBox_IDA_V: QComboBox = window.comboBox_IDA_V
    comboBox_IDA_V.addItem(IDA.IDA_7_5.value)
    comboBox_IDA_V.addItem(IDA.IDA_8_3.value)
    comboBox_IDA_V.setCurrentIndex(1)
    # IDA Version End

    # IDA Click
    textBrowser_dbgsrv_output: QTextBrowser = window.textBrowser_dbgsrv_output

    pushButton_dbgsrv: QPushButton = window.pushButton_dbgsrv
    def on_click_dbgsrv():
        ida_version = comboBox_IDA_V.currentText()
        for stream in adb_helper.start_dbgsrv(ida_version + "_android_server64"):
            thread = threading.Thread(target=reading_stream, args=(stream,textBrowser_dbgsrv_output))
            thread.daemon = True # 设置为守护线程，当主线程结束时，守护线程也会结束
            thread.start()
            
    pushButton_dbgsrv.clicked.connect(on_click_dbgsrv)
    # IDA Click End

    # Startup
    # set_remote_debugger("127.0.0.1", "", 23946); attach_process(pid)
    textBrowser_logcat: QTextBrowser = window.textBrowser_logcat
    def on_click_startup():
        if not apk_selected:
            QMessageBox.warning(None, "警告", "No apk file selected")
            return
        
        for stream in adb_helper.start_debug_app(package, activity):
            thread = threading.Thread(target=reading_stream, args=(stream,textBrowser_logcat))
            thread.daemon = True
            thread.start()

    pushButton_start: QPushButton = window.pushButton_start
    pushButton_start.clicked.connect(on_click_startup)
    # Startup End

    window.show()
    sys.exit(app.exec_())