# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 431, 55))
        self.groupBox.setObjectName("groupBox")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(10, 20, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 910, 546))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sx = QtWidgets.QWidget()
        self.tab_sx.setObjectName("tab_sx")
        self.table_sx = QtWidgets.QTableWidget(self.tab_sx)
        self.table_sx.setGeometry(QtCore.QRect(0, 0, 904, 520))
        self.table_sx.setStyleSheet("")
        self.table_sx.setLineWidth(1)
        self.table_sx.setObjectName("table_sx")
        self.table_sx.setColumnCount(7)
        self.table_sx.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(6, item)
        self.tabWidget.addTab(self.tab_sx, "")
        self.tab_prom = QtWidgets.QWidget()
        self.tab_prom.setObjectName("tab_prom")
        self.table_prom = QtWidgets.QTableWidget(self.tab_prom)
        self.table_prom.setGeometry(QtCore.QRect(0, 0, 904, 521))
        self.table_prom.setStyleSheet("")
        self.table_prom.setLineWidth(1)
        self.table_prom.setObjectName("table_prom")
        self.table_prom.setColumnCount(7)
        self.table_prom.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(6, item)
        self.tabWidget.addTab(self.tab_prom, "")
        self.tab_nasel = QtWidgets.QWidget()
        self.tab_nasel.setObjectName("tab_nasel")
        self.table_nasel = QtWidgets.QTableWidget(self.tab_nasel)
        self.table_nasel.setGeometry(QtCore.QRect(0, 0, 904, 521))
        self.table_nasel.setStyleSheet("")
        self.table_nasel.setLineWidth(1)
        self.table_nasel.setObjectName("table_nasel")
        self.table_nasel.setColumnCount(7)
        self.table_nasel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(6, item)
        self.tabWidget.addTab(self.tab_nasel, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Поиск"))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Земли сельзоз назначения"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Земли промышленности"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Земли населенных пунктов"))
        item = self.table_sx.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_sx.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_sx.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_sx.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_sx.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_sx.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_sx.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sx), _translate("MainWindow", "Земли сельзоз назначения"))
        item = self.table_prom.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_prom.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_prom.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_prom.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_prom.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_prom.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_prom.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prom), _translate("MainWindow", "Земли промышленности"))
        item = self.table_nasel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_nasel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_nasel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_nasel.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_nasel.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_nasel.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_nasel.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nasel), _translate("MainWindow", "Земли населенных пунктов"))
