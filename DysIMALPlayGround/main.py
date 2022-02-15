from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class Main(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        # uic.loadUi("main.ui", self)
        # self.actionsave_and_exit.triggered.connect(sys.exit)
        # self.actionexit.triggered.connect(sys.exit)
        self.studentDialogForm()    

    def studentDialogForm(self):
        uic.loadUi("studentForm.ui", self)

    def secondWindowForm(self):
        uic.loadUi("secondWindow.ui", self)


app = QApplication(sys.argv)
screen = Main()
screen.show()
sys.exit(app.exec())
