# IMPORTING ESSENTIALS
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip
from ApplicationUI import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # methods calling
        self.settingUp_mainWindow()
        self.stackWidgets_behavior()
        self.slideLeftMenu_trigger()

    def settingUp_mainWindow(self):
        """This methods is resposible for setting and removing the necessary in the MainWindow"""

        # Removing the window title bar (since we're using custom layout)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Setting the main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Applying Shadow Style Effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setYOffset(0)
        shadow.setXOffset(0)
        shadow.setColor(QColor(0, 92, 157, 550))
        # Applying the shadow style to the central widgets
        self.ui.centralwidget.setGraphicsEffect(shadow)
        self.setWindowTitle("DysIMAL")

        # Using this line it will resize the whole window
        QSizeGrip(self.ui.sizeGrip)

        # Windows Behavior (close, minimize, restore)
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.restoreBtn.clicked.connect(lambda: self.restore_or_maximize_window())

    def stackWidgets_behavior(self):
        """This methods is responsible for navigating the stack widgets."""
        self.ui.studentProfileBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.studentProfilePage))
        self.ui.examBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.examPage))
        self.ui.recordsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.recordsPage))
        self.ui.devsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.DevtPage))

    def slideLeftMenu(self):
        """This Methods is responsible for animating the left menu frame"""
        width = self.ui.leftMenu.width()
        if width == 40:
            # Expand the width by giving the new Width
            newWidth = 220
        else:
            newWidth = 40
        animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
        animation.setDuration(250)
        animation.setStartValue(width)
        animation.setEndValue(newWidth)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        animation.start()

    def slideLeftMenu_trigger(self):
        """This Methods will trigger Slide Animation"""
        self.ui.menuBtn.clicked.connect(lambda: self.slideLeftMenu())

    def restore_or_maximize_window(self):
        """This methods is responsible for resizing the Screen of the MainWindow"""
        if self.isMaximized():
            self.showNormal()
            self.ui.recordsBtn.setIcon(QtGui.QIcon(u":/icons/ICONS/square.svg"))
        else:
            self.showMaximized()
            self.ui.recordsBtn.setIcon(QtGui.QIcon(u":/icons/ICONS/copy.svg"))

    # def moveWindow(self, e):
    #     if self.isMaximized() == False:
    #         if e.buttons() == Qt.LeftButton:
    #             self.move(self.pos() - e.globalPos() - self.clickPostion)
    #             e.accept()
    #
    # def mousePressEvents(self, event):
    #     self.clickPostion = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())
