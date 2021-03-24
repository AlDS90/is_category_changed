import sys
import psycopg2 as pg
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


def get_text(path: str) -> str:
    with open(path) as inf:
        text = inf.read()
    return text


def del_double(li: list) -> list:
    li_edit = []
    for i, item in enumerate([item[0] for item in li]):
        if item not in [item[0] if isinstance(item, tuple) else item
                        for item in li_edit]:
            li_edit.append(li[i])
    return li_edit


def get_s_kns(li_kns: list) -> str:
    return ','.join(['\'' + item[0] + '\'' for item in li_kns])


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
        self.ui.pushButton.clicked.connect(self.start_analyze)

    def init_tb(self, key: str):
        tb = self.d_tb[key][0]
        self.add_one_row(key)
        tb.setColumnWidth(0, 120)
        tb.setColumnWidth(1, 80)
        tb.setColumnWidth(2, 125)
        tb.setColumnWidth(3, 80)
        tb.setColumnWidth(4, 80)
        tb.setColumnWidth(5, 210)
        tb.setColumnWidth(6, 190)

    def add_one_row(self, name_tb: str):
        tb = self.d_tb[name_tb][0]
        if not tb.rowCount():
            tb.setRowCount(1)
            for i in range(tb.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                tb.setItem(0, i, item)

    def start_analyze(self):
        [self.clear_tb(key) for key in self.d_tb.keys()]
        date = self.ui.dateEdit.text()
        db_name_main = self.ui.comboBox.currentText()
        self.ui.tabWidget.setCurrentIndex(self.d_tb[db_name_main][1])
        db_name_first, db_name_second = [key for key in self.d_tb.keys() if key != db_name_main]
        li_kns_main_db = db.get_data(date, db_name_main, db.q_get_kns)
        if li_kns_main_db:
            li_data_first_db = del_double(db.get_data(date, db_name_first, db.q_get_data_by_kn,
                                                      get_s_kns(li_kns_main_db)))
            li_data_second_db = del_double(db.get_data(date, db_name_second, db.q_get_data_by_kn,
                                                       get_s_kns(li_kns_main_db)))
            li_kns_union: list = []
            li_kns_union.extend([(item[0],) for item in li_data_first_db])
            li_kns_union.extend([(item[0],) for item in li_data_second_db])
            if li_kns_union:
                li_data_main_db = db.get_data(date, db_name_main, db.q_get_data_by_kn,
                                              get_s_kns(li_kns_union))
                for data, db_name in [(li_data_main_db, db_name_main),
                                      (li_data_first_db, db_name_first),
                                      (li_data_second_db, db_name_second)]:
                    if data:
                        self.display_records(data, db_name)
        [self.add_one_row(key) for key in self.d_tb.keys()]
        # for tb, _ in self.d_tb.values():
        #     tb.nam
        # [tb.setRowCount(tb.rowCount())
        #  if tb.rowCount() else tb.setRowCount(1)
        #  for tb, _ in self.d_tb.values()]

        # print(li_kns_main_db)
        # print(li_kns_first_db)
        # print(li_kns_second_db)
        # li_kns = self.get_kns()
        # db.close_con_cur()
        # if li_kns:
        #     date = self.ui.dateEdit.text()
        #     db_name_first, db_name_second = [key for key in self.d_tb.keys() if key != self.ui.comboBox.currentText()]
        #     s_kns = ','.join(['\'' + item[0] + '\'' for item in li_kns])
        #     db.get_db_data_by_kn(date, db_name_first, s_kns)
        #     db.close_con_cur()
        #     change_objects = db.cur.fetchall()
        #     if change_objects:
        #         self.view_records(self.del_double(change_objects), db_name_first)

        # if not self.get_scroll():
        #     date = self.ui.dateEdit.text()
        #     db.get_li_kns(self.ui.dateEdit.text(), self.ui.comboBox.currentText())
        #     kn = ','.join(['\'' + item[0] + '\'' for item in db.cur.fetchall()])
        #     db.close_con_cur()
        #     db_name_first, db_name_second = [key for key in self.d_tb.keys() if key != self.ui.comboBox.currentText()]
        #     db.get_db_data_by_kn(date, db_name_first, kn)
        #     change_object_first = db.cur.fetchall()
        #     if change_object_first:
        #         self.view_records(self.del_double(change_object_first), db_name_first)
        #     db.close_con_cur()
        #     db.get_db_data_by_kn(date, db_name_second, kn)
        #     change_object_second = db.cur.fetchall()
        #     if change_object_second:
        #         self.view_records(self.del_double(change_object_second), db_name_second)
        #     db.close_con_cur()
        #
        # [tb.setRowCount(tb.rowCount())
        #  if tb.rowCount() else tb.setRowCount(1)
        #  for tb, _ in self.d_tb.values()]

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

    def display_records(self, li_data, db_name):
        tb = self.d_tb[db_name][0]
        for row in li_data:
            tb.insertRow(tb.rowCount())
            for i, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col if not isinstance(col, datetime.date)
                                                      else col.strftime('%d.%m.%Y')))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                tb.setItem(tb.rowCount() - 1, i, item)

    def clear_tb(self, db_name):
        tb = self.d_tb[db_name][0]
        [tb.removeRow(row) for row in sorted(range(tb.rowCount()), reverse=True)]


class DB:
    def __init__(self):
        self.con, self.cur = None, None

        self.cs_sx_16_st = get_text(r'db/cs_sx_16_st.txt')
        self.cs_prom_16_st = get_text(r'db/cs_prom_16_st.txt')
        self.cs_nasel = get_text(r'db/cs_nasel.txt')
        self.d_css = {'Земли сельзоз назначения': self.cs_sx_16_st,
                      'Земли промышленности': self.cs_prom_16_st,
                      'Земли населенных пунктов': self.cs_nasel}

        self.q_get_data = get_text(r'db/q_get_data.sql')
        self.q_get_data_by_kn = get_text(r'db/q_get_data_by_kn.sql')
        self.q_get_kns = get_text(r'db/q_get_kns.sql')

    def get_data(self, date: str, db_name: str, query: str, kns: str = None) -> list:
        cs = self.d_css[db_name]
        with pg.connect(cs) as self.con:
            with self.con.cursor() as self.cur:
                if kns:
                    self.cur.execute(query.replace('%(kns)s', kns), {'date': date})
                else:
                    self.cur.execute(query, {'date': date})
                li = self.cur.fetchall()
        self.con.close()
        return li


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    db = DB()
    application = App()
    application.show()
    sys.exit(app.exec())
