from resource.ok_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from adb_helper import get_devices_info
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

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QApplication(sys.argv)
    window = Window()

    # Table
    table: QTableWidget = window.table_devices
    device_info = get_devices_info()

    for id, state, ro_debuggable in device_info:
        row = table.rowCount()
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(id))
        table.setItem(row, 1, QTableWidgetItem(state))
        table.setItem(row, 2, QTableWidgetItem(ro_debuggable))

    # Table End

    openApk_Button: QPushButton = window.pushButton_open_apk
    openApk_Button.clicked.connect(open_file_dialog)

    window.show()
    sys.exit(app.exec_())