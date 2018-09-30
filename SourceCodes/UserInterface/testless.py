# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:28:02 2018

@author: Vince
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class adminLogin(QDialog):
    def __init__(self):
        super(adminLogin, self).__init__()
        loadUi('adminlogin.ui', self)

app = QApplication(sys.argv)
widget = adminLogin()
widget.show()
sys.exit(app.exec_())