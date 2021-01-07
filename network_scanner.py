import nmap
import who_is_on_my_wifi
from who_is_on_my_wifi import *
#pip3 install who-is-on-my-wifi (required pip install wmi AND MANUALY INSTALL NMAP [nmap.org/download.html] do nmap-7.91-setup.exe)

WHO = who()
for i in range(0, len(WHO)):
    print(WHO[i])
    #print(WHO[i][1]) #prints only the ip addresses