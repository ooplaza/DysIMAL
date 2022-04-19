import sys
import os
from cx_Freeze import setup, Executable

# Add Files
files = ['icon.ico', 'Application', 'icons', 'main', 'splashScreen', 'splashScreenTrigger',
         'style']

# Target
target = Executable(
    script="splashScreenTrigger.py",
    base="Win32GUI",
    icon="icon.ico"
)

# Setup Cx Freeze
setup(
    name="DysIMAL",
    version="1.0",
    description="Dyscalculia Immediate Mode of Assessment Learning System",
    author="PLAZA, ORLY O.",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
