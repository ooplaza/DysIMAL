

from PyQt5 import QtCore, QtGui, QtWidgets
import recpic

class SearchRecordsUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 781, 371))
        self.widget.setStyleSheet("background-color: rgb(180, 203, 253);\n"
"border-radius: 20px;")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 40, 761, 61))
        self.frame.setTabletTracking(False)
        self.frame.setStyleSheet("background-color: rgb(218, 229, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 291, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.textChanged.connect(self.nameText_change)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 20, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.gradeText_change)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(340, 20, 47, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 20, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.textChanged.connect(self.ageText_change)
        self.search = QtWidgets.QPushButton(self.frame)
        self.search.setGeometry(QtCore.QRect(690, 10, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setStyleSheet("background-color: rgb(180, 203, 253);")
        self.search.setObjectName("search")
        self.search.clicked.connect(self.search_btn_clicked)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 761, 201))
        self.frame_2.setStyleSheet("background-color: rgb(218, 229, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(5, 10, 751, 161))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        self.homeButton.setGeometry(QtCore.QRect(10, 320, 371, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("background-color: rgb(218, 229, 255);")
        self.homeButton.setObjectName("homeButton")
        self.exportPdfButton = QtWidgets.QPushButton(self.widget)
        self.exportPdfButton.setGeometry(QtCore.QRect(390, 320, 381, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exportPdfButton.setFont(font)
        self.exportPdfButton.setStyleSheet("background-color: rgb(218, 229, 255);")
        self.exportPdfButton.setObjectName("exportPdfButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 241, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 0, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 40, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 821, 491))
        self.frame_3.setStyleSheet("image: url(:/newPrefix/WhiteBackground.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.widget.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def search_btn_clicked(self):
            """This function is for fetching records information"""
            self.textBrowser.setText("Name: " + self.lineEdit.text() + "\nAge: " + self.lineEdit_3.text() + "\nGrade Level: " + self.lineEdit_2.text())
    
    def ageText_change(self):
            if self.lineEdit_3.text().isdigit():
                    print("Valid age")
            else:
                    
                self.lineEdit_3.setText(self.lineEdit_3.text().translate({ord(i): None for i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*;(")[]-_+=<>,./?}{\|`~'}))
    
    def gradeText_change(self):
            if self.lineEdit_2.text().isdigit():
                    print("Valid grade")
            else:
                    
                self.lineEdit_2.setText(self.lineEdit_2.text().translate({ord(i): None for i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(");[]-_+=<>,./?}{\|`~'}))
    
    def nameText_change(self):
        if self.lineEdit.text().isalpha():
                    print("Valid name")
        else:
                self.lineEdit.setText(self.lineEdit.text().translate({ord(i): None for i in '1234567890!@#$%^&*(")[]-_+=<>,./?}{\|`~;'}))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Write your name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your Grade Level"))
        self.label_3.setText(_translate("MainWindow", "Age:"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Grade Level:"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "How old are you?"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        self.exportPdfButton.setText(_translate("MainWindow", "Export PDF"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">R E C O R D S</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "D y s I M A L"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Dyscalculia Immediate Mode of Assessment in Learning System</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SearchRecordsUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
