import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

LARGE_FONT = ("Verdana", 22)
fakeloginsfornow = {
    "laura115":"pass5",
    "yeet":"whataburger_10"
}
class Pages(tk.Tk):
    #starts us off in the login page
    def __init__(self):
        tk.Tk.__init__(self)

        self.winfo_toplevel().title("ScanNET")
        self.wm_minsize(1350, 600)

        container = tk.Frame(self)

        container.grid(row=0, column=0)

        self.frames = {}

        for F in (Loginpage, GUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NESW')

        self.show_frame(Loginpage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
class Loginpage(tk.Frame):
    #login page content
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #username and password 
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        #=====login label
        loginlabel = tk.Label(self, text="ScanNET Login", font=LARGE_FONT)
        loginlabel.grid(row=0, column=0, columnspan=2, pady=40)

        #=====frames
        loginframe1 = tk.LabelFrame(self, width=800, height=600, bd=20)
        loginframe1.grid(row=1, column=0)
        loginframe2 = tk.LabelFrame(self, width=600, height=400, bd=20)
        loginframe2.grid(row=2, column=0)

        #=====Label and Entry
        userlabel = tk.Label(loginframe1, text="Username", font=(20))
        userlabel.grid(row=0, column=0)
        usertext = tk.Entry(loginframe1, font=(20))
        usertext.grid(row=0, column=1)

        passlabel = tk.Label(loginframe1, text="Password", font=(20))
        passlabel.grid(row=1, column=0)
        passtext = tk.Entry(loginframe1, font=(20))
        passtext.grid(row=1, column=1)
        
        #=====Buttons
        loginbutton = tk.Button(loginframe2, text="Login", width=17, font=(20), command=lambda: controller.show_frame(GUI)) #need to make login system 
        loginbutton.grid(row=3, column=0, pady=20, padx=8)
        resetbutton = tk.Button(loginframe2, text="Reset", width=17, font=(20))
        resetbutton.grid(row=3, column=1, pady=20, padx=8)
        closebutton = tk.Button(loginframe2, text="Exit", width=17, font=(20))
        closebutton.grid(row=3, column=2, pady=20, padx=8)

        
        
        



class GUI(tk.Frame):
    def __init__(self, parent, controller):
        #all widths and heights aren't official, most likely change
        tk.Frame.__init__(self, parent)
        #the tabs
        my_notebook = ttk.Notebook(self)
        my_notebook.grid()
        devicestab = tk.Frame(my_notebook, width=800, height=600)
        reportstab = tk.Frame(my_notebook, width=800, height=600)
        devicestab.pack(fill='both', expand=1)
        reportstab.pack(fill='both', expand=1)
        my_notebook.add(devicestab, text="Devices")
        my_notebook.add(reportstab, text="Reports")

        #contents for devices tab
        devicesleft = tk.LabelFrame(devicestab, text="Devices found: ", padx=5, pady=5, width=500, height=600)
        devicesleft.grid(row=0, column=0)
        devicesright = tk.LabelFrame(devicestab, text="Activity Feed: ", padx=5, pady=5, width=300 , height=600)
        devicesright.grid(row=0, column=1)

        #contents for reports tab
        reportsleft = tk.LabelFrame(reportstab, text="Report Summaries: ", padx=5, pady=5, width=400 , height=600)
        reportsleft.grid(row=0, column=0)
        reportsright= tk.LabelFrame(reportstab, text="Charts and Diagrams: ", padx=5, pady=5, width=400 , height=600)
        reportsright.grid(row=0, column=1)


app = Pages()
app.mainloop()