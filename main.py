from resource.ok_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from apk_helper import get_apk_info
from constants import IDA
from datetime import datetime
import PyQt5.QtCore as QtCore
import adb_helper
import threading
import time

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
    adb_helper.install_apk(get_device_index(), text)
    
def uninstall_apk():
    label_package_name: QLabel = window.label_package_name
    text = label_package_name.text()
    if text == "包名":
        QMessageBox.warning(None, "警告", "No file selected")
        return
    adb_helper.uninstall_apk(get_device_index(), text)


def reading_stream(stream, textBrowser, encoding="utf-8"):
    """
    读取流并将其显示在textBrowser中
    由于读取流的时候，换行符是\r\n, 所以需要将\r和\n替换为空
    注: 
    1. append会自动加一个换行符
    2. 必须time.sleep, 过快添加内容会崩溃
    """
    tmp = b""
    while True:
        try:
            b = stream.read(1)
            if b == b"": continue
        except Exception as e:
            break
        if b == b"\r":
            # textBrowser_logcat.textCursor().insertText(tmp.decode(encoding))
            # textBrowser.cursorText()
            textBrowser.append(tmp.decode(encoding))
            textBrowser.moveCursor(QTextCursor.End)
            time.sleep(0.01)
            tmp = b""
        elif b == b"\n":
            pass
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

    def get_device_index():
        return table.currentRow()

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
        stream = adb_helper.start_dbgsrv(get_device_index(), ida_version + "_android_server64")
        thread = threading.Thread(target=reading_stream, args=(stream,textBrowser_dbgsrv_output))
        thread.daemon = True # 设置为守护线程，当主线程结束时，守护线程也会结束
        thread.start()
            
    pushButton_dbgsrv.clicked.connect(on_click_dbgsrv)
    # IDA Click End

    # Startup
    textBrowser_logcat: QTextBrowser = window.textBrowser_logcat
    plainTextEdit_idapython: QPlainTextEdit = window.plainTextEdit_idapython
    checkBox_auto_clear: QCheckBox = window.checkBox_auto_clear

    def on_click_startup():
        if not apk_selected:
            QMessageBox.warning(None, "警告", "No apk file selected")
            return
        
        if checkBox_auto_clear.isChecked():
            textBrowser_logcat.clear()
        
        global pid
        pid, stream = adb_helper.start_debug_app(get_device_index(), package, activity)
        plainTextEdit_idapython.setPlainText(f'set_remote_debugger("127.0.0.1", "", 23946); attach_process({pid})')
        thread = threading.Thread(target=reading_stream, args=(stream,textBrowser_logcat))
        thread.daemon = True
        thread.start()

        table.setItem(get_device_index(), 3, QTableWidgetItem(str(pid)))

    pushButton_start: QPushButton = window.pushButton_start
    pushButton_start.clicked.connect(on_click_startup)
    # Startup End

    # Continue
    from jdbc_helper import start_jdbc
    pushButton_continue: QPushButton = window.pushButton_continue
    textBrowser_jdbc_output: QTextBrowser = window.textBrowser_jdbc_output
    def on_click_continue():
        if not globals().get("pid"):
            QMessageBox.warning(None, "警告", "No pid found")
            return

        stdout, stderr = start_jdbc(get_device_index(), pid)
        thread1 = threading.Thread(target=reading_stream, args=(stdout,textBrowser_jdbc_output, "gbk"))
        thread2 = threading.Thread(target=reading_stream, args=(stderr,textBrowser_jdbc_output, "gbk"))
        thread1.daemon = True
        thread2.daemon = True
        thread1.start()
        thread2.start()
        
    
    pushButton_continue.clicked.connect(on_click_continue)
    # Continue End

    # Copy
    pushButton_copy: QPushButton = window.pushButton_copy
    pushButton_copy.clicked.connect(lambda: QApplication.clipboard().setText(plainTextEdit_idapython.toPlainText()))
    pushButton_copy_logcat: QPushButton = window.pushButton_copy_logcat
    pushButton_copy_logcat.clicked.connect(lambda: QApplication.clipboard().setText(textBrowser_logcat.toPlainText()))
    # Copy End

    # Clear Logcat
    pushButton_clear: QPushButton = window.pushButton_clear
    pushButton_clear.clicked.connect(lambda: textBrowser_logcat.clear())
    # Clear Logcat End

    # Save Logcat
    pushButton_save: QPushButton = window.pushButton_save
    def on_click_save():
        options = QFileDialog.Options()
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name, _ = QFileDialog.getSaveFileName(None, "Save Logcat", f"logcat_{current_time}.log", "Log Files (*.log)", options=options)
        if file_name:
            with open(file_name, "w") as f:
                f.write(textBrowser_logcat.toPlainText())
        else:
            print("No file selected")
    pushButton_save.clicked.connect(on_click_save)
    # Save Logcat End

    window.show()
    sys.exit(app.exec_())