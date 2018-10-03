# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adviseeregistration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdviseeRegister(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 390)
        
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
        self.lineEdit_studentnumber = QtWidgets.QLineEdit(Form)
        self.lineEdit_studentnumber.setGeometry(QtCore.QRect(100, 110, 171, 20))
        self.lineEdit_studentnumber.setText("")
        self.lineEdit_studentnumber.setObjectName("lineEdit_studentnumber")
        self.lineEdit_program = QtWidgets.QLineEdit(Form)
        self.lineEdit_program.setGeometry(QtCore.QRect(340, 110, 71, 20))
        self.lineEdit_program.setText("")
        self.lineEdit_program.setObjectName("lineEdit_program")
        self.lineEdit_address_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_1.setGeometry(QtCore.QRect(10, 220, 51, 20))
        self.lineEdit_address_1.setObjectName("lineEdit_address_1")
        self.lineEdit_address_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_2.setGeometry(QtCore.QRect(70, 220, 151, 20))
        self.lineEdit_address_2.setObjectName("lineEdit_address_2")
        self.lineEdit_address_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_3.setGeometry(QtCore.QRect(230, 220, 151, 20))
        self.lineEdit_address_3.setObjectName("lineEdit_address_3")
        self.lineEdit_address_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_4.setGeometry(QtCore.QRect(390, 220, 151, 20))
        self.lineEdit_address_4.setObjectName("lineEdit_address_4")
        self.lineEdit_address_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_5.setGeometry(QtCore.QRect(10, 250, 151, 20))
        self.lineEdit_address_5.setObjectName("lineEdit_address_5")
        self.lineEdit_address_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_address_6.setGeometry(QtCore.QRect(170, 250, 151, 20))
        self.lineEdit_address_6.setObjectName("lineEdit_address_6")
        self.lineEdit_contactnumber = QtWidgets.QLineEdit(Form)
        self.lineEdit_contactnumber.setGeometry(QtCore.QRect(100, 280, 171, 20))
        self.lineEdit_contactnumber.setText("")
        self.lineEdit_contactnumber.setObjectName("lineEdit_contactnumber")
        self.lineEdit_emailaddress = QtWidgets.QLineEdit(Form)
        self.lineEdit_emailaddress.setGeometry(QtCore.QRect(100, 310, 171, 20))
        self.lineEdit_emailaddress.setText("")
        self.lineEdit_emailaddress.setObjectName("lineEdit_emailaddress")
        
        self.pushButton_register = QtWidgets.QPushButton(Form)
        self.pushButton_register.setGeometry(QtCore.QRect(370, 350, 75, 23))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_register.setAutoDefault(True)
        self.pushButton_register.clicked.connect(lambda: self.push_register(Form))
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(460, 350, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.setAutoDefault(True)
        self.pushButton_cancel.clicked.connect(lambda: self.push_cancel(Form))
        
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_name.setObjectName("label_name")
        self.label_program = QtWidgets.QLabel(Form)
        self.label_program.setGeometry(QtCore.QRect(290, 110, 51, 21))
        self.label_program.setObjectName("label_program")
        self.label_address = QtWidgets.QLabel(Form)
        self.label_address.setGeometry(QtCore.QRect(10, 200, 51, 21))
        self.label_address.setObjectName("label_address")
        self.label_studentnumber = QtWidgets.QLabel(Form)
        self.label_studentnumber.setGeometry(QtCore.QRect(10, 110, 91, 21))
        self.label_studentnumber.setObjectName("label_studentnumber")
        self.label_contactnumber = QtWidgets.QLabel(Form)
        self.label_contactnumber.setGeometry(QtCore.QRect(10, 280, 91, 21))
        self.label_contactnumber.setObjectName("label_contactnumber")
        self.label_emailaddress = QtWidgets.QLabel(Form)
        self.label_emailaddress.setGeometry(QtCore.QRect(10, 310, 91, 21))
        self.label_emailaddress.setObjectName("label_emailaddress")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Name:"))
        self.lineEdit_lastname.setPlaceholderText(_translate("Form", "Last Name"))
        self.label_program.setText(_translate("Form", "Program:"))
        self.lineEdit_givenname.setPlaceholderText(_translate("Form", "Given Name"))
        self.label_address.setText(_translate("Form", "Address:"))
        self.lineEdit_middlename.setPlaceholderText(_translate("Form", "Middle Name"))
        self.label_studentnumber.setText(_translate("Form", "Student Number:"))
        self.lineEdit_address_2.setPlaceholderText(_translate("Form", "Street"))
        self.lineEdit_address_3.setPlaceholderText(_translate("Form", "Barangay"))
        self.lineEdit_address_4.setPlaceholderText(_translate("Form", "Town"))
        self.lineEdit_address_1.setPlaceholderText(_translate("Form", "No."))
        self.label_contactnumber.setText(_translate("Form", "Contact Number:"))
        self.label_emailaddress.setText(_translate("Form", "Mymail Address:"))
        self.lineEdit_emailaddress.setPlaceholderText(_translate("Form", "someonne@mymail.mapua.edu.ph"))
        self.pushButton_register.setText(_translate("Form", "Register"))
        self.lineEdit_address_5.setPlaceholderText(_translate("Form", "City"))
        self.lineEdit_address_6.setPlaceholderText(_translate("Form", "State"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))

    def connect_session(self, session):
        self.ses = session

    def push_register(self, form):
        if self.lineEdit_address_1.text() == '' or self.lineEdit_address_2.text() == '' or self.lineEdit_address_3.text() == '' or self.lineEdit_address_4.text() == '' or self.lineEdit_address_5.text() == '' or self.lineEdit_address_6.text() == '' or self.lineEdit_contactnumber.text() == '' or self.lineEdit_emailaddress.text() == '' or self.lineEdit_givenname.text() == '' or self.lineEdit_middlename.text() == '' or self.lineEdit_lastname.text() == '' or self.lineEdit_program.text() == '' or self.lineEdit_studentnumber.text() == '':
           self.smsg('Please fill-up all fields!') 
        else:
            homeadd = '{} {}, {}, {}, {}, {}'.format(self.lineEdit_address_1.text(), self.lineEdit_address_2.text(), self.lineEdit_address_3.text(), self.lineEdit_address_4.text(), self.lineEdit_address_5.text(), self.lineEdit_address_6.text())
            if self.ses.register_advisee(self.lineEdit_studentnumber.text(), self.lineEdit_givenname.text(), self.lineEdit_middlename.text(), self.lineEdit_lastname.text(), self.lineEdit_program.text(), self.lineEdit_contactnumber.text(), homeadd, self.lineEdit_emailaddress.text()):
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
        #icon = QtGui.QIcon("TutorialOn.png")
        #msg.setWindowIcon(icon)
        msg.setText(message)
        msg.exec_()
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AdviseeRegister()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

