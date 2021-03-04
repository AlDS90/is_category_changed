import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        pass


app = QtWidgets.QApplication([])
application = App()
application.show()
sys.exit(app.exec())
