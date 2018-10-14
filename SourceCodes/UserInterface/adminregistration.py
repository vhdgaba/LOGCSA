# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminregistration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminRegister(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 390)
        
        icon = QtGui.QIcon("../Resources/logo.png")
        Form.setWindowIcon(icon)
        Form.setWindowTitle("TutorialOn")
        
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_name.setObjectName("label_name")
        self.lineEdit_lastname = QtWidgets.QLineEdit(Form)
        self.lineEdit_lastname.setGeometry(QtCore.QRect(10, 80, 171, 20))
        self.lineEdit_lastname.setStatusTip("")
        self.lineEdit_lastname.setWhatsThis("")
        self.lineEdit_lastname.setAccessibleName("")
        self.lineEdit_lastname.setInputMask("")
        self.lineEdit_lastname.setText("")
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.lineEdit_givenname = QtWidgets.QLineEdit(Form)
        self.lineEdit_givenname.setGeometry(QtCore.QRect(190, 80, 171, 20))
        self.lineEdit_givenname.setObjectName("lineEdit_givenname")
        self.lineEdit_middlename = QtWidgets.QLineEdit(Form)
        self.lineEdit_middlename.setGeometry(QtCore.QRect(370, 80, 171, 20))
        self.lineEdit_middlename.setObjectName("lineEdit_middlename")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 91, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setGeometry(QtCore.QRect(70, 110, 171, 20))
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.pushButton_register = QtWidgets.QPushButton(Form)
        self.pushButton_register.setGeometry(QtCore.QRect(460, 350, 75, 23))
        self.pushButton_register.setObjectName("pushButton")
        self.pushButton_register.clicked.connect(lambda: self.push_register(Form))
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(380, 350, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton")
        self.pushButton_cancel.clicked.connect(lambda: self.push_cancel(Form))
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(320, 110, 171, 20))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(260, 110, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(260, 140, 91, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_password_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_password_2.setGeometry(QtCore.QRect(320, 140, 171, 20))
        self.lineEdit_password_2.setText("")
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 41, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(70, 140, 171, 20))
        self.lineEdit_email.setText("")
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TutorialOn"))
        self.label_name.setText(_translate("Form", "Name:"))
        self.lineEdit_lastname.setPlaceholderText(_translate("Form", "Last Name"))
        self.lineEdit_givenname.setPlaceholderText(_translate("Form", "Given Name"))
        self.lineEdit_middlename.setPlaceholderText(_translate("Form", "Middle Name"))
        self.label_4.setText(_translate("Form", "Username:"))
        self.pushButton_register.setText(_translate("Form", "Register"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.label_5.setText(_translate("Form", "Password:"))
        self.label_6.setText(_translate("Form", "Password:"))
        self.label_7.setText(_translate("Form", "Mymail:"))
        self.lineEdit_email.setPlaceholderText(_translate("Form", "someone@mapua.edu.ph"))

    def connect_session(self, session):
        self.ses = session
        
    def push_register(self, form):
        if self.ses.register_admin(self.lineEdit_username.text(), self.lineEdit_givenname.text(), self.lineEdit_middlename.text(), self.lineEdit_lastname.text(), self.lineEdit_password.text(), self.lineEdit_password_2.text(), self.lineEdit_email.text()):
            self.smsg('Register success!')
            self.registered = True
            form.close()
        else:
            self.smsg(self.ses.errormsg)
    
    def push_cancel(self, form):
        self.registered = False
        form.close()

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
    Form = QtWidgets.QWidget()
    ui = Ui_AdminRegister()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

