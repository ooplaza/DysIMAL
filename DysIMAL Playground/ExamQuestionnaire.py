from MathFluencySubtest1To5 import *
from MathFluencySubTest6To10 import *
from MathFluencySubtest11To15 import *
from CalculationSubTest1to5 import *
from CalculationSubTest6to10 import *
from CalculationSubTest11To15 import *
from StudentProfile import *


class ExamQuestions:
    """This class is responsible for the questionnaire of the entire exam."""
    def __init__(self, MainWindow):
        """Attribute initializing for all Questions in the Entire Exam!"""
        self.mathFluency1to5 = MathFluencySubTest1to5()
        self.mathFluency6to10 = MathFluencySubTest6to10()
        self.mathFluency11to15 = MathFluencySubtest11To15()
        self.calculationSubtest1to5 = CalculationSubtest1To5()
        self.calculationSubtest6to10 = CalculationSubtest6To10()
        self.calculationSubtest11to15 = CalculationSubtest10to15()
        self.mainWindow = MainWindow

    def calculation_subtest_1_to_5(self):
        self.calculationSubtest1to5.setupUi(self.mainWindow)
        self.calculationSubtest1to5.pushButton_2.clicked.connect(self.calculation_subtest_6_to_10)

    def calculation_subtest_6_to_10(self):
        self.calculationSubtest6to10.setupUi(self.mainWindow)
        self.calculationSubtest6to10.pushButton.clicked.connect(self.calculation_subtest_1_to_5)
        self.calculationSubtest6to10.pushButton_2.clicked.connect(self.calculation_subtest_11_to_15)

    def calculation_subtest_11_to_15(self):
        self.calculationSubtest11to15.setupUi(self.mainWindow)
        self.calculationSubtest11to15.pushButton.clicked.connect(self.calculation_subtest_6_to_10)
        self.calculationSubtest11to15.pushButton_2.clicked.connect(self.math_fluency_1_to_5)

    def math_fluency_1_to_5(self):
        """This function is responsible for math fluency subtest number 1 to 5"""
        self.mathFluency1to5.setupUi(self.mainWindow)
        self.mathFluency1to5.pushButton.clicked.connect(self.calculation_subtest_11_to_15)
        self.mathFluency1to5.pushButton_2.clicked.connect(self.math_fluency_6_to_10)

    def math_fluency_6_to_10(self):
        """This function is responsible for math fluency subtest number 6 to 10"""
        self.mathFluency6to10.setupUi(self.mainWindow)
        self.mathFluency6to10.pushButton.clicked.connect(self.math_fluency_1_to_5)
        self.mathFluency6to10.pushButton_2.clicked.connect(self.math_fluency_11_to_15)

    def math_fluency_11_to_15(self):
        """This function is responsible for math fluency subtest number 11 to 15."""
        self.mathFluency11to15.setupUi(self.mainWindow)
        self.mathFluency11to15.pushButton.clicked.connect(self.math_fluency_6_to_10)
        self.mathFluency11to15.pushButton_2.clicked.connect(self.math_fluency_16_to_20)

    def math_fluency_16_to_20(self):
        pass
