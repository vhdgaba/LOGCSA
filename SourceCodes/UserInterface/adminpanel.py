# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminpanel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BusinessLogic.Advisee import Advisee
from BusinessLogic.PeerAdviser import PeerAdviser
from BusinessLogic.Admin import Admin
from UserInterface.passworddialog import Ui_Password
from UserInterface import peeradviserregistration, adminregistration, adviseeregistration

class Ui_AdminPanel(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 550)
        
        icon = QtGui.QIcon("../Resources/logo.png")
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle("TutorialOn")
        
        self.admin_panel = QtWidgets.QGroupBox(Dialog)
        self.admin_panel.setGeometry(QtCore.QRect(10, 90, 121, 451))
        self.admin_panel.setTitle("")
        self.admin_panel.setObjectName("admin_panel")
        self.pushButton_viewStudentInfo = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_viewStudentInfo.setGeometry(QtCore.QRect(10, 40, 101, 41))
        self.pushButton_viewStudentInfo.setAutoExclusive(True)
        self.pushButton_viewStudentInfo.setObjectName("pushButton_viewStudentInfo")
        self.pushButton_viewStudentInfo.clicked.connect(lambda: self.push_vsi())
        self.pushButton_viewSessionLog = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_viewSessionLog.setGeometry(QtCore.QRect(10, 80, 101, 41))
        self.pushButton_viewSessionLog.setAutoExclusive(True)
        self.pushButton_viewSessionLog.setObjectName("pushButton_viewSessionLog")
        self.pushButton_viewSessionLog.clicked.connect(lambda: self.push_vsl())
        self.pushButton_viewTimeSheetLog = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_viewTimeSheetLog.setGeometry(QtCore.QRect(10, 120, 101, 41))
        self.pushButton_viewTimeSheetLog.setAutoExclusive(True)
        self.pushButton_viewTimeSheetLog.setObjectName("pushButton_viewTimeSheetLog")
        self.pushButton_viewTimeSheetLog.clicked.connect(lambda: self.push_vts())
        self.pushButton_add = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_add.setGeometry(QtCore.QRect(10, 160, 101, 41))
        self.pushButton_add.setAutoExclusive(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.clicked.connect(lambda:self.push_add())
        self.pushButton_email = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_email.setGeometry(QtCore.QRect(10, 200, 101, 41))
        self.pushButton_email.setAutoExclusive(True)
        self.pushButton_email.setObjectName("pushButton_email")
        self.pushButton_email.clicked.connect(lambda:self.push_email())
        self.pushButton_logout = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_logout.setGeometry(QtCore.QRect(10, 360, 101, 41))
        self.pushButton_logout.setAutoExclusive(True)
        self.pushButton_logout.setObjectName("pushButton_viewEvaluation")
        self.pushButton_logout.clicked.connect(lambda:self.push_logout(Dialog))
        self.pushButton_clearDatabase = QtWidgets.QPushButton(self.admin_panel)
        self.pushButton_clearDatabase.setGeometry(QtCore.QRect(10, 400, 101, 41))
        self.pushButton_clearDatabase.setAutoExclusive(True)
        self.pushButton_clearDatabase.setObjectName("pushButton_clearDatabase")
        self.pushButton_clearDatabase.clicked.connect(lambda: self.push_clear())
        self.label_adminPanel = QtWidgets.QLabel(self.admin_panel)
        self.label_adminPanel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_adminPanel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adminPanel.setObjectName("label_adminPanel")
        
        self.vsi_panel = QtWidgets.QGroupBox(Dialog)
        self.vsi_panel.setGeometry(QtCore.QRect(140, 90, 651, 451))
        self.vsi_panel.setTitle("")
        self.vsi_panel.setObjectName("vsi_panel")
        self.radioButton_vsi_advisee = QtWidgets.QRadioButton(self.vsi_panel)
        self.radioButton_vsi_advisee.setGeometry(QtCore.QRect(50, 40, 91, 17))
        self.radioButton_vsi_advisee.setObjectName("radioButton_vsi_advisee")
        self.radioButton_vsi_advisee.setChecked(True)
        self.radioButton_vsi_advisee.toggled.connect(lambda: self.toggle_vsia())
        self.radioButton_vsi_peeradviser = QtWidgets.QRadioButton(self.vsi_panel)
        self.radioButton_vsi_peeradviser.setGeometry(QtCore.QRect(150, 40, 91, 17))
        self.radioButton_vsi_peeradviser.setObjectName("radioButton_vsi_peeradviser")
        self.radioButton_vsi_advisee.toggled.connect(lambda: self.toggle_vsip())
        self.lineEdit_vsi_studentnumber = QtWidgets.QLineEdit(self.vsi_panel)
        self.lineEdit_vsi_studentnumber.setGeometry(QtCore.QRect(52, 70, 109, 21))
        self.lineEdit_vsi_studentnumber.setObjectName("lineEdit_vsi_studentnumber")
        self.lineEdit_vsi_studentnumber.returnPressed.connect(lambda: self.push_vsi_search())
        self.lineEdit_vsi_studentnumber.textChanged.connect(lambda: self.vsi_clear())
        self.pushButton_vsi_search = QtWidgets.QPushButton(self.vsi_panel)
        self.pushButton_vsi_search.setEnabled(True)
        self.pushButton_vsi_search.setGeometry(QtCore.QRect(160, 69, 51, 23))
        self.pushButton_vsi_search.setObjectName("pushButton_vsi_search")
        self.pushButton_vsi_search.clicked.connect(lambda: self.push_vsi_search())
        self.groupBox_vsia = QtWidgets.QGroupBox(self.vsi_panel)
        self.groupBox_vsia.setEnabled(True)
        self.groupBox_vsia.setGeometry(QtCore.QRect(30, 120, 591, 131))
        self.groupBox_vsia.setObjectName("groupBox_vsia")
        self.xx_3 = QtWidgets.QLabel(self.groupBox_vsia)
        self.xx_3.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.xx_3.setObjectName("xx_3")
        self.xx = QtWidgets.QLabel(self.groupBox_vsia)
        self.xx.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.xx.setObjectName("xx")
        self.xx_2 = QtWidgets.QLabel(self.groupBox_vsia)
        self.xx_2.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.xx_2.setObjectName("xx_2")
        self.xx_4 = QtWidgets.QLabel(self.groupBox_vsia)
        self.xx_4.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.xx_4.setObjectName("xx_4")
        self.xx_5 = QtWidgets.QLabel(self.groupBox_vsia)
        self.xx_5.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.xx_5.setObjectName("xx_5")
        self.label_vsia_name = QtWidgets.QLabel(self.groupBox_vsia)
        self.label_vsia_name.setGeometry(QtCore.QRect(110, 20, 200, 16))
        self.label_vsia_name.setText("")
        self.label_vsia_name.setObjectName("label_vsia_name")
        self.label_vsia_program = QtWidgets.QLabel(self.groupBox_vsia)
        self.label_vsia_program.setGeometry(QtCore.QRect(110, 40, 200, 16))
        self.label_vsia_program.setText("")
        self.label_vsia_program.setObjectName("label_vsia_program")
        self.label_vsia_contactnumber = QtWidgets.QLabel(self.groupBox_vsia)
        self.label_vsia_contactnumber.setGeometry(QtCore.QRect(110, 60, 200, 16))
        self.label_vsia_contactnumber.setText("")
        self.label_vsia_contactnumber.setObjectName("label_vsia_contactnumber")
        self.label_vsia_emailaddress = QtWidgets.QLabel(self.groupBox_vsia)
        self.label_vsia_emailaddress.setGeometry(QtCore.QRect(110, 80, 200, 16))
        self.label_vsia_emailaddress.setText("")
        self.label_vsia_emailaddress.setObjectName("label_vsia_emailaddress")
        self.label_vsia_homeaddress = QtWidgets.QLabel(self.groupBox_vsia)
        self.label_vsia_homeaddress.setGeometry(QtCore.QRect(110, 100, 200, 16))
        self.label_vsia_homeaddress.setText("")
        self.label_vsia_homeaddress.setObjectName("label_vsia_homeaddress")
        self.xx_3.raise_()
        self.xx.raise_()
        self.xx_2.raise_()
        self.xx_4.raise_()
        self.xx_5.raise_()
        self.label_vsia_name.raise_()
        self.label_vsia_program.raise_()
        self.label_vsia_contactnumber.raise_()
        self.label_vsia_emailaddress.raise_()
        self.label_vsia_homeaddress.raise_()
        self.groupBox_vsip = QtWidgets.QGroupBox(self.vsi_panel)
        self.groupBox_vsip.setGeometry(QtCore.QRect(30, 120, 591, 161))
        self.groupBox_vsip.setObjectName("groupBox_vsip")
        self.groupBox_vsip.setVisible(False)
        self.xx_7 = QtWidgets.QLabel(self.groupBox_vsip)
        self.xx_7.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.xx_7.setObjectName("xx_7")
        self.xx_8 = QtWidgets.QLabel(self.groupBox_vsip)
        self.xx_8.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.xx_8.setObjectName("xx_8")
        self.xx_9 = QtWidgets.QLabel(self.groupBox_vsip)
        self.xx_9.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.xx_9.setObjectName("xx_9")
        self.xx_10 = QtWidgets.QLabel(self.groupBox_vsip)
        self.xx_10.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.xx_10.setObjectName("xx_10")
        self.label_vsip_name = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_name.setGeometry(QtCore.QRect(110, 20, 200, 16))
        self.label_vsip_name.setText("")
        self.label_vsip_name.setObjectName("label_vsip_name")
        self.label_vsip_program = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_program.setGeometry(QtCore.QRect(110, 40, 200, 16))
        self.label_vsip_program.setText("")
        self.label_vsip_program.setObjectName("label_vsip_program")
        self.label_vsip_contactnumber = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_contactnumber.setGeometry(QtCore.QRect(110, 60, 200, 16))
        self.label_vsip_contactnumber.setText("")
        self.label_vsip_contactnumber.setObjectName("label_vsip_contactnumber")
        self.label_vsip_organization = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_organization.setGeometry(QtCore.QRect(110, 80, 200, 16))
        self.label_vsip_organization.setText("")
        self.label_vsip_organization.setObjectName("label_vsip_organization")
        self.xx_11 = QtWidgets.QLabel(self.groupBox_vsip)
        self.xx_11.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.xx_11.setObjectName("xx_11")
        self.label_vsip_advisingschedule_1 = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_advisingschedule_1.setGeometry(QtCore.QRect(110, 100, 200, 16))
        self.label_vsip_advisingschedule_1.setText("")
        self.label_vsip_advisingschedule_1.setObjectName("label_vsip_advisingschedule_1")
        self.label_vsip_advisingschedule_2 = QtWidgets.QLabel(self.groupBox_vsip)
        self.label_vsip_advisingschedule_2.setGeometry(QtCore.QRect(110, 120, 200, 16))
        self.label_vsip_advisingschedule_2.setText("")
        self.label_vsip_advisingschedule_2.setObjectName("label_vsip_advisingschedule_2")
        self.pushButton_vsi_delete = QtWidgets.QPushButton(self.vsi_panel)
        self.pushButton_vsi_delete.setEnabled(True)
        self.pushButton_vsi_delete.setGeometry(QtCore.QRect(540, 290, 81, 21))
        self.pushButton_vsi_delete.setObjectName("pushButton_vsi_delete")
        self.vsl_panel = QtWidgets.QGroupBox(Dialog)
        self.vsl_panel.setGeometry(QtCore.QRect(140, 90, 651, 451))
        self.vsl_panel.setTitle("")
        self.vsl_panel.setObjectName("vsl_panel")
        self.radioButton_vsl_searchByDate = QtWidgets.QRadioButton(self.vsl_panel)
        self.radioButton_vsl_searchByDate.setGeometry(QtCore.QRect(70, 40, 91, 17))
        self.radioButton_vsl_searchByDate.setObjectName("radioButton_vsl_searchByDate")
        self.radioButton_vsl_searchByDate.toggled.connect(lambda: self.toggle_vsl_searchByDate())
        self.radioButton_vsl_searchByDate.setChecked(True)
        self.radioButton_vsl_searchByStudentNumber = QtWidgets.QRadioButton(self.vsl_panel)
        self.radioButton_vsl_searchByStudentNumber.setGeometry(QtCore.QRect(70, 70, 181, 17))
        self.radioButton_vsl_searchByStudentNumber.setObjectName("radioButton_vsl_searchByStudentNumber")
        self.radioButton_vsl_searchByStudentNumber.toggled.connect(lambda: self.toggle_vsl_searchByStudentNumber())
        self.lineEdit_vsl_studentnumber = QtWidgets.QLineEdit(self.vsl_panel)
        self.lineEdit_vsl_studentnumber.setEnabled(False)
        self.lineEdit_vsl_studentnumber.setGeometry(QtCore.QRect(230, 71, 109, 21))
        self.lineEdit_vsl_studentnumber.setObjectName("lineEdit_vsl_studentnumber")
        self.pushButton_vsl_search = QtWidgets.QPushButton(self.vsl_panel)
        self.pushButton_vsl_search.setEnabled(True)
        self.pushButton_vsl_search.setGeometry(QtCore.QRect(490, 40, 81, 51))
        self.pushButton_vsl_search.setObjectName("pushButton_vsl_search")
        self.pushButton_vsl_search.clicked.connect(lambda: self.push_vsl_search())
        self.dateEdit_vsl = QtWidgets.QDateEdit(self.vsl_panel)
        self.dateEdit_vsl.setEnabled(True)
        self.dateEdit_vsl.setGeometry(QtCore.QRect(230, 41, 109, 22))
        self.dateEdit_vsl.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_vsl.setObjectName("dateEdit_vsl")
        self.tableWidget_vslbsn = QtWidgets.QTableWidget(self.vsl_panel)
        self.tableWidget_vslbsn.setGeometry(QtCore.QRect(45, 110, 550, 311))
        self.tableWidget_vslbsn.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_vslbsn.setAlternatingRowColors(True)
        self.tableWidget_vslbsn.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_vslbsn.setObjectName("tableWidget_vslbsn")
        self.tableWidget_vslbsn.setColumnCount(5)
        self.tableWidget_vslbsn.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbsn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbsn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbsn.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbsn.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbsn.setHorizontalHeaderItem(4, item)
        self.tableWidget_vslbd = QtWidgets.QTableWidget(self.vsl_panel)
        self.tableWidget_vslbd.setGeometry(QtCore.QRect(45, 110, 550, 311))
        self.tableWidget_vslbd.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_vslbd.setAlternatingRowColors(True)
        self.tableWidget_vslbd.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_vslbd.setObjectName("tableWidget_vslbd")
        self.tableWidget_vslbd.setColumnCount(5)
        self.tableWidget_vslbd.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbd.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbd.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vslbd.setHorizontalHeaderItem(4, item)
        self.tableWidget_vslbsn.raise_()
        self.tableWidget_vslbd.raise_()
        self.radioButton_vsl_searchByDate.raise_()
        self.radioButton_vsl_searchByStudentNumber.raise_()
        self.lineEdit_vsl_studentnumber.raise_()
        self.pushButton_vsl_search.raise_()
        self.dateEdit_vsl.raise_()
        self.vts_panel = QtWidgets.QGroupBox(Dialog)
        self.vts_panel.setGeometry(QtCore.QRect(140, 90, 651, 451))
        self.vts_panel.setTitle("")
        self.vts_panel.setObjectName("vts_panel")
        self.radioButton_vts_searchByDate = QtWidgets.QRadioButton(self.vts_panel)
        self.radioButton_vts_searchByDate.setGeometry(QtCore.QRect(100, 40, 91, 17))
        self.radioButton_vts_searchByDate.setObjectName("radioButton_vts_searchByDate")
        self.radioButton_vts_searchByDate.toggled.connect(lambda: self.toggle_vts_searchByDate())
        self.radioButton_vts_searchByDate.setChecked(True)
        self.radioButton_vts_searchByStudentNumber = QtWidgets.QRadioButton(self.vts_panel)
        self.radioButton_vts_searchByStudentNumber.setGeometry(QtCore.QRect(100, 70, 171, 17))
        self.radioButton_vts_searchByStudentNumber.setObjectName("radioButton_vts_searchByStudentNumber")
        self.radioButton_vts_searchByStudentNumber.toggled.connect(lambda: self.toggle_vts_searchByStudentNumber())
        self.lineEdit_vts_studentnumber = QtWidgets.QLineEdit(self.vts_panel)
        self.lineEdit_vts_studentnumber.setEnabled(False)
        self.lineEdit_vts_studentnumber.setGeometry(QtCore.QRect(270, 71, 109, 21))
        self.lineEdit_vts_studentnumber.setObjectName("lineEdit_vts_studentnumber")
        self.pushButton_vts_search = QtWidgets.QPushButton(self.vts_panel)
        self.pushButton_vts_search.setEnabled(True)
        self.pushButton_vts_search.setGeometry(QtCore.QRect(430, 40, 81, 51))
        self.pushButton_vts_search.setObjectName("pushButton_vts_search")
        self.pushButton_vts_search.clicked.connect(lambda: self.push_vts_search())
        self.dateEdit_vts = QtWidgets.QDateEdit(self.vts_panel)
        self.dateEdit_vts.setEnabled(True)
        self.dateEdit_vts.setGeometry(QtCore.QRect(270, 41, 109, 22))
        self.dateEdit_vts.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_vts.setObjectName("dateEdit_vts")
        self.tableWidget_vtsbsn = QtWidgets.QTableWidget(self.vts_panel)
        self.tableWidget_vtsbsn.setGeometry(QtCore.QRect(125, 110, 342, 311))
        self.tableWidget_vtsbsn.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_vtsbsn.setAlternatingRowColors(True)
        self.tableWidget_vtsbsn.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_vtsbsn.setObjectName("tableWidget_vtsbsn")
        self.tableWidget_vtsbsn.setColumnCount(3)
        self.tableWidget_vtsbsn.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbsn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbsn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbsn.setHorizontalHeaderItem(2, item)
        self.tableWidget_vtsbd = QtWidgets.QTableWidget(self.vts_panel)
        self.tableWidget_vtsbd.setGeometry(QtCore.QRect(125, 110, 342, 311))
        self.tableWidget_vtsbd.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_vtsbd.setAlternatingRowColors(True)
        self.tableWidget_vtsbd.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_vtsbd.setObjectName("tableWidget_vtsbd")
        self.tableWidget_vtsbd.setColumnCount(3)
        self.tableWidget_vtsbd.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vtsbd.setHorizontalHeaderItem(2, item)
        self.add_panel = QtWidgets.QGroupBox(Dialog)
        self.add_panel.setGeometry(QtCore.QRect(140, 90, 651, 451))
        self.add_panel.setTitle("")
        
        self.add_panel.setObjectName("add_panel")
        self.radioButton_a_peeradviser = QtWidgets.QRadioButton(self.add_panel)
        self.radioButton_a_peeradviser.setGeometry(QtCore.QRect(170, 190, 91, 17))
        self.radioButton_a_peeradviser.setObjectName("radioButton_a_peeradviser")
        self.radioButton_a_admin = QtWidgets.QRadioButton(self.add_panel)
        self.radioButton_a_admin.setGeometry(QtCore.QRect(170, 220, 91, 17))
        self.radioButton_a_admin.setObjectName("radioButton_a_admin")
        self.pushButton_a_register = QtWidgets.QPushButton(self.add_panel)
        self.pushButton_a_register.setEnabled(True)
        self.pushButton_a_register.setGeometry(QtCore.QRect(350, 180, 71, 41))
        self.pushButton_a_register.setObjectName("pushButton_a_register")
        self.pushButton_a_register.clicked.connect(lambda: self.push_a_register())
        self.radioButton_a_advisee = QtWidgets.QRadioButton(self.add_panel)
        self.radioButton_a_advisee.setGeometry(QtCore.QRect(170, 160, 91, 17))
        self.radioButton_a_advisee.setObjectName("radioButton_a_advisee")
        self.radioButton_a_advisee.setChecked(True)
        self.xx_26 = QtWidgets.QLabel(self.add_panel)
        self.xx_26.setGeometry(QtCore.QRect(170, 130, 241, 16))
        self.xx_26.setObjectName("xx_26")
        self.email_panel = QtWidgets.QGroupBox(Dialog)
        self.email_panel.setGeometry(QtCore.QRect(140, 90, 651, 451))
        self.email_panel.setTitle("")
        self.email_panel.setObjectName("email_panel")
        self.radioButton_e_allPeerAdvisers = QtWidgets.QRadioButton(self.email_panel)
        self.radioButton_e_allPeerAdvisers.setGeometry(QtCore.QRect(220, 30, 161, 16))
        self.radioButton_e_allPeerAdvisers.setObjectName("radioButton_e_allPeerAdvisers")
        self.radioButton_e_allAdvisees = QtWidgets.QRadioButton(self.email_panel)
        self.radioButton_e_allAdvisees.setGeometry(QtCore.QRect(120, 30, 80, 16))
        self.radioButton_e_allAdvisees.setObjectName("radioButton_e_allAdvisees")
        self.radioButton_e_allAdvisees.setChecked(True)
        self.radioButton_e_allPeerAdvisers.raise_()
        self.radioButton_e_allAdvisees.raise_()
        self.pushButton_e_send = QtWidgets.QPushButton(self.email_panel)
        self.pushButton_e_send.setEnabled(True)
        self.pushButton_e_send.setGeometry(QtCore.QRect(290, 370, 81, 31))
        self.pushButton_e_send.setObjectName("pushButton_e_send")
        self.pushButton_e_send.clicked.connect(lambda: self.push_e_send())
        self.lineEdit_e_subject = QtWidgets.QLineEdit(self.email_panel)
        self.lineEdit_e_subject.setGeometry(QtCore.QRect(90, 60, 521, 20))
        self.lineEdit_e_subject.setObjectName("lineEdit_e_subject")
        self.textEdit_e_body = QtWidgets.QTextEdit(self.email_panel)
        self.textEdit_e_body.setGeometry(QtCore.QRect(40, 120, 571, 241))
        self.textEdit_e_body.setObjectName("textEdit_e_body")
        self.xx_39 = QtWidgets.QLabel(self.email_panel)
        self.xx_39.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.xx_39.setObjectName("xx_39")
        self.xx_40 = QtWidgets.QLabel(self.email_panel)
        self.xx_40.setGeometry(QtCore.QRect(40, 100, 41, 16))
        self.xx_40.setObjectName("xx_40")
        self.xx_38 = QtWidgets.QLabel(self.email_panel)
        self.xx_38.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.xx_38.setObjectName("xx_38")
        self.hide_panels()
        self.vsi_panel.setVisible(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TutorialOn"))
        self.pushButton_viewSessionLog.setText(_translate("Dialog", "View\n"
"Session Log"))
        self.pushButton_viewTimeSheetLog.setText(_translate("Dialog", "View\n"
"Timesheet Log"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_clearDatabase.setText(_translate("Dialog", "Clear Database"))
        self.pushButton_email.setText(_translate("Dialog", "Email"))
        self.pushButton_logout.setText(_translate("Dialog", "Logout"))
        self.label_adminPanel.setText(_translate("Dialog", "Admin Panel"))
        self.pushButton_viewStudentInfo.setText(_translate("Dialog", "View\n"
"Student Info"))
        self.radioButton_vsi_advisee.setText(_translate("Dialog", "Advisee"))
        self.radioButton_vsi_peeradviser.setText(_translate("Dialog", "Peer Adviser"))
        self.lineEdit_vsi_studentnumber.setPlaceholderText(_translate("Dialog", "Student Number"))
        self.pushButton_vsi_search.setText(_translate("Dialog", "Search"))
        self.groupBox_vsia.setTitle(_translate("Dialog", "Student Information"))
        self.xx_3.setText(_translate("Dialog", "Home Address:"))
        self.xx.setText(_translate("Dialog", "Name:"))
        self.xx_2.setText(_translate("Dialog", "Program:"))
        self.xx_4.setText(_translate("Dialog", "Email Address:"))
        self.xx_5.setText(_translate("Dialog", "Contact Number:"))
        self.groupBox_vsip.setTitle(_translate("Dialog", "Student Information"))
        self.xx_7.setText(_translate("Dialog", "Name:"))
        self.xx_8.setText(_translate("Dialog", "Program:"))
        self.xx_9.setText(_translate("Dialog", "Organization:"))
        self.xx_10.setText(_translate("Dialog", "Contact Number:"))
        self.xx_11.setText(_translate("Dialog", "Advising Schedule:"))
        self.pushButton_vsi_delete.setText(_translate("Dialog", "Delete User"))
        self.radioButton_vsl_searchByDate.setText(_translate("Dialog", "Search by date"))
        self.radioButton_vsl_searchByStudentNumber.setText(_translate("Dialog", "Search by student number"))
        self.lineEdit_vsl_studentnumber.setPlaceholderText(_translate("Dialog", "Student Number"))
        self.pushButton_vsl_search.setText(_translate("Dialog", "Search"))
        item = self.tableWidget_vslbsn.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget_vslbsn.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Time in"))
        item = self.tableWidget_vslbsn.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time out"))
        item = self.tableWidget_vslbsn.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Subject"))
        item = self.tableWidget_vslbsn.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Peer Adviser"))
        item = self.tableWidget_vslbd.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student Number"))
        item = self.tableWidget_vslbd.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Time in"))
        item = self.tableWidget_vslbd.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time out"))
        item = self.tableWidget_vslbd.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Subject"))
        item = self.tableWidget_vslbd.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Peer Adviser"))
        self.radioButton_vts_searchByDate.setText(_translate("Dialog", "Search by date"))
        self.radioButton_vts_searchByStudentNumber.setText(_translate("Dialog", "Search by student number"))
        self.lineEdit_vts_studentnumber.setPlaceholderText(_translate("Dialog", "Student Number"))
        self.pushButton_vts_search.setText(_translate("Dialog", "Search"))
        item = self.tableWidget_vtsbsn.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget_vtsbsn.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Time in"))
        item = self.tableWidget_vtsbsn.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time out"))
        item = self.tableWidget_vtsbd.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student Number"))
        item = self.tableWidget_vtsbd.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Time in"))
        item = self.tableWidget_vtsbd.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time out"))
        self.radioButton_a_peeradviser.setText(_translate("Dialog", "Peer Adviser"))
        self.radioButton_a_admin.setText(_translate("Dialog", "Admin"))
        self.pushButton_a_register.setText(_translate("Dialog", "Register"))
        self.radioButton_a_advisee.setText(_translate("Dialog", "Advisee"))
        self.xx_26.setText(_translate("Dialog", "Choose a user type to register:"))
        self.radioButton_e_allAdvisees.setText(_translate("Dialog", "All Advisees"))
        self.radioButton_e_allPeerAdvisers.setText(_translate("Dialog", "All Peer Advisers"))
        self.pushButton_e_send.setText(_translate("Dialog", "Send"))
        self.xx_39.setText(_translate("Dialog", "Subject:"))
        self.xx_40.setText(_translate("Dialog", "Body"))
        self.xx_38.setText(_translate("Dialog", "Recipient:"))

    def connect_session(self, session):
        self.ses = session
        self.admin = self.ses.admin

    def hide_panels(self):
        self.vsi_panel.setVisible(False)
        self.vsl_panel.setVisible(False)
        self.vts_panel.setVisible(False)
        self.add_panel.setVisible(False)
        self.email_panel.setVisible(False)
        
    #View Student Information Panel Functions
    
    def vsi_clear(self):
        self.label_vsia_name.clear()
        self.label_vsia_program.clear()
        self.label_vsia_contactnumber.clear()
        self.label_vsia_homeaddress.clear()
        self.label_vsia_emailaddress.clear()
        self.label_vsip_name.clear()
        self.label_vsip_program.clear()
        self.label_vsip_organization.clear()
        self.label_vsip_contactnumber.clear()
        self.label_vsip_advisingschedule_1.clear()
        self.label_vsip_advisingschedule_2.clear()
    
    def push_vsi(self):
        self.hide_panels()
        self.vsi_panel.setVisible(True)
        self.radioButton_vsi_advisee.setChecked(True)
        self.groupBox_vsip.setVisible(False)
        self.lineEdit_vsi_studentnumber.clear()
        self.vsi_clear()
        
    def toggle_vsia(self):
        if self.radioButton_vsi_advisee.isChecked():
            self.groupBox_vsia.setVisible(True)      
        else:
            self.groupBox_vsia.setVisible(False) 
    
    def toggle_vsip(self):
        if self.radioButton_vsi_peeradviser.isChecked():
            self.groupBox_vsip.setVisible(True)      
        else:
            self.groupBox_vsip.setVisible(False) 
        
    def push_vsi_search(self):
        studentnumber = self.lineEdit_vsi_studentnumber.text()
        if self.radioButton_vsi_advisee.isChecked():
            if self.ses.get_advisee(studentnumber) != None:
                adv = Advisee(*self.ses.get_advisee(studentnumber))
                self.label_vsia_name.setText(adv.get_fullname())
                self.label_vsia_program.setText(adv.program)
                self.label_vsia_contactnumber.setText(adv.contactnumber)
                self.label_vsia_homeaddress.setText(adv.homeaddress)
                self.label_vsia_emailaddress.setText(adv.emailaddress)
            else:
                self.vsi_clear()
                self.smsg("Error: Student not found.")
        else:
            if self.ses.get_peeradviser(studentnumber) != None:
                padv = PeerAdviser(*self.ses.get_peeradviser(studentnumber))
                self.label_vsip_name.setText(padv.get_fullname())
                self.label_vsip_program.setText(padv.program)
                self.label_vsip_organization.setText(padv.program)
                self.label_vsip_contactnumber.setText(padv.contactnumber)
                self.label_vsip_advisingschedule_1.setText(padv.get_schedule()[0])
                self.label_vsip_advisingschedule_2.setText(padv.get_schedule()[1])
            else:
                self.vsi_clear()
                self.smsg("Error: Student not found.")
    
    #View Session Log Panel Functions
        
    def push_vsl(self):
        self.hide_panels()
        self.vsl_panel.setVisible(True)
            
    def toggle_vsl_searchByDate(self):
        self.tableWidget_vslbd.setRowCount(0)
        if self.radioButton_vsl_searchByDate.isChecked():
            self.dateEdit_vsl.setEnabled(True)      
            self.tableWidget_vslbd.setVisible(True)
        else:
            self.dateEdit_vsl.setEnabled(False)
            self.tableWidget_vslbd.setVisible(False)
    
    def toggle_vsl_searchByStudentNumber(self):
        self.lineEdit_vsl_studentnumber.clear()
        self.tableWidget_vslbsn.setRowCount(0)
        if self.radioButton_vsl_searchByStudentNumber.isChecked():
            self.lineEdit_vsl_studentnumber.setEnabled(True)
            self.tableWidget_vslbsn.setVisible(True)
        else:
            self.lineEdit_vsl_studentnumber.setEnabled(False)     
            self.tableWidget_vslbsn.setVisible(False)
            
    def push_vsl_search(self):
        if self.radioButton_vsl_searchByDate.isChecked():
            month, day, year = self.dateEdit_vsl.text().split('/')
            if len(month) == 1:
                month = '0' + month
            if len(day) == 1:
                day = '0' + day
            date = month + '-' + day + '-' + year
            count = len(self.admin.get_dailysessionlog(date))
            self.tableWidget_vslbd.setRowCount(count)
            if count > 0:
                column = 0
                for studentnumber, timein, timeout, subject, adviserid in self.admin.get_dailysessionlog(date):     
                    self.tableWidget_vslbd.setItem(column, 0, QtWidgets.QTableWidgetItem(str(studentnumber)))
                    self.tableWidget_vslbd.setItem(column, 1, QtWidgets.QTableWidgetItem(timein))
                    self.tableWidget_vslbd.setItem(column, 2, QtWidgets.QTableWidgetItem(timeout))
                    self.tableWidget_vslbd.setItem(column, 3, QtWidgets.QTableWidgetItem(subject))
                    self.tableWidget_vslbd.setItem(column, 4, QtWidgets.QTableWidgetItem(str(adviserid)))
                    column += 1
            else:
                self.smsg("No record.")
        else:
            studentnumber = self.lineEdit_vsl_studentnumber.text()
            count = len(self.admin.get_studentsessionlog(studentnumber))
            self.tableWidget_vslbsn.setRowCount(count)
            if count > 0:
                column = 0
                for date, timein, timeout, subject, adviserid in self.admin.get_studentsessionlog(studentnumber):     
                    self.tableWidget_vslbsn.setItem(column, 0, QtWidgets.QTableWidgetItem(date))
                    self.tableWidget_vslbsn.setItem(column, 1, QtWidgets.QTableWidgetItem(timein))
                    self.tableWidget_vslbsn.setItem(column, 2, QtWidgets.QTableWidgetItem(timeout))
                    self.tableWidget_vslbsn.setItem(column, 3, QtWidgets.QTableWidgetItem(subject))
                    self.tableWidget_vslbsn.setItem(column, 4, QtWidgets.QTableWidgetItem(str(adviserid)))
                    column += 1
            else:
                self.smsg("No record.")
                
    #View Timesheet Log Panel Functions
        
    def push_vts(self):
        self.hide_panels()
        self.vts_panel.setVisible(True)
        
    def toggle_vts_searchByDate(self):
        self.tableWidget_vtsbd.setRowCount(0)
        if self.radioButton_vts_searchByDate.isChecked():
            self.dateEdit_vts.setEnabled(True)      
            self.tableWidget_vtsbd.setVisible(True)
        else:
            self.dateEdit_vts.setEnabled(False)
            self.tableWidget_vtsbd.setVisible(False)
    
    def toggle_vts_searchByStudentNumber(self):
        self.lineEdit_vts_studentnumber.clear()
        self.tableWidget_vtsbsn.setRowCount(0)
        if self.radioButton_vts_searchByStudentNumber.isChecked():
            self.lineEdit_vts_studentnumber.setEnabled(True)
            self.tableWidget_vtsbsn.setVisible(True)
        else:
            self.lineEdit_vts_studentnumber.setEnabled(False)     
            self.tableWidget_vtsbsn.setVisible(False)
            
    def push_vts_search(self):
        if self.radioButton_vts_searchByDate.isChecked():
            month, day, year = self.dateEdit_vts.text().split('/')
            if len(month) == 1:
                month = '0' + month
            if len(day) == 1:
                day = '0' + day
            date = month + '-' + day + '-' + year
            count = len(self.admin.get_dailytimesheet(date))
            self.tableWidget_vtsbd.setRowCount(count)
            if count > 0:
                column = 0
                for studentnumber, timein, timeout in self.admin.get_dailytimesheet(date):     
                    self.tableWidget_vtsbd.setItem(column, 0, QtWidgets.QTableWidgetItem(str(studentnumber)))
                    self.tableWidget_vtsbd.setItem(column, 1, QtWidgets.QTableWidgetItem(timein))
                    self.tableWidget_vtsbd.setItem(column, 2, QtWidgets.QTableWidgetItem(timeout))
                    column += 1
            else:
                self.smsg("No record.")
        else:
            studentnumber = self.lineEdit_vts_studentnumber.text()
            count = len(self.admin.get_studenttimesheet(studentnumber))
            self.tableWidget_vtsbsn.setRowCount(count)
            if count > 0:
                column = 0
                for date, timein, timeout in self.admin.get_studenttimesheet(studentnumber):     
                    self.tableWidget_vtsbsn.setItem(column, 0, QtWidgets.QTableWidgetItem(date))
                    self.tableWidget_vtsbsn.setItem(column, 1, QtWidgets.QTableWidgetItem(timein))
                    self.tableWidget_vtsbsn.setItem(column, 2, QtWidgets.QTableWidgetItem(timeout))
                    column += 1
            else:
                self.smsg("No record.")
        
    #Add user panel functions
        
    def push_add(self):
        self.hide_panels()
        self.add_panel.setVisible(True)
        
        
    def push_a_register(self):
        if self.radioButton_a_admin.isChecked():
            registrationform = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
            ui = adminregistration.Ui_AdminRegister()
            ui.setupUi(registrationform)
            ui.connect_session(self.admin)
            registrationform.exec_()
        elif self.radioButton_a_advisee.isChecked():
            registrationform = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
            ui = adviseeregistration.Ui_AdviseeRegister()
            ui.setupUi(registrationform)
            ui.connect_session(self.ses)
            registrationform.exec_()
        else:
            registrationform = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
            ui = peeradviserregistration.Ui_PeerAdviserRegister()
            ui.setupUi(registrationform)
            ui.connect_session(self.admin)
            registrationform.exec_()
        
    #Send email panel functions
        
    def push_email(self):
        self.hide_panels()
        self.email_panel.setVisible(True)
        
    def push_e_send(self):
        
        PasswordDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Password()
        ui.setupUi(PasswordDialog)
        PasswordDialog.exec_()
        if ui.loggedin:
            password = ui.lineEdit_password.text()
            if self.radioButton_e_allAdvisees.isChecked():
                drop = self.admin.email_advisee(password, self.lineEdit_e_subject.text(), self.textEdit_e_body.toPlainText())
                if drop != 0:
                    self.smsg(drop + " messages failed to send.")
                else:
                    self.smsg("Message sent succesfully to all recepients")
            else:
                drop = self.admin.email_adviser(password, self.lineEdit_e_subject.text(), self.textEdit_e_body.toPlainText())
                if drop != 0:
                    self.smsg(drop + " messages failed to send.")
                else:
                    self.smsg("Message sent succesfully to all recepients")
        else:
            print('hi')
                

    #Logout
    
    def push_logout(self, form):
        form.close()


    #Clear
    def push_clear(self):
        PasswordDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Password()
        ui.setupUi(PasswordDialog)
        PasswordDialog.exec_()
        password = ui.lineEdit_password.text()
        if self.ses.login_admin(self.admin.adminid, password):
            self.admin.clear_database()
            self.smsg("Database cleared.")
        else:
            self.smsg("Error: Authentication failed")
            
    #############
    
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
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminPanel()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

