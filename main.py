import sys
import psycopg2 as pg
import datetime
from PyQt5 import QtWidgets
from ui import Ui_MainWindow


def init_tb(tb):
    tb.setRowCount(1)
    tb.setColumnWidth(0, 130)
    tb.setColumnWidth(1, 125)
    tb.setColumnWidth(2, 440)


def get_text(path: str = None) -> str:
    with open(path) as inf:
        text = inf.read()
    return text


# def get_tb_data(tb):
#     tb_data = list()
#     num_rows, num_columns = tb.rowCount(), tb.columnCount()
#     for row in range(num_rows):
#         tb_data.append([])
#         for column in range(num_columns):
#             tb_data[row].append(tb.item(row, column))
#     return tb_data


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.d_tb = {'Земли сельзоз назначения': (self.ui.table_sx, self.ui.tab_sx),
                     'Земли промышленности': (self.ui.table_prom, self.ui.tab_prom),
                     'Земли населенных пунктов': (self.ui.table_nasel, self.ui.tab_nasel)}

    def init_ui(self):
        init_tb(self.ui.table_sx)
        init_tb(self.ui.table_prom)
        init_tb(self.ui.table_nasel)
        self.ui.pushButton.clicked.connect(self.get_scroll)

    def get_scroll(self):
        db_name = self.ui.comboBox.currentText()
        db.get_db_data(self.ui.dateEdit.text(),
                       db_name)
        li_data = db.cur.fetchall()
        self.clear_tb(self.d_tb[db_name][0])
        self.d_tb[db_name][0].setRowCount(len(li_data))
        self.d_tb[db_name][0].setColumnCount(len(li_data[0]))
        self.add_records(li_data, db_name)


    def add_records(self, li_data, db_name):
        for i, row in enumerate(li_data):
            for j, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col if not isinstance(col, datetime.date)
                                                      else col.strftime('%d.%m.%Y')))
                print(1)
                self.d_tb[db_name][0].setItem(i, j, item)

    def clear_tb(self, tb):
        [tb.removeRow(row) for row in sorted(range(tb.rowCount()), reverse=True)]


class DB:
    def __init__(self):
        self.con, self.cur = None, None
        self.cs_nasel = get_text(r'db/cs_nasel.txt')
        self.cs_prom_16_st = get_text(r'db/cs_prom_16_st.txt')
        self.cs_prom_24_st = get_text(r'db/cs_prom_24_st.txt')
        self.cs_sx_16_st = get_text(r'db/cs_sx_16_st.txt')
        self.cs_sx_24_st = get_text(r'db/cs_sx_24_st.txt')
        self.q_get_data = get_text(r'db/q_get_data.sql')
        self.d_css = {'Земли сельзоз назначения': (self.cs_sx_16_st, self.cs_sx_24_st),
                      'Земли промышленности': (self.cs_prom_16_st, self.cs_prom_24_st),
                      'Земли населенных пунктов': (self.cs_nasel,)}

    def get_db_data(self, date, db_name):
        cs = db.d_css[db_name][0]
        self.con = pg.connect(cs)
        self.cur = self.con.cursor()
        self.cur.execute(db.q_get_data, {'date': date})


app = QtWidgets.QApplication([])
db = DB()
application = App()
application.show()
sys.exit(app.exec())
