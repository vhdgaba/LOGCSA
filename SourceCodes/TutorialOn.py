# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:06:49 2018

@author: Vince
"""
from UserInterface.peeradviserlogin import Ui_PeerAdviser 

from BusinessLogic.Session import Session
from PyQt5 import QtCore, QtGui, QtWidgets

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
