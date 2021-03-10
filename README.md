# ScanNET
ScanNET is a senior design project from four students that Prairie View A&M University.  

Laura Longoria - Team leader (so Project Manager) and back-end developer.  
Jerusalem Abebe - Front-end developer, researcher, and diversed developer.  
Shontell Murphy - Front-end developer, full stack if needed.  
Eric Richardson - Network specialist.  

In summary, ScanNET is an anomaly detection system. It will scan for devices in a user's network and show activity from all devices scanned. 

## Prerequisites
Make sure you have these. (We'll end up trying to make it so that these get installed for the user.)
- Windows 10
- pypcap
- dpkt


## Install requirements.txt

    pip install -r requirements.txt

    #to start gui
    python scannetgui.py 

    #to test packet sniffer (Crtl+C to quit sniffing)
    python sniffing.py