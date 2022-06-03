from PySide2.QtCore import QFileInfo
from PySide2.QtPrintSupport import QPrinter
from PySide2.QtWidgets import QMainWindow, QApplication, QSizeGrip, QFileDialog
from Application import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # METHODS CALLING
        ################################################################################################################
        # self.animate_sideMenu()
        self.export_buttons_functionality()
        self.windows_Configuration()
        self.stackWidget_Behaviour()
        self.all_Exam_buttons_functionality()
        ################################################################################################################

    def windows_Configuration(self):
        """THIS METHOD IS RESPONSIBLE FOR WINDOWS CONFIGURATION."""
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_6.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_7.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.pushButton_8.clicked.connect(lambda: self.close())
        QSizeGrip(self.ui.sigeGrip)

    def restore_or_maximize_window(self):
        """This methods is responsible for resizing the Screen of the MainWindow"""
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_7.setIcon(QtGui.QIcon(u":/icons/1CON/square.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_7.setIcon(QtGui.QIcon(u":/icons/1CON/copy.svg"))

    def stackWidget_Behaviour(self):
        """THIS METHOD IS RESPONSIBLE FOR STACKWIDGET BEHAVIOR."""
        self.ui.studentProfileBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ProfilePage))
        self.ui.takeTestBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ExamPage))
        self.ui.recordsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RecordsPage))
        self.ui.devsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.DevtPage))
        self.ui.sideMenuBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.HomePage))

    def export_buttons_functionality(self):
        """THIS METHOD WILL TRIGGER THE Export_PDF()"""
        self.ui.exportPdfBtn.clicked.connect(self.Export_PDF)

    def Export_PDF(self):
        """THIS METHOD IS RESPONSIBLE FOR EXPORTING ANY DATA COMING FROM TEXTEDIT FUNCTION"""
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.ui.textEdit.document().print_(printer)

        # GETTING RID THE CONTENTS AFTER EXPORTING
        self.ui.get_rid_text_export()

    def all_Exam_buttons_functionality(self):
        """THIS METHOD IS RESPONSIBLE FOR ALL THE BUTTONS FUNCTIONALITY."""
        self.ui.submitBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ExamPage))
        self.ui.searchBtn.clicked.connect(lambda: self.ui.get_user_info_from_db())

        # NEXT FUNCTIONALITY
        self.ui.pushButton_3.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculationSubTest6to10))
        self.ui.pushButton_4.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculationSubTest11to15))
        self.ui.pushButton_9.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest1to5))
        self.ui.pushButton_11.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest6to10))
        self.ui.pushButton_13.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest11to15))
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices1to3))
        self.ui.pushButton_21.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices4to6))
        self.ui.pushButton_23.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices7to10))
        self.ui.pushButton_25.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.applied1to5))
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.applied6to10))

        # BACK FUNCTIONALITY
        self.ui.pushButton_20.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.applied1to5))
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices7to10))
        self.ui.pushButton_26.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices4to6))
        self.ui.pushButton_24.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.matrices1to3))
        self.ui.pushButton_22.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest11to15))
        self.ui.pushButton_16.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest6to10))
        self.ui.pushButton_14.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.mathFluencySubtest1to5))
        self.ui.pushButton_12.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculationSubTest11to15))
        self.ui.pushButton_10.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculationSubTest6to10))
        self.ui.pushButton_5.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculationSubTest1to5))
