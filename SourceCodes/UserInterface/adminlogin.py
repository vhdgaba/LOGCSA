# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminlogin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UserInterface import peeradviserlogin, adviseelogin

class Ui_Admin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_advisee = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_advisee.setGeometry(QtCore.QRect(20, 90, 91, 23))
        self.pushButton_advisee.setObjectName("pushButton_advisee")
        self.pushButton_advisee.clicked.connect(lambda: self.push_advisee(MainWindow))
        self.pushButton_peeradviser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_peeradviser.setGeometry(QtCore.QRect(20, 120, 91, 23))
        self.pushButton_peeradviser.setObjectName("pushButton_peeradviser")
        self.pushButton_peeradviser.clicked.connect(lambda: self.push_peeradviser(MainWindow))
        self.pushButton_administrator = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_administrator.setGeometry(QtCore.QRect(20, 150, 91, 23))
        self.pushButton_administrator.setObjectName("pushButton_administrator")    
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(340, 170, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")

        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(200, 100, 211, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(200, 130, 211, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
    
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 80, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(140, 100, 51, 21))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(140, 130, 51, 21))
        self.label_password.setObjectName("label_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_advisee.setText(_translate("MainWindow", "Advisee"))
        self.pushButton_peeradviser.setText(_translate("MainWindow", "Peer Adviser"))
        self.pushButton_administrator.setText(_translate("MainWindow", "Administrator"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.label_password.setText(_translate("MainWindow", "Password:"))

    def connect_session(self, session):
        self.ses = session
        
    def push_advisee(self, MainWindow):
        ui = adviseelogin.Ui_Advisee()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)

    def push_peeradviser(self, MainWindow):
        ui = peeradviserlogin.Ui_PeerAdviser()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

