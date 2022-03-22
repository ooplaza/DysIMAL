from MathFluencySubtest1to5 import *
from MathFluencySubtest6to10 import *
from MathFluencySubtest11to15 import *
from CalculationSubTest1to5 import *
from CalculationSubTest6to10 import *
from CalculationSubTest11to15 import *
from AppliedProblemSubtest1to5 import *
from AppliedProblemSubtest6to10 import *


class ExamQuestions:
    """This class is responsible for the questionnaire of the entire exam."""
    def __init__(self, MainWindow):
        """Attribute initializing for all Questions in the Entire Exam!"""
        self.mathFluency1to5 = MathFluencySubTest1To5()
        self.mathFluency6to10 = MathFluencySubTest6To10()
        self.mathFluency11to15 = MathFluencySubtest11To15()
        self.calculationSubtest1to5 = CalculationSubtest1To5()
        self.calculationSubtest6to10 = CalculationSubtest6To10()
        self.calculationSubtest11to15 = CalculationSubtest11To15()
        self.appliedProblem1to5 = AppliedProblemSubtest1To5()
        self.appliedProblem6to10 = AppliedProblemSubtest6To10()
        self.mainWindow = MainWindow

    def calculation_subtest_1_to_5(self):
        self.calculationSubtest1to5.setupUi(self.mainWindow)
        self.calculationSubtest1to5.pushButton.hide()
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
        self.mathFluency11to15.pushButton_2.clicked.connect(self.applied_problem_1_to_5)

    def applied_problem_1_to_5(self):
        self.appliedProblem1to5.setupUi(self.mainWindow)
        self.appliedProblem1to5.pushButton.clicked.connect(self.math_fluency_11_to_15)
        self.appliedProblem1to5.pushButton_2.clicked.connect(self.applied_problem_6_to_10)

    def applied_problem_6_to_10(self):
        self.appliedProblem6to10.setupUi(self.mainWindow)
        self.appliedProblem6to10.pushButton.clicked.connect(self.applied_problem_1_to_5)
        self.appliedProblem6to10.pushButton_2.hide()