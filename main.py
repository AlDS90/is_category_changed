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


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.con, self.cur = None, None

        self.clear_tb()
        print(self.get_tb_data())
        self.init_ui()

    def init_ui(self):
        init_tb(self.ui.tableWidget)
        init_tb(self.ui.tableWidget_2)
        init_tb(self.ui.tableWidget_3)
        self.ui.pushButton.clicked.connect(self.get_db_data)

    def get_db_data(self):
        date = self.ui.dateEdit.text()
        cs = db.d_cs[self.ui.comboBox.currentText()]

        self.con = pg.connect(cs)
        self.cur = self.con.cursor()
        self.cur.execute(db.q_get_data, {'date': date})
        self.clear_tb()
        li_data = self.cur.fetchall()
        self.ui.tableWidget.setRowCount(len(li_data))
        self.ui.tableWidget.setColumnCount(len(li_data[0]))
        for i, row in enumerate(li_data):
            for j, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col if not isinstance(col, datetime.date)
                                                      else col.strftime('%d.%m.%Y')))
                self.ui.tableWidget.setItem(i, j, item)

    def clear_tb(self):
        tb = self.ui.tableWidget
        for row in sorted(range(tb.rowCount()), reverse=True):
            tb.removeRow(row)

    def get_tb_data(self):
        tb = self.ui.tableWidget
        tb_data = list()
        num_rows, num_columns = tb.rowCount(), tb.columnCount()
        for row in range(num_rows):
            tb_data.append([])
            for column in range(num_columns):
                tb_data[row].append(tb.item(row, column).text())
        return tb_data


class DB:
    def __init__(self):
        self.cs_nasel = get_text(r'db/cs_nasel.txt')
        self.cs_prom_16_st = get_text(r'db/cs_prom_16_st.txt')
        self.cs_prom_24_st = get_text(r'db/cs_prom_24_st.txt')
        self.cs_sx_16_st = get_text(r'db/cs_sx_16_st.txt')
        self.cs_sx_24_st = get_text(r'db/cs_sx_24_st.txt')
        self.q_get_data = get_text(r'db/q_get_data.sql')
        self.d_cs = {'Земли сельзоз назначения': (self.cs_sx_16_st, self.cs_sx_24_st),
                     'Земли промышленности': (self.cs_prom_16_st, self.cs_prom_24_st),
                     'Земли населенных пунктов': self.cs_nasel}


app = QtWidgets.QApplication([])
db = DB()
application = App()
application.show()
sys.exit(app.exec())
