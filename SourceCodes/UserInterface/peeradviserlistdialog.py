# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peeradviserlistdialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PeerDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 360, 211))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_select = QtWidgets.QPushButton(Dialog)
        self.pushButton_select.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.pushButton_select.setObjectName("pushButton_select")
        self.pushButton_select.clicked.connect(lambda: self.push_select(Dialog))
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(300, 250, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.clicked.connect(lambda: self.push_cancel(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_select.setText(_translate("Dialog", "Select"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        
    def connect_session(self, session):
        self.ses = session
        self.updatelist()
        
    def updatelist(self):
        self.listWidget.clear()
        for padv in self.ses.peeradvisers:
            self.listWidget.addItem('{} - {}, {} {}'.format(padv.studentnumber, padv.lastname, padv.firstname, padv.middlename))
        
    def push_select(self, Dialog):
        self.cancelled = False
        Dialog.close()
        
    def push_cancel(self, Dialog):
        self.cancelled = True
        Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_PeerDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

