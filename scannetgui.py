import tkinter as tk
from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ScanNET")
        #all widths and heights aren't official, most likely change
        self.root.minsize (600, 500)

        #the tabs
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack()
        devicestab = Frame(my_notebook, width=600, height=500, bg="blue")
        reportstab = Frame(my_notebook, width=600, height=500, bg="red")
        devicestab.pack(fill="both", expand=1)
        reportstab.pack(fill="both", expand=1)
        my_notebook.add(devicestab, text="Devices")
        my_notebook.add(reportstab, text="Reports")
        
        
    def start(self):
        self.root.mainloop()

scannetstart = GUI()
scannetstart.start()