# ScanNET
ScanNET is a senior design project from four students that Prairie View A&M University.  

Laura Longoria - Team leader (so Project Manager), front and back-end developer.  
Jerusalem Abebe - Interface and database designer.  
Shontell Murphy - Full stack developer.  
Eric Richardson - Front-end developer, network specialist.  

In summary, ScanNET is a network activity scanner that scans devices in a user's network. ScanNET also uses machine learning to alert users on sites visited while using ChromeDriver.

## Prerequisites
Make sure you have these.
- Windows 10
- git clone https://github.com/scapegoatjpg/ScanNET
- Install requirements.txt
- Install most recent stable release for [ChromeDriver](https://sites.google.com/chromium.org/driver/)
    - Go to 'scannetgui.py' and paste chromedriver.exe's directory into webdriver.Chrome(r'here')
        - If it doesn't work, try running chromedriver.exe at least one time
        - example: driver = webdriver.Chrome(r'G:\downloads\chromedriver.exe')
- Have [xampp](https://www.apachefriends.org/download.html) and [mysql](https://dev.mysql.com/downloads/installer/) installed
    - turn on apache and mysql
    - import the sql file into localhost/php


## Install requirements.txt

    pip install -r requirements.txt
    #if requirements don't fully download, pip install them manually ¯\_(ツ)_/¯

    #to start gui
    python scannetgui.py 
