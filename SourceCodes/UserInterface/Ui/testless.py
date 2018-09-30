# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:28:02 2018

@author: Vince
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
from Session import Session

class adminLogin(QMainWindow):
    def __init__(self):
        super(adminLogin, self).__init__()
        loadUi('adminlogin.ui', self)
        self.session = Session()
        self. pushButton_5.clicked.connect(lambda: self.on_pushButton_5())
        
    def on_pushButton_5(self):
        if self.session.login_admin(self.lineEdit.text(), self.lineEdit_2.text()):
            self.label.setText('G')
        else:
            self.label.setText('engk')

app = QApplication(sys.argv)
widget = adminLogin()
widget.show()
sys.exit(app.exec_())