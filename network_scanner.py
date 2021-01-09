import time
import nmap
import who_is_on_my_wifi
from who_is_on_my_wifi import who
#pip3 install who-is-on-my-wifi (required pip install wmi AND MANUALY INSTALL NMAP [nmap.org/download.html] do nmap-7.91-setup.exe)

ipmacs = {}
WHO = who()
for i in range(0, len(WHO)):
    ipmacs[WHO[i][1]] = WHO[i][3]   #dictionary to put in ip addresses and corresponding MAC addresses

def netting():
    while True:
        print(ipmacs)       #prints the list on terminal
        time.sleep(3)       #delays by 3 seconds