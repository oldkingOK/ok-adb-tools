from resource.ok_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from adb_helper import get_devices_info
from apk_helper import get_apk_info
import PyQt5.QtCore as QtCore

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def open_file_dialog():
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    file_name, _ = QFileDialog.getOpenFileName(None, "打开Apk文件", "", "Apk Files (*.apk)", options=options)
    if file_name:
        print(file_name)
    else:
        print("No file selected")

    global window

    package, activity = get_apk_info(file_name)
    label_package_name: QLabel = window.label_package_name
    label_package_name.setText(package)

    comboBox_open_apk: QComboBox = window.comboBox_open_apk
    comboBox_open_apk.addItem(file_name)
    

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QApplication(sys.argv)
    window = Window()

    # Table
    table: QTableWidget = window.table_devices

    def refresh_devices():
        device_info = get_devices_info()
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
    openApk_Button.clicked.connect(open_file_dialog)

    window.show()
    sys.exit(app.exec_())