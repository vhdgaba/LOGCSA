# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('../')
from BusinessLogic.Session import Session
from BusinessLogic.Advisee import Advisee
from PyQt5 import QtCore, QtGui, QtWidgets
from UserInterface.peeradviserlistdialog import Ui_PeerDialog
from UserInterface.adviseelistdialog import Ui_AdviseeDialog
from UserInterface import peeradviserlogin, adminlogin, adviseeregistration

ses = Session()

class Ui_Advisee(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
        
        icon = QtGui.QIcon("../Resources/logo.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle("TutorialOn")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 160, 620, 130))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.lineEdit_studentnumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_studentnumber.setGeometry(QtCore.QRect(240, 120, 151, 20))
        self.lineEdit_studentnumber.setObjectName("lineEdit_studentnumber")
        self.lineEdit_studentnumber.returnPressed.connect(lambda: self.input_sn())
        self.lineEdit_studentnumber.textChanged.connect(lambda: self.input_changed())
        
        self.radioButton_mathematics = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_mathematics.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.radioButton_mathematics.setObjectName("radioButton_mathematics")
        self.radioButton_mathematics.clicked.connect(lambda: self.select_math())
        self.radioButton_chemistry = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_chemistry.setGeometry(QtCore.QRect(120, 10, 91, 21))
        self.radioButton_chemistry.setObjectName("radioButton_chemistry")
        self.radioButton_chemistry.clicked.connect(lambda: self.select_chemistry())
        self.radioButton_physics = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_physics.setGeometry(QtCore.QRect(210, 10, 91, 21))
        self.radioButton_physics.setObjectName("radioButton_physics")
        self.radioButton_physics.clicked.connect( lambda: self.select_physics())
        self.radioButton_professional = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_professional.setGeometry(QtCore.QRect(290, 10, 121, 21))
        self.radioButton_professional.setObjectName("radioButton_professional")
        self.radioButton_professional.clicked.connect(lambda: self.select_professional())
        
        self.comboBox_coursecode = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_coursecode.setGeometry(QtCore.QRect(80, 60, 151, 22))
        self.comboBox_coursecode.setObjectName("comboBox_coursecode")
        self.comboBox_coursecode.currentTextChanged.connect(lambda: self.select_others())
        self.comboBox_coursecode.setDisabled(True)
        
        self.lineEdit_others = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_others.setGeometry(QtCore.QRect(50, 90, 181, 20))
        self.lineEdit_others.setObjectName("lineEdit_others")
        self.lineEdit_others.setDisabled(True)
        
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(630, 300, 21, 21))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_dot.setAutoDefault(True)
        self.pushButton_dot.clicked.connect(lambda: self.open_peerdialog())
        
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(700, 350, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setAutoDefault(True)
        self.pushButton_login.clicked.connect(lambda: self.push_login())
        self.pushButton_login.setDisabled(True)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(620, 350, 75, 23))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_logout.clicked.connect(lambda: self.push_logout())
        self.pushButton_logout.setAutoDefault(True)
        self.pushButton_advisee = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_advisee.setGeometry(QtCore.QRect(20, 90, 91, 23))
        self.pushButton_advisee.setObjectName("pushButton_advisee")
        self.pushButton_advisee.setAutoDefault(True)
        self.pushButton_advisee.setDown(True)
        self.pushButton_peeradviser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_peeradviser.setGeometry(QtCore.QRect(20, 120, 91, 23))
        self.pushButton_peeradviser.setObjectName("pushButton_peeradviser")
        self.pushButton_peeradviser.setAutoDefault(True)
        self.pushButton_peeradviser.clicked.connect(lambda: self.push_peeradviser(MainWindow))
        self.pushButton_admin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin.setGeometry(QtCore.QRect(20, 150, 91, 23))
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.pushButton_admin.setAutoDefault(True)
        self.pushButton_admin.clicked.connect(lambda: self.push_admin(MainWindow))
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(20, 350, 91, 23))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_register.setAutoDefault(True)
        self.pushButton_register.clicked.connect(lambda: self.push_register())
       
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(150, 90, 41, 21))
        self.label_name.setObjectName("label_name")
        self.label_program = QtWidgets.QLabel(self.centralwidget)
        self.label_program.setGeometry(QtCore.QRect(640, 90, 51, 21))
        self.label_program.setObjectName("label_program")
        self.label_studentnumber = QtWidgets.QLabel(self.centralwidget)
        self.label_studentnumber.setGeometry(QtCore.QRect(150, 120, 91, 21))
        self.label_studentnumber.setObjectName("label_studentnumber")
        self.label_coursecode = QtWidgets.QLabel(self.groupBox)
        self.label_coursecode.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_coursecode.setObjectName("label_coursecode")
        self.label_others = QtWidgets.QLabel(self.groupBox)
        self.label_others.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_others.setObjectName("label_others")
        self.label_peeradviser = QtWidgets.QLabel(self.centralwidget)
        self.label_peeradviser.setGeometry(QtCore.QRect(150, 300, 71, 21))
        self.label_peeradviser.setObjectName("label_peeradviser")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 80, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(190, 90, 431, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_program = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_program.setGeometry(QtCore.QRect(690, 90, 81, 20))
        self.lineEdit_program.setObjectName("lineEdit_program")
        self.lineEdit_program.setReadOnly(True)
        self.lineEdit_peeradviser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_peeradviser.setGeometry(QtCore.QRect(220, 300, 401, 20))
        self.lineEdit_peeradviser.setObjectName("lineEdit_peeradviser")
        self.lineEdit_peeradviser.setReadOnly(True)
        
        self.pushButton_admin.setAutoExclusive(True)
        self.pushButton_advisee.setAutoExclusive(True)
        self.pushButton_peeradviser.setAutoExclusive(True)
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "TutorialOn"))
        self.pushButton_admin.setText(_translate("MainWindow", "Administrator"))
        self.label_program.setText(_translate("MainWindow", "Program:"))
        self.radioButton_mathematics.setText(_translate("MainWindow", "Mathematics"))
        self.radioButton_chemistry.setText(_translate("MainWindow", "Chemistry"))
        self.radioButton_physics.setText(_translate("MainWindow", "Physics"))
        self.radioButton_professional.setText(_translate("MainWindow", "Professional Course"))
        self.label_coursecode.setText(_translate("MainWindow", "Course Code:"))
        self.label_others.setText(_translate("MainWindow", "Others:"))
        self.pushButton_dot.setText(_translate("MainWindow", "..."))
        self.pushButton_peeradviser.setText(_translate("MainWindow", "Peer Adviser"))
        self.label_peeradviser.setText(_translate("MainWindow", "Peer Adviser:"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_studentnumber.setText(_translate("MainWindow", "Student Number:"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.pushButton_advisee.setText(_translate("MainWindow", "Advisee"))
        self.pushButton_register.setText(_translate("MainWindow", "Register"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))

    def connect_session(self, session):
        self.ses = session

    def input_sn(self):
        user = self.ses.get_advisee(self.lineEdit_studentnumber.text())
        if user != None:
            self.pushButton_login.setEnabled(True)
            adv = Advisee(*user)
            self.lineEdit_name.setText(adv.get_fullname())
            self.lineEdit_program.setText(adv.program)
        else:
            self.lineEdit_name.clear()
            self.lineEdit_program.clear()
            self.smsg("Student number not found.")
        
    def input_changed(self):
        self.pushButton_login.setDisabled(True)
        self.lineEdit_name.clear()
        self.lineEdit_program.clear()
    
    def select_math(self):
        self.comboBox_coursecode.clear()
        self.comboBox_coursecode.setEnabled(True)
        codes = self.ses.get_subjects('Mathematics')
        for code, in codes:
            self.comboBox_coursecode.addItem(code)
        self.comboBox_coursecode.addItem('Others')
            
    def select_chemistry(self):
        self.comboBox_coursecode.clear()
        self.comboBox_coursecode.setEnabled(True)
        codes = self.ses.get_subjects('Chemistry')
        for code, in codes:
            self.comboBox_coursecode.addItem(code)
        self.comboBox_coursecode.addItem('Others')
            
    def select_physics(self):
        self.comboBox_coursecode.clear()
        self.comboBox_coursecode.setEnabled(True)
        codes = self.ses.get_subjects('Physics')
        for code, in codes:
            self.comboBox_coursecode.addItem(code)
        self.comboBox_coursecode.addItem('Others')
            
    def select_professional(self):
        self.comboBox_coursecode.clear()
        self.comboBox_coursecode.setEnabled(True)
        codes = self.ses.get_subjects('Professional')
        for code, in codes:
            self.comboBox_coursecode.addItem(code)
        self.comboBox_coursecode.addItem('Others')

    def select_others(self):
        if self.comboBox_coursecode.currentText() == 'Others':
            self.lineEdit_others.setEnabled(True)
        else:
            self.lineEdit_others.setDisabled(True)

    def open_peerdialog(self):
        PeerDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_PeerDialog()
        ui.setupUi(PeerDialog)
        ui.connect_session(self.ses)
        PeerDialog.exec_()
        if ui.cancelled:
            pass
        else:
            self.lineEdit_peeradviser.setText(ui.listWidget.currentItem().text())
        
    def select_peeradviser(self, item):
        print(item)
        
    def push_admin(self, MainWindow):
        ui = adminlogin.Ui_Admin()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)
        
    def push_peeradviser(self, MainWindow):
        ui = peeradviserlogin.Ui_PeerAdviser()
        ui.connect_session(self.ses)
        ui.setupUi(MainWindow)
        
    def push_login(self):
        if self.lineEdit_peeradviser.text() != '' and (self.radioButton_chemistry.isChecked() or self.radioButton_mathematics.isChecked() or self.radioButton_physics.isChecked() or self.radioButton_professional.isChecked()):
            if self.comboBox_coursecode.currentText() == 'Others' and self.lineEdit_others.text() == '':
                self.smsg('Please fill-up all fields!')
            else:
                if self.ses.login_advisee(self.lineEdit_studentnumber.text()):
                    Advisee(*(self.ses.get_advisee(self.lineEdit_studentnumber.text()))).time_in(self.comboBox_coursecode.currentText(), self.lineEdit_peeradviser.text().split(' ')[0])
                    self.smsg('Login Success!')
                    self.comboBox_coursecode.clear()
                    self.lineEdit_name.clear()
                    self.lineEdit_others.clear()
                    self.lineEdit_peeradviser.clear()
                    self.lineEdit_program.clear()
                    self.lineEdit_studentnumber.clear()
                    self.radioButton_chemistry.setAutoExclusive(False)
                    self.radioButton_chemistry.setChecked(False)
                    self.radioButton_mathematics.setAutoExclusive(False)
                    self.radioButton_mathematics.setChecked(False)
                    self.radioButton_physics.setAutoExclusive(False)
                    self.radioButton_physics.setChecked(False)
                    self.radioButton_professional.setAutoExclusive(False)
                    self.radioButton_professional.setChecked(False)
                    
                    self.radioButton_chemistry.setAutoExclusive(True)
                    self.radioButton_mathematics.setAutoExclusive(True)
                    self.radioButton_physics.setAutoExclusive(True)
                    self.radioButton_professional.setAutoExclusive(True)
                else:
                    self.smsg(self.ses.errormsg)
        else:
            self.smsg('Please fill-up all fields!')
            
    def push_logout(self):
        AdviseeDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_AdviseeDialog()
        ui.setupUi(AdviseeDialog)
        ui.connect_session(self.ses)
        AdviseeDialog.exec_()
            
    def push_register(self):
        registrationform = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = adviseeregistration.Ui_AdviseeRegister()
        ui.setupUi(registrationform)
        ui.connect_session(self.ses)
        registrationform.exec_()
            
    def smsg(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('TutorialOn')
        icon = QtGui.QIcon("../Resources/logo.png")
        msg.setWindowIcon(icon)
        msg.setText(message)
        msg.exec_()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Advisee()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

