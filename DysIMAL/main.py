# DysIMAL

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("MainForm")
        self.setWindowIcon(QIcon(".\Images\windowIcon.png"))
        self.setFixedSize(800, 480)
        self.create_button()

    def background_init(self):
        image = QPixmap()
        image.load(".\Imager\background2.jpg")
        image = image.scaled(self.width(), self.height())

        pallete = QPalette()
        pallete.setBrush(self.backgroundRole(), QBrush(image))
        self.setPalett (pallete)

    def create_button(self):
        btn = QPushButton('TAKE TEST', self)
        btn.setGeometry(50, 50, 200, 100)
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec())
