import mysql.connector as sqltor
from tkinter import messagebox

with open("database_password.txt", "r+") as f:
    password = f.read()  # read everything in the file
try:
    my = sqltor.connect(host='localhost',
                        user='root', password=password,
                        database='gui_dairy_management')
except :
    messagebox.showinfo("Password not found", "Open database_password.txt ,type password and save")
