# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ok-adb-tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_devices = QtWidgets.QTableWidget(self.centralwidget)
        self.table_devices.setGeometry(QtCore.QRect(10, 30, 421, 221))
        self.table_devices.setObjectName("table_devices")
        self.table_devices.setColumnCount(4)
        self.table_devices.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_devices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_devices.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_devices.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_devices.setHorizontalHeaderItem(3, item)
        self.comboBox_open_apk = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_open_apk.setGeometry(QtCore.QRect(450, 30, 441, 31))
        self.comboBox_open_apk.setObjectName("comboBox_open_apk")
        self.pushButton_open_apk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_apk.setGeometry(QtCore.QRect(850, 70, 41, 31))
        self.pushButton_open_apk.setObjectName("pushButton_open_apk")
        self.pushButton_adb_install = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_adb_install.setGeometry(QtCore.QRect(780, 70, 61, 31))
        self.pushButton_adb_install.setObjectName("pushButton_adb_install")
        self.label_package_name = QtWidgets.QLabel(self.centralwidget)
        self.label_package_name.setGeometry(QtCore.QRect(450, 70, 191, 31))
        self.label_package_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_package_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_package_name.setObjectName("label_package_name")
        self.comboBox_IDA_V = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_IDA_V.setGeometry(QtCore.QRect(450, 170, 71, 31))
        self.comboBox_IDA_V.setObjectName("comboBox_IDA_V")
        self.pushButton_dbgsrv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dbgsrv.setGeometry(QtCore.QRect(530, 170, 91, 31))
        self.pushButton_dbgsrv.setObjectName("pushButton_dbgsrv")
        self.textBrowser_dbgsrv_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_dbgsrv_output.setGeometry(QtCore.QRect(10, 280, 421, 151))
        self.textBrowser_dbgsrv_output.setObjectName("textBrowser_dbgsrv_output")
        self.label_IDA_output = QtWidgets.QLabel(self.centralwidget)
        self.label_IDA_output.setGeometry(QtCore.QRect(10, 260, 131, 16))
        self.label_IDA_output.setObjectName("label_IDA_output")
        self.label_jdbc_output = QtWidgets.QLabel(self.centralwidget)
        self.label_jdbc_output.setGeometry(QtCore.QRect(10, 440, 81, 16))
        self.label_jdbc_output.setObjectName("label_jdbc_output")
        self.textBrowser_jdbc_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_jdbc_output.setGeometry(QtCore.QRect(10, 460, 421, 141))
        self.textBrowser_jdbc_output.setObjectName("textBrowser_jdbc_output")
        self.label_logcat = QtWidgets.QLabel(self.centralwidget)
        self.label_logcat.setGeometry(QtCore.QRect(450, 260, 131, 16))
        self.label_logcat.setObjectName("label_logcat")
        self.textBrowser_logcat = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_logcat.setGeometry(QtCore.QRect(450, 280, 441, 321))
        self.textBrowser_logcat.setObjectName("textBrowser_logcat")
        self.label_DeviceInfo = QtWidgets.QLabel(self.centralwidget)
        self.label_DeviceInfo.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_DeviceInfo.setObjectName("label_DeviceInfo")
        self.plainTextEdit_idapython = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_idapython.setGeometry(QtCore.QRect(450, 130, 341, 31))
        self.plainTextEdit_idapython.setReadOnly(True)
        self.plainTextEdit_idapython.setObjectName("plainTextEdit_idapython")
        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(800, 130, 41, 31))
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(850, 130, 41, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_tip = QtWidgets.QLabel(self.centralwidget)
        self.label_tip.setGeometry(QtCore.QRect(650, 160, 241, 21))
        self.label_tip.setObjectName("label_tip")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(850, 260, 41, 21))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(800, 260, 41, 21))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_refresh_device = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh_device.setGeometry(QtCore.QRect(90, 10, 41, 21))
        self.pushButton_refresh_device.setObjectName("pushButton_refresh_device")
        self.pushButton_adb_uninstall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_adb_uninstall.setGeometry(QtCore.QRect(710, 70, 61, 31))
        self.pushButton_adb_uninstall.setObjectName("pushButton_adb_uninstall")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 22))
        self.menubar.setObjectName("menubar")
        self.menuOk_Adbtools = QtWidgets.QMenu(self.menubar)
        self.menuOk_Adbtools.setObjectName("menuOk_Adbtools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOk_Adbtools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ok adbtools"))
        item = self.table_devices.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "设备"))
        item = self.table_devices.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "状态"))
        item = self.table_devices.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ro.debuggable"))
        item = self.table_devices.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "App pid"))
        self.pushButton_open_apk.setText(_translate("MainWindow", "打开"))
        self.pushButton_adb_install.setText(_translate("MainWindow", "安装apk"))
        self.label_package_name.setText(_translate("MainWindow", "包名"))
        self.pushButton_dbgsrv.setText(_translate("MainWindow", "运行 dbgsrv"))
        self.label_IDA_output.setText(_translate("MainWindow", "IDA dbgsrv output"))
        self.label_jdbc_output.setText(_translate("MainWindow", "jdbc output"))
        self.label_logcat.setText(_translate("MainWindow", "Logcat output"))
        self.label_DeviceInfo.setText(_translate("MainWindow", "Device Info"))
        self.pushButton_copy.setText(_translate("MainWindow", "复制"))
        self.pushButton_start.setText(_translate("MainWindow", "启动"))
        self.label_tip.setText(_translate("MainWindow", "点击启动之后，使用ida连接，再点一次启动"))
        self.pushButton_save.setText(_translate("MainWindow", "保存"))
        self.pushButton_clear.setText(_translate("MainWindow", "清除"))
        self.pushButton_refresh_device.setText(_translate("MainWindow", "刷新"))
        self.pushButton_adb_uninstall.setText(_translate("MainWindow", "卸载apk"))
        self.menuOk_Adbtools.setTitle(_translate("MainWindow", "Ok Adbtools"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
