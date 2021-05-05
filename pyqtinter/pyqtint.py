import sys, icon_rc, random
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi

quotes=[
    'Looking over you!',
    'I spy some malicious content.',
    'A UDP packet walks into a bar,\n no one acknowledges him.',
    'What did the router dog say\nto the other router dog?\nARP! ARP! ARP!'
]

class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi('login.ui',self)
        self.setFixedSize(310,465)
        self.pushButton.clicked.connect(self.loginfunction)
        self.pushButton_2.clicked.connect(self.gotosignup)
        self.label_3.setText(random.choice(quotes))

    def loginfunction(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(user)
        print(password)
        #authenticate here
        devpg = DevicesPage()
        widget.addWidget(devpg)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignup(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

class SignUp(QtWidgets.QDialog):
    def __init__(self):
        super(SignUp,self).__init__()
        loadUi('signup.ui',self)
        self.pushButton.clicked.connect(self.createAcc)

    def createAcc(self):
        fName = self.lineEdit.text()
        lName = self.lineEdit_2.text()
        user = self.lineEdit_3.text()
        password = self.lineEdit_4.text()

        print(fName)
        print(lName)
        print(user)
        print(password)
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class DevicesPage(QtWidgets.QDialog):
    def __init__(self):
        super(DevicesPage,self).__init__()
        self.resize(700,600)
        loadUi('devpage.ui',self)
        self.setFixedSize(700,600)
        self.pushButton_2.clicked.connect(self.gotorep)
    
    def gotorep(self):
        reppg = ReportsPage()
        widget.addWidget(reppg)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ReportsPage(QtWidgets.QDialog):
    def __init__(self):
        super(ReportsPage,self).__init__()
        loadUi('reppage.ui',self)
        self.pushButton.clicked.connect(self.gotodev)
        
    def gotodev(self):
        devpg = DevicesPage()
        widget.addWidget(devpg)
        widget.setCurrentIndex(widget.currentIndex()+1)

app = QtWidgets.QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)        
widget.setWindowTitle(QtCore.QCoreApplication.translate('Form','ScanNET'))
widget.setWindowIcon(QtGui.QIcon('scanneticon.png'))
widget.show()
app.exec()