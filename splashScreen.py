from PySide2 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(400, 240)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
                                           "    background-color: #C5D8A4;\n"
                                           "    color: rgb(85, 85, 127);\n"
                                           "    border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.App_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.App_title.setGeometry(QtCore.QRect(0, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.App_title.setFont(font)
        self.App_title.setAlignment(QtCore.Qt.AlignCenter)
        self.App_title.setObjectName("App_title")
        self.App_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.App_description.setGeometry(QtCore.QRect(0, 60, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.App_description.setFont(font)
        self.App_description.setAlignment(QtCore.Qt.AlignCenter)
        self.App_description.setObjectName("App_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 361, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "    \n"
                                       "    ; \n"
                                       "    background-color: #F7E9D7;\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:1, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(238, 238, 238, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.loading.setGeometry(QtCore.QRect(0, 190, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.loading.setFont(font)
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName("loading")
        self.description = QtWidgets.QLabel(self.dropShadowFrame)
        self.description.setGeometry(QtCore.QRect(0, 120, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.App_title.setText(_translate("SplashScreen", "<strong>DysIMAL"))
        self.App_description.setText(
            _translate("SplashScreen", "<strong>Dyscalculia Immediate Mode of Assessment Learning System"))
        self.loading.setText(_translate("SplashScreen", "<strong>Loading..."))
        self.description.setText(_translate("SplashScreen", "<strong>Loading"))
