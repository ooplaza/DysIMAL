"""
    Team DysIMAL
    RENOMERON, ROMEL LOVE RYAN
    BIAOCO, VINCE HARVEY
    BAYSA, JERSON
    PLAZA, ORLY
"""


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# Initialize Application from QtClass
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("DysIMAL")
window.setFixedWidth(1000)
window.setFixedHeight(650)
window.setStyleSheet("Background: #D3D3D3;")

# Initialized Grid Layout for the window
grid = QGridLayout()
window.setLayout(grid)

# This line of codes is set to the global variable
widgets = {
    "logo": [],
    "button": []
}

def create_button(text):
    """This function will be responsible for the creation of buttons."""
    pass

# Take test button for the main frame
def takeTest_button():
    """This function will display the push button name (take test)."""
    button = QPushButton("Take test")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        # Using CSS to Design the Push Button
        "*{border: 4px solid '#000000';" +
        "border-radius: 45px;" +
        "font-family: 'After Disaster';" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 20px 0;" +
        "margin: 50px 50px}" +
        "*:hover{background: '#FF7F50'}"
    )

    # Importing the image logo
    image = QPixmap(".\Images\logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)

    # Using this line of code, it will append it to the global variable name widgets and can fill whenever this
    # function calls
    widgets["button"].append(button)
    widgets["logo"].append(logo)

    # adding this widget to the grid class
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-1], 1, 0)


takeTest_button()
window.show()
app.exit(app.exec())
