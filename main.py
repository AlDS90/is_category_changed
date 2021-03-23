import sys
import psycopg2 as pg
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


def get_text(path):
    with open(path) as inf:
        text = inf.read()
    return text


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.d_tb = {'Земли сельзоз назначения': (self.ui.table_sx, 0),
                     'Земли промышленности': (self.ui.table_prom, 1),
                     'Земли населенных пунктов': (self.ui.table_nasel, 2)}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Анализ категории')
        self.setWindowIcon(QIcon('ui_img/logo.png'))
        self.setFixedSize(self.size())
        [self.init_tb(key) for key in self.d_tb.keys()]
        self.ui.pushButton.clicked.connect(self.start_processing)

    def init_tb(self, key):
        tb = self.d_tb[key][0]
        self.add_one_row(key)
        tb.setColumnWidth(0, 120)
        tb.setColumnWidth(1, 80)
        tb.setColumnWidth(2, 125)
        tb.setColumnWidth(3, 80)
        tb.setColumnWidth(4, 80)
        tb.setColumnWidth(5, 210)
        tb.setColumnWidth(6, 190)

    def add_one_row(self, name_tb):
        tb = self.d_tb[name_tb][0]
        tb.setRowCount(1)
        for i in range(tb.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            tb.setItem(0, i, item)

    def start_processing(self):
        [self.clear_tb(key) for key in self.d_tb.keys()]
        if not self.get_scroll():
            date = self.ui.dateEdit.text()
            db.get_kn(self.ui.dateEdit.text(), self.ui.comboBox.currentText())
            kn = ','.join(['\'' + item[0] + '\'' for item in db.cur.fetchall()])
            db.close_con_cur()
            db_name_first, db_name_second = [key for key in self.d_tb.keys() if key != self.ui.comboBox.currentText()]
            db.get_db_data_by_kn(date, db_name_first, kn)
            change_object_first = db.cur.fetchall()
            if change_object_first:
                self.view_records(self.del_double(change_object_first), db_name_first)
            db.close_con_cur()
            db.get_db_data_by_kn(date, db_name_second, kn)
            change_object_second = db.cur.fetchall()
            if change_object_second:
                self.view_records(self.del_double(change_object_second), db_name_second)
            db.close_con_cur()

        [tb.setRowCount(tb.rowCount())
         if tb.rowCount() else tb.setRowCount(1)
         for tb, _ in self.d_tb.values()]

    def get_scroll(self):
        scroll_is_empty = False
        db_name = self.ui.comboBox.currentText()
        db.get_db_data(self.ui.dateEdit.text(), db_name)
        li_data = db.cur.fetchall()
        if li_data:
            self.view_records(li_data, db_name)
            db.close_con_cur()
        else:
            scroll_is_empty = True
            db.close_con_cur()
        self.ui.tabWidget.setCurrentIndex(self.d_tb[db_name][1])
        return scroll_is_empty

    def view_records(self, li_data, db_name):
        tb = self.d_tb[db_name][0]
        for row in li_data:
            tb.insertRow(tb.rowCount())
            for i, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col if not isinstance(col, datetime.date)
                                                      else col.strftime('%d.%m.%Y')))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                tb.setItem(tb.rowCount() - 1, i, item)

    def del_double(self, list_):
        list_edit = []
        for i, item in enumerate([item[0] for item in list_]):
            if item not in [item[0] if isinstance(item, tuple) else item
                            for item in list_edit]:
                list_edit.append(list_[i])
        return list_edit

    def clear_tb(self, db_name):
        tb = self.d_tb[db_name][0]
        [tb.removeRow(row) for row in sorted(range(tb.rowCount()), reverse=True)]


class DB:
    def __init__(self):
        self.con, self.cur = None, None
        self.cs_nasel = get_text(r'db/cs_nasel.txt')
        self.cs_prom_16_st = get_text(r'db/cs_prom_16_st.txt')
        self.cs_sx_16_st = get_text(r'db/cs_sx_16_st.txt')
        self.q_get_data = get_text(r'db/q_get_data.sql')
        self.q_get_data_by_kn = get_text(r'db/q_get_data_by_kn.sql')
        self.q_get_kn = get_text(r'db/q_get_kn.sql')
        self.d_css = {'Земли сельзоз назначения': self.cs_sx_16_st,
                      'Земли промышленности': self.cs_prom_16_st,
                      'Земли населенных пунктов': self.cs_nasel}

    def get_db_data(self, date, db_name):
        cs = self.d_css[db_name]
        self.con = pg.connect(cs)
        self.cur = self.con.cursor()
        self.cur.execute(self.q_get_data, {'date': date})

    def get_db_data_by_kn(self, date, db_name, kn):
        cs = self.d_css[db_name]
        self.con = pg.connect(cs)
        self.cur = self.con.cursor()
        self.cur.execute(self.q_get_data_by_kn.replace('%(kn)s', kn), {'date': date})

    def get_kn(self, date, db_name):
        cs = self.d_css[db_name]
        self.con = pg.connect(cs)
        self.cur = self.con.cursor()
        self.cur.execute(self.q_get_kn, {'date': date})

    def close_con_cur(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    db = DB()
    application = App()
    application.show()
    sys.exit(app.exec())
