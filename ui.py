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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sx = QtWidgets.QWidget()
        self.tab_sx.setObjectName("tab_sx")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_sx)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_sx = QtWidgets.QTableWidget(self.tab_sx)
        self.table_sx.setObjectName("table_sx")
        self.table_sx.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sx.setHorizontalHeaderItem(9, item)
        self.verticalLayout_3.addWidget(self.table_sx)
        self.tabWidget.addTab(self.tab_sx, "")
        self.tab_prom = QtWidgets.QWidget()
        self.tab_prom.setObjectName("tab_prom")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_prom)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table_prom = QtWidgets.QTableWidget(self.tab_prom)
        self.table_prom.setObjectName("table_prom")
        self.table_prom.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prom.setHorizontalHeaderItem(9, item)
        self.verticalLayout_4.addWidget(self.table_prom)
        self.tabWidget.addTab(self.tab_prom, "")
        self.tab_nasel = QtWidgets.QWidget()
        self.tab_nasel.setObjectName("tab_nasel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_nasel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table_nasel = QtWidgets.QTableWidget(self.tab_nasel)
        self.table_nasel.setObjectName("table_nasel")
        self.table_nasel.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_nasel.setHorizontalHeaderItem(9, item)
        self.verticalLayout_5.addWidget(self.table_nasel)
        self.tabWidget.addTab(self.tab_nasel, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.btn_find = QtWidgets.QPushButton(self.groupBox)
        self.btn_find.setObjectName("btn_find")
        self.verticalLayout.addWidget(self.btn_find)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.ll_date = QtWidgets.QLabel(self.groupBox_2)
        self.ll_date.setText("")
        self.ll_date.setObjectName("ll_date")
        self.gridLayout.addWidget(self.ll_date, 0, 2, 1, 1)
        self.ll_name_db = QtWidgets.QLabel(self.groupBox_2)
        self.ll_name_db.setText("")
        self.ll_name_db.setObjectName("ll_name_db")
        self.gridLayout.addWidget(self.ll_name_db, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btn_unload = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_unload.setObjectName("btn_unload")
        self.gridLayout.addWidget(self.btn_unload, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_sx.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_sx.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_sx.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сегмент"))
        item = self.table_sx.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Код расчета"))
        item = self.table_sx.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Код ВРИ"))
        item = self.table_sx.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_sx.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_sx.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_sx.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_sx.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sx), _translate("MainWindow", "Земли сельзоз назначения"))
        item = self.table_prom.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_prom.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_prom.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сегмент"))
        item = self.table_prom.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Код расчета"))
        item = self.table_prom.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Код ВРИ"))
        item = self.table_prom.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_prom.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_prom.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_prom.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_prom.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prom), _translate("MainWindow", "Земли промышленности"))
        item = self.table_nasel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "КН"))
        item = self.table_nasel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "КК"))
        item = self.table_nasel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сегмент"))
        item = self.table_nasel.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Код расчета"))
        item = self.table_nasel.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Код ВРИ"))
        item = self.table_nasel.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Описание перечня"))
        item = self.table_nasel.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_nasel.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Площадь"))
        item = self.table_nasel.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Вид использования по документам"))
        item = self.table_nasel.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Неформализованное описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nasel), _translate("MainWindow", "Земли населенных пунктов"))
        self.groupBox.setTitle(_translate("MainWindow", "Поиск"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Земли сельзоз назначения"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Земли промышленности"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Земли населенных пунктов"))
        self.btn_find.setText(_translate("MainWindow", "Найти"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выгрузить"))
        self.label_2.setText(_translate("MainWindow", "Имя базы:"))
        self.btn_unload.setText(_translate("MainWindow", "Старт"))
        self.label.setText(_translate("MainWindow", "Дата:"))
