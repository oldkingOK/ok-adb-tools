from resource.ok_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from apk_helper import get_apk_info
import PyQt5.QtCore as QtCore
import adb_helper

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

    global window

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
    openApk_Button: QPushButton = window.pushButton_open_apk
    openApk_Button.clicked.connect(on_open_apk)
    # Select Apk End

    # Apk install and uninstall Apk
    pushButton_adb_install: QPushButton = window.pushButton_adb_install
    pushButton_adb_install.clicked.connect(install_apk)
    pushButton_adb_uninstall: QPushButton = window.pushButton_adb_uninstall
    pushButton_adb_uninstall.clicked.connect(uninstall_apk)
    # Apk install and uninstall Apk End

    window.show()
    sys.exit(app.exec_())