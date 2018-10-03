# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('../')
from BusinessLogic.Session import Session
from BusinessLogic.User import User, PeerAdviser
from PyQt5 import QtCore, QtGui, QtWidgets
from UserInterface.passworddialog import Ui_Password
from UserInterface import adviseelogin, adminlogin, peeradviserregistration


class Ui_PeerAdviser(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineEdit_studentnumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_studentnumber.setGeometry(QtCore.QRect(240, 120, 151, 20))
        self.lineEdit_studentnumber.setObjectName("lineEdit_studentnumber")
        self.lineEdit_studentnumber.returnPressed.connect(lambda: self.input_sn())
        self.lineEdit_studentnumber.textChanged.connect(lambda: self.input_changed())
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(190, 90, 431, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_program = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_program.setGeometry(QtCore.QRect(690, 90, 81, 20))
        self.lineEdit_program.setObjectName("lineEdit_program")
        self.lineEdit_program.setReadOnly(True)
        self.lineEdit_organization = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_organization.setGeometry(QtCore.QRect(480, 120, 141, 20))
        self.lineEdit_organization.setObjectName("lineEdit_organization")
        self.lineEdit_organization.setReadOnly(True)
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(150, 150, 621, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(lambda: self.pushButton_logout.setEnabled(True))
        self.updatelist()
        
        self.pushButton_advisee = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_advisee.setGeometry(QtCore.QRect(20, 90, 91, 23))
        self.pushButton_advisee.setObjectName("pushButton_advisee")
        self.pushButton_advisee.clicked.connect(lambda: self.push_advisee(MainWindow))
        self.pushButton_peeradviser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_peeradviser.setGeometry(QtCore.QRect(20, 120, 91, 23))
        self.pushButton_peeradviser.setObjectName("pushButton_peeradviser")
        self.pushButton_admin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin.setGeometry(QtCore.QRect(20, 150, 91, 23))
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.pushButton_admin.clicked.connect(lambda: self.push_admin(MainWindow))
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(700, 350, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setDisabled(True)
        self.pushButton_login.clicked.connect(lambda: self.push_login())
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(620, 350, 75, 23))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_logout.setDisabled(True)
        self.pushButton_logout.clicked.connect(lambda: self.push_logout())
        
        self.label_studentnumber = QtWidgets.QLabel(self.centralwidget)
        self.label_studentnumber.setGeometry(QtCore.QRect(150, 120, 91, 21))
        self.label_studentnumber.setObjectName("label_studentnumber")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(150, 90, 41, 21))
        self.label_name.setObjectName("label_name")
        self.label_program = QtWidgets.QLabel(self.centralwidget)
        self.label_program.setGeometry(QtCore.QRect(640, 90, 51, 21))
        self.label_program.setObjectName("label_program")
        self.label_organization = QtWidgets.QLabel(self.centralwidget)
        self.label_organization.setGeometry(QtCore.QRect(410, 120, 71, 21))
        self.label_organization.setObjectName("label_organization")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 80, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
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
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.pushButton_peeradviser.setText(_translate("MainWindow", "Peer Adviser"))
        self.label_studentnumber.setText(_translate("MainWindow", "Student Number:"))
        self.pushButton_admin.setText(_translate("MainWindow", "Administrator"))
        self.label_program.setText(_translate("MainWindow", "Program:"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_organization.setText(_translate("MainWindow", "Organization:"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))

    def connect_session(self, session):
        self.ses = session
        
    def input_sn(self):
        user = self.ses.get_peeradviser(self.lineEdit_studentnumber.text())
        if user != None:
            self.pushButton_login.setEnabled(True)
            padv = PeerAdviser(*user)
            self.lineEdit_name.setText(padv.get_fullname())
            self.lineEdit_organization.setText(padv.organization)
            self.lineEdit_program.setText(padv.program)
        else:
            self.lineEdit_name.clear()
            self.lineEdit_program.clear()
            self.lineEdit_organization.clear()

    def input_changed(self):
        self.pushButton_login.setDisabled(True)
        self.lineEdit_name.clear()
        self.lineEdit_program.clear()
        self.lineEdit_organization.clear()

    def push_advisee(self, MainWindow):
        ui = adviseelogin.Ui_Advisee()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)

    def push_admin(self, MainWindow):
        ui = adminlogin.Ui_Admin()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)

    def push_login(self):
        PasswordDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Password()
        ui.setupUi(PasswordDialog)
        PasswordDialog.exec_()
        if ui.loggedin:
            studnum = self.lineEdit_studentnumber.text()
            password = ui.lineEdit_password.text()
            if self.ses.login_peeradviser(studnum, password):
                self.smsg('Login success!')
                self.updatelist()
                self.lineEdit_name.clear()
                self.lineEdit_organization.clear()
                self.lineEdit_program.clear()
                self.lineEdit_studentnumber.clear()
            else:
                self.smsg(self.ses.errormsg)

    def push_logout(self):
        user_sn = self.listWidget.currentItem().text().split(' ')[0]
        if self.ses.logout_peeradviser(user_sn):
            self.smsg('Logout success!')
            self.updatelist()
        else:
            self.smsg(self.ses.errormsg)

    def updatelist(self):
        self.listWidget.clear()
        for adv in self.ses.peeradvisers:
            self.listWidget.addItem('{} - {}, {} {}'.format(adv.studentnumber, adv.lastname, adv.firstname, adv.middlename))
        
    def smsg(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('TutorialOn')
        #icon = QtGui.QIcon("TutorialOn.png")
        #msg.setWindowIcon(icon)
        msg.setText(message)
        msg.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ses = Session()
    ui = Ui_PeerAdviser()
    ui.connect_session(ses)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

