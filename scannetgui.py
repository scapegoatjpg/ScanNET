import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import sniffing
from sniffing import pkt_list
from sniffing import time
import threading


LARGE_FONT = ('Verdana', 22)
fakeloginsfornow = {
    'laura115':'pass5',
    'yeet':'whataburger_10'
}

class Pages(tk.Tk):
    #starts us off in the login page
    def __init__(self):
        tk.Tk.__init__(self)

        self.iconbitmap(r'snicon.ico')
        self.winfo_toplevel().title('ScanNET')
        self.wm_minsize(800, 600)
        self.wm_maxsize(800, 600)

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
        
        #=====button functions
        def printlogins():
            print (fakeloginsfornow)

        def validation(self, controller):
            u = (self.username.get())
            p = (self.password.get())
            
            if u == '' and p == '':
                tkinter.messagebox.showerror('Error', 'Please enter your credentials.')
            else:   #try except so that we don't deal with KeyError
                try:
                    if p in fakeloginsfornow[u]:
                        controller.show_frame(GUI)
                        sniffthread.start()
                except KeyError:
                    tkinter.messagebox.showerror('Error', 'Wrong credentials, please try again.')
                    resetting()
        
        def registeruser(self, user, passw):
            print('registering this new user...')
            u = (user.get())
            p = (passw.get())

            if u == '' or p == '':
                tkinter.messagebox.showerror('Error', 'Please enter your credentials.')
                printlogins()
            else:
                if u in fakeloginsfornow:
                    tkinter.messagebox.showerror('Error', 'Username already taken, please use a different username.')
                    user.set('')
                    printlogins()
                else:
                    fakeloginsfornow[u] = p
                    tkinter.messagebox.showinfo('Register', 'Register successful.')
                    printlogins()

        def registering():
            regwin = new_window(self)
            regwin.iconbitmap(r'snicon.ico')
            regwin.title('Register for ScanNET')
            regwin.geometry('600x400')
            newuser = tk.StringVar()
            newpass = tk.StringVar()

            tk.Label(regwin, text = 'Please enter your information.', font=LARGE_FONT).pack()
            tk.Label(regwin, text='').pack()
            
            tk.Label(regwin, text='Username').pack()
            userentry = tk.Entry(regwin, textvariable=newuser)
            userentry.pack()
            tk.Label(regwin, text='Password').pack()
            passentry = tk.Entry(regwin, show='*',textvariable=newpass)
            passentry.pack()
            tk.Label(regwin, text='').pack()
            tk.Button(regwin, text='Register', width=10, height=1, command=lambda: registeruser(self, newuser, newpass)).pack()
        
        def resetting():
            self.username.set('')
            self.password.set('')
            usertext.focus()

        def exiting(self):
            self.exiting = tkinter.messagebox.askyesno('Exit?', 'Are you sure you want to exit?')
            if self.exiting > 0:
                self.quit()
            else:
                usertext.focus()

        def new_window(self):
            return tk.Toplevel(self.master)

        tk.Frame.__init__(self,parent)
        tk.Frame.configure(self, bg='darkseagreen3')
        
        #=====username and password 
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        #=====login label
        loginlabel = tk.Label(self, text='ScanNET Login', bg='darkseagreen3', font=LARGE_FONT)
        loginlabel.grid(row=0, column=0, columnspan=2, pady=40)

        #=====frames
        loginframe1 = tk.LabelFrame(self, width=800, height=600, bd=20, bg='darkseagreen3')
        loginframe1.grid(row=1, column=0)
        loginframe2 = tk.LabelFrame(self, width=600, height=400, bd=20, bg='darkseagreen3')
        loginframe2.grid(row=2, column=0)

        #=====Label and Entry
        userlabel = tk.Label(loginframe1, text='Username', font=(20), bg='darkseagreen3')
        userlabel.grid(row=0, column=0)
        usertext = tk.Entry(loginframe1, font=(20), textvariable = self.username)
        usertext.grid(row=0, column=1)

        passlabel = tk.Label(loginframe1, text='Password', font=(20), bg='darkseagreen3')
        passlabel.grid(row=1, column=0)
        passtext = tk.Entry(loginframe1, font=(20), show='*',textvariable = self.password)
        passtext.grid(row=1, column=1)

        #=====Buttons
        loginbutton = tk.Button(loginframe2, text='Login', width=17, font=(20), bg='darkseagreen3', command=lambda: validation(self, controller)) #need to make login system 
        loginbutton.grid(row=3, column=0, pady=20, padx=8)
        registerbutton = tk.Button(loginframe2, text='Register', width=17, font=(20), bg='darkseagreen3', command=lambda: registering())
        registerbutton.grid(row=3, column=1, pady=20, padx=8)
        resetbutton = tk.Button(loginframe2, text='Reset', width=17, font=(20), bg='darkseagreen3', command=lambda: resetting())
        resetbutton.grid(row=3, column=2, pady=20, padx=8)
        closebutton = tk.Button(loginframe2, text='Exit', width=17, font=(20), bg='darkseagreen3', command=lambda: exiting(self))
        closebutton.grid(row=3, column=3, pady=20, padx=8)

class GUI(tk.Frame):
    def __init__(self, parent, controller):
        #all widths and heights aren't official, most likely change
        def updatefeed():
            #updates the packet feed in the gui
            while True:
                #continously checks if anything is added into the pkt_list queue. Packets are added from sniffing thread 
                #prints packet info into console, otherwise prints no packet info
                print('Checking for feed...')
                if len(pkt_list) != 0:
                    print('Updating feed...')
                    pktmp = pkt_list.pop(0)
                    print('No.: ', pktmp.num)
                    print('Length: ', pktmp.length)
                    print('Timestamp: ', pktmp.ts)
                    print('Ethernet Frame: ', pktmp.macsrc, pktmp.macdst)
                    print('%s: %s -> %s' % (pktmp.ipv, pktmp.src, pktmp.dst))

                    if (pktmp.sport != 0) or (pktmp.dport != 0):
                        try:
                            print('Source Port: %d' % pktmp.sport)
                            print('Destination Port: %d' % pktmp.dport)
                        except AttributeError:
                            pass
                        
                    if (pktmp.prtcl == 'ICMP6') or (pktmp.prtcl == 'ICMP'):
                        try:
                            print('%s: type:%d code:%d checksum:%d data: %s' % (pktmp.prtcl, pktmp.pack.type, pktmp.pack.code, pktmp.pack.sum, repr(pktmp.pack.data)))
                        except AttributeError:
                            pass
                        
                    print('Feed updated!\n')

                else:
                    time.sleep(0.5)
                    print('No feed to update.\n')
        #thread for updating packet info starts when scannetgui.py is executued, but won't print any packets since sniffing thread begins once successfully logged in
        updatethread = threading.Thread(target=updatefeed)
        updatethread.start()

        tk.Frame.__init__(self, parent)

        #the tabs
        my_notebook = ttk.Notebook(self)
        my_notebook.grid()
        devicestab = tk.Frame(my_notebook, width=800, height=600)
        reportstab = tk.Frame(my_notebook, width=800, height=600)
        devicestab.pack(fill='both', expand=1)
        reportstab.pack(fill='both', expand=1)
        my_notebook.add(devicestab, text='Devices')
        my_notebook.add(reportstab, text='Reports')

        #contents for devices tab
        devicesleft = tk.LabelFrame(devicestab, text='Devices found: ', padx=5, pady=5, width=500, height=600, bg='darkseagreen3')
        devicesleft.grid(row=0, column=0)
        devicesright = tk.LabelFrame(devicestab, text='Activity Feed: ', padx=5, pady=5, width=300 , height=600, bg='darkseagreen3')
        devicesright.grid(row=0, column=1)

        #contents for reports tab
        reportsleft = tk.LabelFrame(reportstab, text='Report Summaries: ', padx=5, pady=5, width=400 , height=600, bg='darkseagreen3')
        reportsleft.grid(row=0, column=0)
        reportsright= tk.LabelFrame(reportstab, text='Charts and Diagrams: ', padx=5, pady=5, width=400 , height=600, bg='darkseagreen3')
        reportsright.grid(row=0, column=1)
    
#threads so work different processes can go at the same time
def backthread():
    sniffing.net()
def forethread():
    app = Pages()
    app.mainloop()

sniffthread = threading.Thread(target=backthread)
guithread = threading.Thread(target=forethread)
guithread.start()