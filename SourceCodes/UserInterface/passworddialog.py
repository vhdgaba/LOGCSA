# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passworddialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Password(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 146)
        
        icon = QtGui.QIcon("../Resources/logo.png")
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle("TutorialOn")
        
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(100, 50, 201, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setAutoDefault(True)
        self.pushButton_login.clicked.connect(lambda: self.push_login(Dialog))
        
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(40, 50, 61, 16))
        self.label_password.setObjectName("label_password")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TutorialOn"))
        self.pushButton_login.setText(_translate("Dialog", "Login"))
        self.label_password.setText(_translate("Dialog", "Password:"))

    def push_login(self, Dialog):
        self.loggedin = True
        Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Password()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

