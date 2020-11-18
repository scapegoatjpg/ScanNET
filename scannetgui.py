import tkinter as tk
from tkinter import *

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')

        #textboxes
        first_textbox = Text(self.root, width=50, height=20, bg="yellow")
        second_textbox = Text(self.root, width=25, height=10, bg="blue")
        third_textbox = Text(self.root, width=25, height=10, bg="red")

        #pack it all up
        first_textbox.grid(column=1, row=1, rowspan=2)
        second_textbox.grid(column=2, row=1)
        third_textbox.grid(column=2, row=2)
        
    def start(self):
        self.root.mainloop()

scannetstart = GUI()
scannetstart.start()