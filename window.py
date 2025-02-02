from tkinter import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
win = Tk()
win.geometry("1150x950")
win.title("Dairy Management")
win.resizable(True, True)  # width,height
