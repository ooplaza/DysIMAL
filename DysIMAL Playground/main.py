"""
    DysIMAL Beta Version
"""
# Importing all the necessary files/modules to be include in the main program
from PyQt5.QtWidgets import QApplication

from TakeTestAndRecordsUI import *
from StudentProfile import *
from ExamUIMod import *
from records2 import *
from WelcomeUI import *


class main:
    def __init__(self):
        """Initializing class as a Module"""
        self.welcome_ui = WelcomeUI()
        self.take_test_and_records_ui = TakeTestRecords_UI()
        self.student_profile_ui = StudentProfileUI()
        self.mainWindow = QtWidgets.QMainWindow()
        self.search_records = SearchRecords()
        self.examUI = ExamUI()
        self.hidden = False

        # Methods calling
        self.display_welcome()

    def display_student_profile(self):
        self.student_profile_ui.setupUi(self.mainWindow)
        self.student_profile_ui.pushButton.clicked.connect(self.display_welcome)
        self.student_profile_ui.pushButton_2.clicked.connect(self.display_exam)

    def display_take_test_records(self):
        # hidden = False
        # if hidden:
        #     self.welcome_ui.pushButton.show()
        #     hidden = True
        # else:
        #     self.welcome_ui.pushButton.hide()
        #     hidden = True
        self.take_test_and_records_ui.setupUi(self.mainWindow)
        self.take_test_and_records_ui.pushButton.clicked.connect(self.display_student_profile)
        self.take_test_and_records_ui.pushButton_2.clicked.connect(self.get_records)

    def display_welcome(self):
        """This method is responsible for switching frame from welcome to take test and records frame."""
        self.welcome_ui.setupUi(self.mainWindow)
        self.welcome_ui.pushButton.clicked.connect(self.display_take_test_records)

    def display_exam(self):
        self.student_profile_ui.q_message()
        self.examUI.setupUi(self.mainWindow)

    def get_records(self):
        self.search_records.setupUi(self.mainWindow)
        self.search_records.pushButton_3.clicked.connect(self.display_welcome)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.mainWindow.show()
    sys.exit(app.exec())
