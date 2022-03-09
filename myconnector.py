from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='dysimal'
)

cursor = mydb.cursor()

first_name = input("Enter your First Name:\n")
middle_name = input("Enter your Middle Name:\n")
last_name = input("Enter your Last Name:\n")
grade_level = int(input("Grade:\n"))
age = int(input("Age:\n"))

insertquery = 'INSERT INTO students_profile values(%s,%s,%s,%s,%s)'

student = (first_name, middle_name, last_name, grade_level, age)

cursor.execute(insertquery, student)

mydb.commit()
