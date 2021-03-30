import sys
import psycopg2 as pg
import datetime
import pandas as pd
import os
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
        self.main_dir = r'\\192.168.1.40\All\Сотниченко А.Д\programs\is_category_changed'
        self.date, self.db_name_main, self.db_name_first, self.db_name_second = '', '', '', ''
        self.li_data_main_db, self.li_data_first_db, self.li_data_second_db = [], [], []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.d_tb = {'Земли сельзоз назначения': (self.ui.table_sx, 0),
                     'Земли промышленности': (self.ui.table_prom, 1),
                     'Земли населенных пунктов': (self.ui.table_nasel, 2)}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Анализ категории')
        self.setWindowIcon(QIcon('ui_img/logo.png'))
        [self.init_tb(key) for key in self.d_tb.keys()]
        self.ui.pushButton.clicked.connect(self.start_analyze)
        self.ui.pushButton_2.clicked.connect(self.unload_to_excel)

    def init_tb(self, key: str):
        tb = self.d_tb[key][0]
        [tb.setColumnWidth(i, width) for i, width in enumerate((120, 80, 60, 75, 55,
                                                                125, 80, 80, 210, 190))]
        self.add_one_row(key)

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
        [data.clear() for data in [self.li_data_main_db, self.li_data_first_db, self.li_data_second_db]]
        self.date = self.ui.dateEdit.text()
        self.db_name_main = self.ui.comboBox.currentText()
        self.ui.tabWidget.setCurrentIndex(self.d_tb[self.db_name_main][1])
        self.db_name_first, self.db_name_second = [key for key in self.d_tb.keys() if key != self.db_name_main]
        li_kns_main_db = db.get_data(self.date, self.db_name_main, db.q_get_kns)
        if li_kns_main_db:
            self.li_data_first_db = del_double(db.get_data(self.date, self.db_name_first,
                                                           db.q_get_data_first_and_second_dbs,
                                                           get_s_kns(li_kns_main_db)))
            self.li_data_second_db = del_double(db.get_data(self.date, self.db_name_second,
                                                            db.q_get_data_first_and_second_dbs,
                                                            get_s_kns(li_kns_main_db)))
            li_kns_union = []
            li_kns_union.extend([(item[0],) for item in self.li_data_first_db])
            li_kns_union.extend([(item[0],) for item in self.li_data_second_db])
            if li_kns_union:
                self.li_data_main_db = db.get_data(self.date, self.db_name_main, db.q_get_data_main_db,
                                                   get_s_kns(li_kns_union))
                for data, db_name in [(self.li_data_main_db, self.db_name_main),
                                      (self.li_data_first_db, self.db_name_first),
                                      (self.li_data_second_db, self.db_name_second)]:
                    if data:
                        self.display_records(data, db_name)
        [self.add_one_row(key) for key in self.d_tb.keys()]

    def unload_to_excel(self):
        if self.db_name_main and \
           self.db_name_first and \
           self.db_name_second:
            file_name = '{}_{}_{}_analyze_doc.xlsx'.format(datetime.datetime.now().strftime('%d%m%Y_%H%M%S%f'),
                                                           self.date,
                                                           self.db_name_main)
            li_name_col = tuple([(self.ui.table_sx.horizontalHeaderItem(j).text(), j)
                                 for j in range(self.ui.table_sx.columnCount())])

            df_main_db = pd.DataFrame({name: [row[col] for row in self.li_data_main_db]
                                       for name, col in li_name_col})
            df_first_db = pd.DataFrame({name: [row[col] for row in self.li_data_first_db]
                                        for name, col in li_name_col})
            df_second_db = pd.DataFrame({name: [row[col] for row in self.li_data_second_db]
                                         for name, col in li_name_col})
            d_data_shs = {self.db_name_main: df_main_db,
                          self.db_name_first: df_first_db,
                          self.db_name_second: df_second_db}
            writer = pd.ExcelWriter(self.main_dir + os.sep + file_name, engine='xlsxwriter')
            [d_data_shs[sh_name].to_excel(writer, sheet_name=sh_name, index=False)
             for sh_name in d_data_shs.keys()]
            writer.save()

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

        self.q_get_data_main_db = get_text(r'db/q_get_data_main_db.sql')
        self.q_get_data_first_and_second_dbs = get_text(r'db/q_get_data_first_and_second_dbs.sql')
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
