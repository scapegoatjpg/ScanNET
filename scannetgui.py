import tkinter as tk
from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ScanNET")
        #all widths and heights aren't official, most likely change
        self.root.minsize (800, 600)

        #the tabs
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack()
        devicestab = Frame(my_notebook, width=800, height=600)

        reportstab = Frame(my_notebook, width=800, height=600)
        devicestab.pack(fill=BOTH, expand=1)
        reportstab.pack(fill=BOTH, expand=1)
        my_notebook.add(devicestab, text="Devices")
        my_notebook.add(reportstab, text="Reports")

        #contents for devices tab
        devicesleft = LabelFrame(devicestab, text="Devices found: ", padx=5, pady=5, width=500, height=600)
        devicesleft.grid(row=0, column=0)
        devicesright = LabelFrame(devicestab, text="Activity Feed: ", padx=5, pady=5, width=300 , height=600)
        devicesright.grid(row=0, column=1)

        #contents for reports tab
        reportsleft = LabelFrame(reportstab, text="Report Summaries: ", padx=5, pady=5, width=400 , height=600)
        reportsleft.grid(row=0, column=0)
        reportsright= LabelFrame(reportstab, text="Charts and Diagrams: ", padx=5, pady=5, width=400 , height=600)
        reportsright.grid(row=0, column=1)

        


        
    def start(self):
        self.root.mainloop()

scannetstart = GUI()
scannetstart.start()