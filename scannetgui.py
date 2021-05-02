import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import sniffing
from sniffing import pkt_list, recentdevs, alldevs, time, datetime, Devs, pktcounting, track, socket
import threading
import DBconn
from DBconn import * 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib import style
style.use('ggplot')

#testing out figure sizes
fig1 = Figure(figsize=(5,5), dpi=100)
a1 = fig1.add_subplot(111)
#fig2 = Figure(figsize=(5,5), dpi=100)
#a2 = fig2.add_subplot(111)

xPkts = []
yIP = []
yNONIP = []
yTCP = []
yUDP = []
yARP = []
yHTTP = []
yHTTPS = []
ySMTP = []
yDHCP = []
yFTP = []
ySSH = []
yNTP = []
yTN = []
yWHO = []
yRSYNC = []
yICMP = []
yIPV6 = []

colors = [
    'red',
    'blue',
    'yellow'
]

def pktanimate(i):
    xPkts.append(pktcounting.counter)
    yIP.append(pktcounting.ipcounter)
    yNONIP.append(pktcounting.nonipcounter)
    yTCP.append(pktcounting.tcpcounter)
    yUDP.append(pktcounting.udpcounter)
    yARP.append(pktcounting.arpcounter)
    yHTTP.append(pktcounting.httpcounter)
    yHTTPS.append(pktcounting.httpscounter)
    ySMTP.append(pktcounting.smtpcounter)
    yDHCP.append(pktcounting.dhcpcounter)
    yFTP.append(pktcounting.ftpcounter)
    ySSH.append(pktcounting.sshcounter)
    yNTP.append(pktcounting.ntpcounter)
    yTN.append(pktcounting.telnetcounter)
    yWHO.append(pktcounting.whoiscounter)
    yRSYNC.append(pktcounting.rsynccounter)
    yICMP.append(pktcounting.icmpcounter)
    yIPV6.append(pktcounting.ipv6counter)

    a1.clear()
        
    if pktcounting.ipcounter > 0:
        a1.plot(xPkts, yIP, label='IP')
    if pktcounting.nonipcounter > 0:
        a1.plot(xPkts, yNONIP, label='Non-IP')
    if pktcounting.tcpcounter > 0:
        a1.plot(xPkts, yTCP, label='TCP')
    if pktcounting.udpcounter > 0:
        a1.plot(xPkts, yUDP, label='UDP')
    if pktcounting.arpcounter > 0:
        a1.plot(xPkts, yARP, label='ARP')
    if pktcounting.httpcounter > 0:
        a1.plot(xPkts, yHTTP, label='HTTP')
    if pktcounting.httpscounter > 0:
        a1.plot(xPkts, yHTTPS, label='HTTPS')
    if pktcounting.smtpcounter > 0:
        a1.plot(xPkts, ySMTP, label='SMTP')
    if pktcounting.dhcpcounter > 0:
        a1.plot(xPkts, yDHCP, label='DHCP')
    if pktcounting.ftpcounter > 0:
        a1.plot(xPkts, yFTP, label='FTP')
    if pktcounting.sshcounter > 0:
        a1.plot(xPkts, ySSH, label='SSH')
    if pktcounting.ntpcounter > 0:
        a1.plot(xPkts, yNTP, label='NTP')
    if pktcounting.telnetcounter > 0:
        a1.plot(xPkts, yTN, label='TelNet')
    if pktcounting.whoiscounter > 0:
        a1.plot(xPkts, yWHO, label='whois')
    if pktcounting.rsynccounter > 0:
        a1.plot(xPkts, yRSYNC, label='RSYNC')
    if pktcounting.icmpcounter > 0:
        a1.plot(xPkts, yICMP, label='ICMP')
    if pktcounting.ipv6counter > 0:
        a1.plot(xPkts, yIPV6, label='IPv6')

    #a1.title('Packet Types')
    a1.legend()

LARGE_FONT = ('Verdana', 22)
class Pages(tk.Tk):
    #starts us off in the login page
    def __init__(self):
        tk.Tk.__init__(self)

        self.iconbitmap(r'snicon.ico')
        self.winfo_toplevel().title('ScanNET')
        self.wm_minsize(800, 600)

        container = tk.Frame(self)
        container.grid(row=0, column=0)

        self.frames = {}

        for F in (Loginpage, GUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nesw')
        self.show_frame(Loginpage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
class Loginpage(tk.Frame):
    #login page content
    def __init__(self, parent, controller):
        #=====button functions
        def validation(self, controller):
            data = (
               
                self.username.get(),
                self.password.get()
                )

            #validations
            if self.username.get() == '' and self.password.get() == '':
                tkinter.messagebox.showerror('Error', 'Please enter your credentials.')
            else:
               res = user_login(data)
               if res:
                   tkinter.messagebox.showinfo('Message', 'Login Successfully')
                   controller.show_frame(GUI)
                   sniffthread.start()
               else:
                    tkinter.messagebox.showerror('Error', 'Wrong credentials, please try again.')
                    resetting()
        
        def registeruser(self):
            print('registering this new user...')
            data2 = self.password.get()
            data = (
                self.fname.get(),
                self.lname.get(),
                self.username.get(),
                data2
                )

            if self.fname.get() == '' or self.lname.get() == '' or self.username.get() == '' or self.password.get() == '':
                tkinter.messagebox.showerror('Error', 'Please enter your credentials.')    
         
            else:
              res = add_user(data)
              if res:
                  tkinter.messagebox.showinfo('Register', 'Registration successful.')
    
        def registering():
            regwin = new_window(self)
            regwin.iconbitmap(r'snicon.ico')
            regwin.title('Register for ScanNET')
            regwin.geometry('600x400')
            #newfname = tk.StringVar()
            #newlname = tk.StringVar()
            #newuser = tk.StringVar()
            #newpass = tk.StringVar()
            tk.Label(regwin, text = 'Please enter your information.', font=LARGE_FONT).pack()
            tk.Label(regwin, text='').pack()
            tk.Label(regwin, text='First Name').pack()
            fnameentry = tk.Entry(regwin, textvariable= self.fname)
            fnameentry.pack()
            tk.Label(regwin, text='Last Name').pack()
            lnameentry = tk.Entry(regwin, textvariable= self.lname)
            lnameentry.pack()
            tk.Label(regwin, text='Username').pack()
            userentry = tk.Entry(regwin, textvariable= self.username)
            userentry.pack()
            tk.Label(regwin, text='Password').pack()
            passentry = tk.Entry(regwin, show='*',textvariable= self.password)
            passentry.pack()
            tk.Label(regwin, text='Use 8 or more characters with a mix of letters, numbers & symbols').pack()
            tk.Label(regwin, text='').pack()
            tk.Button(regwin, text='Register', width=10, height=1, command=lambda: registeruser(self)).pack()

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
        
        #===== first name, last name, username, and password 
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        #=====login label
        loginlabel = tk.Label(self, text='ScanNET Login', bg='darkseagreen3', font=LARGE_FONT)
        loginlabel.grid(row=0, column=0, columnspan=2, pady=40)

        #=====frames
        loginframe1 = tk.LabelFrame(self, bd=20, bg='darkseagreen3')
        loginframe1.grid(row=1, column=0)
        loginframe2 = tk.LabelFrame(self, bd=20, bg='darkseagreen3')
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

class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, background='#ffffff')          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background='#ffffff')                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)   
        self.canvas.yview_moveto('1.0')                       #attach scrollbar action to scroll of canvas

        self.vsb.pack(side='right', fill='y')                                       #pack scrollbar to right of self
        self.canvas.pack(side='left', fill='both', expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor='nw', tags='self.viewPort')           #add view port frame to canvas      

        self.viewPort.bind('<Configure>', self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind('<Configure>', self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.

class GUI(tk.Frame):
    def __init__(self, parent, controller):
        #all widths and heights aren't official, most likely change                
        def pktwin(p):
            pwin = new_window(self)
            pwin.iconbitmap(r'snicon.ico')
            pwin.title('Packet Information')
            pwin.geometry('400x400')

            pktext = tk.Text(pwin, wrap='word')
            pktext.insert('end', p)
            pktext.grid(row=0, column=0, sticky='nesw')
        
        def devwin(d):
            dwin = new_window(self)
            dwin.iconbitmap(r'snicon.ico')
            dwin.title('Device Information')
            dwin.geometry('400x400')

            devtext = tk.Text(dwin, wrap='word')
            devtext.insert('end', d)
            devtext.grid(row=0, column=0, sticky='nesw')

        def new_window(self):
            return tk.Toplevel(self.master)
        
        def device_info(p):
            deviceinf = device(p)
            if deviceinf:
                print("Device Information is Saved")

        def updatepkts():
            #updates the packet feed in the gui
            while True:
                #continously checks if anything is added into the pkt_list queue. Packets are added from sniffing thread 
                if len(pkt_list) != 0:
                    pktmp = pkt_list.pop(0)
                    pktstr = 'Hostname: ' + pktmp.hostname()
                    pktstr = pktstr + '\nNo.: ' + str(pktmp.num) + '\nLength: ' + str(pktmp.length) + '\nTimestamp: ' + str(pktmp.ts) + '\nEthernetFrame:\nMAC source: ' + str(pktmp.macsrc) + '\nMAC dest: ' + str(pktmp.macdst) + '\n' + str(pktmp.ipv) + ':\nIP source: ' + str(pktmp.src) + '\nIP dest: ' + str(pktmp.dst)

                    if (pktmp.sport != 0) or (pktmp.dport != 0):
                        try:
                            pktstr = pktstr + '\nSource Port: ' + str(pktmp.sport) + '\nDestination Port: ' + str(pktmp.dport)    
                        except AttributeError:
                            pass
                    if (pktmp.prtcl == 'ICMP6') or (pktmp.prtcl == 'ICMP'):
                        try:
                            pktstr = str(pktstr) + str(pktmp.prtcl) + ': type:' + str(pktmp.pack.type) + ' code:' + str(pktmp.pack.code) + ' checksum:' + str(pktmp.pack.sum) + ' data: ' + repr(pktmp.pack.data)  
                        except AttributeError:
                            pass
                    a = pktstr
                    tk.Button(pktframe.viewPort, width=100, anchor='w', text=pktstr, bg=pktmp.color, command=lambda x=a: pktwin(x)).grid(row=pktmp.num, column=0)

                    dev = Devs
                    
                    if any(i.ipaddr == pktmp.src for i in recentdevs) or any(i.ipaddr == pktmp.dst for i in recentdevs):
                        pass
                    else:
                        dev.timing = pktmp.timing
                        if pktmp.src in alldevs:
                            dev.hostname = pktmp.hostname
                            dev.ipaddr = pktmp.src
                            dev.mac = pktmp.macsrc
                       
                        devices = (
                            
                            dev.ipaddr,
                            dev.mac,
                            self.username.get()
                          )    
                       
                        device_info(devices)
                        recentdevs.append(dev)
                            
                    if len(devframe.viewPort.winfo_children()) < len(recentdevs):
                        for i in range(len(devframe.viewPort.winfo_children()), len(recentdevs)):
                            a = recentdevs[i].hostname
                            tk.Button(devframe.viewPort, width=100, anchor='w', text=recentdevs[i].hostname, command=lambda x=a: devwin(x)).grid(row=i, column=0)

                    if len(recentdevs) != 0:
                        for i in range(len(recentdevs)):
                            timenow = (str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second))
                            tdelta = datetime.datetime.strptime(timenow, '%H:%M:%S') - datetime.datetime.strptime(recentdevs[i].timing, '%H:%M:%S')
                            if tdelta > datetime.timedelta(seconds=30):
                                recentdevs.remove(recentdevs[i])
                                i = 0
                                for child in devframe.viewPort.winfo_children():
                                    child.destroy()
                                for j in range(len(recentdevs)):
                                    a = recentdevs[j].hostname
                                    tk.Button(devframe.viewPort, width=100, anchor='w', text=recentdevs[j].hostname, command=lambda x=a: devwin(x)).grid(row=j, column=0)

        def trackdef(name, color):
            if name == '' or name == ' ':
                pass
            else:
                try:
                    track[name] = color
                    trackvar.set('')
                    colorbtn.set(colors[0])
                    tracktext.focus()
                except socket.gaierror:
                    pass
            print(track)


        tk.Frame.__init__(self, parent)

        #the tabs
        my_notebook = ttk.Notebook(self)
        my_notebook.grid()
        devicestab = tk.Frame(my_notebook)
        reportstab = tk.Frame(my_notebook)
        devicestab.pack(fill='both', expand=True)
        reportstab.pack(fill='both', expand=True)
        my_notebook.add(devicestab, text='Devices')
        my_notebook.add(reportstab, text='Reports')

        #contents for devices tab
        devicesleft = tk.LabelFrame(devicestab, text='Devices found: ', padx=5, pady=5, width=2, height=1, bg='darkseagreen3')
        devicesleft.grid(row=0, column=0)

        devicesright = tk.LabelFrame(devicestab, text='Activity Feed: ', padx=5, pady=5, width=1 , height=1, bg='darkseagreen3')
        devicesright.grid(row=0, column=1)

        acttracking = tk.LabelFrame(devicestab, width=2 , height=1, bg='darkseagreen')
        acttracking.grid(row=1, column=1)

        devframe = ScrollFrame(devicesleft)
        devframe.pack(side='top', fill='both', expand=True)

        trackvar = tk.StringVar()
        colorbtn = tk.StringVar(acttracking)
        colorbtn.set(colors[0])
        tracktext = tk.Entry(acttracking, font=(16), textvariable=trackvar, width=25)
        trackbtn = tk.Button(acttracking, text='Track', width=10, height=1, command= lambda: trackdef(trackvar.get(), colorbtn.get()))
        col = tk.OptionMenu(acttracking, colorbtn, *colors)
        tracktext.grid(row=0, column=0)
        col.grid(row=0, column=1)
        trackbtn.grid(row=0, column=2)
        
        pktframe = ScrollFrame(devicesright)
        pktframe.pack(side='top', fill='both', expand=True)

        #contents for reports tab
        reportsleft = tk.LabelFrame(reportstab, text='Report Summaries: ', padx=5, pady=5, width=1 , height=1, bg='darkseagreen3')
        reportsleft.grid(row=0, column=0)
        reportsright= tk.LabelFrame(reportstab, text='Charts and Diagrams: ', padx=5, pady=5, width=1 , height=1, bg='darkseagreen3')
        reportsright.grid(row=0, column=1)
        
        reporting = tk.Text(reportsleft, width=40)
        reporting.pack()
        reporting.insert('end', ' ')

        cnvs1 = FigureCanvasTkAgg(fig1, reportsright)
        cnvs1.draw()
        cnvs1.get_tk_widget().pack(side='top')

        #thread for updating packet info starts when scannetgui.py is executued, but won't print any packets since sniffing thread begins once successfully logged in
        updatethread = threading.Thread(target=updatepkts)
        updatethread.start()
    
#threads so work different processes can go at the same time
def backthread():
    sniffing.net()
def forethread():
    app = Pages()
    ani1 = animation.FuncAnimation(fig1, pktanimate, interval=1550)
    app.mainloop()

sniffthread = threading.Thread(target=backthread)
guithread = threading.Thread(target=forethread)
guithread.start()