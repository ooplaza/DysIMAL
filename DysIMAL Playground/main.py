"""
    DysIMAL Beta Version
"""
# Importing all the necessary files/modules to be include in the main program
from PyQt5.QtWidgets import QApplication
from ExamQuestionnaire import *
from TakeTestRecordsUI import *
from StudentProfile import *
from records1 import *
from WelcomeUI import *
import sys


class main:
    def __init__(self):
        """Initializing class as a Module"""
        self.welcome_ui = WelcomeUI()
        self.mainWindow = QtWidgets.QMainWindow()
        self.take_test_and_records_ui = TakeTestRecords_UI()
        self.student_profile_ui = StudentProfileUI()
        self.search_records = SearchRecords()
        self.Questions = ExamQuestions(self.mainWindow)

        # Methods calling
        self.display_welcome()

    def display_student_profile(self):
        """This functions is responsible for displaying Student Profile UI."""
        self.student_profile_ui.setupUi(self.mainWindow)
        self.student_profile_ui.pushButton.clicked.connect(self.display_welcome)
        self.student_profile_ui.pushButton_2.clicked.connect(self.get_exam_questions)

    def display_take_test_records(self):
        """This function is responsible for fetching data from local database"""
        self.take_test_and_records_ui.setupUi(self.mainWindow)
        self.take_test_and_records_ui.pushButton.clicked.connect(self.display_student_profile)
        self.take_test_and_records_ui.pushButton_2.clicked.connect(self.get_records)

    def display_welcome(self):
        """This method is responsible for switching frame from welcome to take test and records frame."""
        self.welcome_ui.setupUi(self.mainWindow)
        self.welcome_ui.pushButton.clicked.connect(self.display_take_test_records)

    def get_exam_questions(self):
        """This function is use to trigger all the question systematically"""
        self.Questions.calculation_subtest_1_to_5()

    def get_records(self):
        self.search_records.setupUi(self.mainWindow)
        #self.search_records.pushButton_3.clicked.connect(self.display_welcome)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.mainWindow.show()
    sys.exit(app.exec())
