import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from splashScreen import Ui_SplashScreen
from main import MainWindow


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = 0

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # TIMER
        self.timer.start(35)

        # CHANGE TEXT DESCRIPTION
        QtCore.QTimer.singleShot(500, lambda: self.ui.description.setText("<strong>LOADING </strong>DATABASE"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.description.setText("<strong>LOADING </strong>USER INTERFACE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.description.setText("<strong>LOADING </strong>OPTIMIZING CODE"))

    def progress(self):
        """THIS METHODS WILL TRIGGER THE PROGRESS BAR
           THEN EVENTUALLY RUN THE MAIN PROGRAM
        """

        self.ui.progressBar.setValue(self.counter)
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # Main Program
            self.main = MainWindow()
            self.main.show()

            # Close Splash Screen
            self.close()
        self.counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = SplashScreen()
    screen.show()
    sys.exit(app.exec_())