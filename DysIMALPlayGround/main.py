from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("main.ui", self)
        self.actionsave_and_exit.triggered.connect(sys.exit)
        self.actionexit.triggered.connect(sys.exit)


app = QApplication(sys.argv)
screen = Main()
screen.show()
sys.exit(app.exec())
