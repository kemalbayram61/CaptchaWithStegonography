# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from userUpdate import UI_UserUpdate
from profileInformation import UI_ProfileInformation

class Ui_Form(object):
    tcNumber=''
    def __init__(self,tcNumber):
        self.tcNumber=tcNumber

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        self.btnAccountAction = QtWidgets.QPushButton(Form)
        self.btnAccountAction.setGeometry(QtCore.QRect(100, 170, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAction.setFont(font)
        self.btnAccountAction.setObjectName("btnAccountAction")
        self.btnAccountAbstract = QtWidgets.QPushButton(Form)
        self.btnAccountAbstract.setGeometry(QtCore.QRect(100, 120, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAbstract.setFont(font)
        self.btnAccountAbstract.setObjectName("btnAccountAbstract")
        self.btnProfileSetting = QtWidgets.QPushButton(Form)
        self.btnProfileSetting.setGeometry(QtCore.QRect(100, 360, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileSetting.setFont(font)
        self.btnProfileSetting.setObjectName("btnProfileSetting")
        self.btnSendMoney = QtWidgets.QPushButton(Form)
        self.btnSendMoney.setGeometry(QtCore.QRect(100, 70, 180, 30))

        self.btnProfileSetting.clicked.connect(self.userUpdateScreen)

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSendMoney.setFont(font)
        self.btnSendMoney.setObjectName("btnSendMoney")
        self.btnProfileView = QtWidgets.QPushButton(Form)
        self.btnProfileView.setGeometry(QtCore.QRect(100, 300, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileView.setFont(font)
        self.btnProfileView.setObjectName("btnProfileView")
        self.lbAccount = QtWidgets.QLabel(Form)
        self.lbAccount.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.btnProfileView.clicked.connect(self.userOverviewProfile)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbAccount.setFont(font)
        self.lbAccount.setObjectName("lbAccount")
        self.lbProfileProcess = QtWidgets.QLabel(Form)
        self.lbProfileProcess.setGeometry(QtCore.QRect(20, 270, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbProfileProcess.setFont(font)
        self.lbProfileProcess.setObjectName("lbProfileProcess")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ana Sayfa"))
        self.btnAccountAction.setText(_translate("Form", "Hesap Hareketleri"))
        self.btnAccountAbstract.setText(_translate("Form", "Hesap Özeti"))
        self.btnProfileSetting.setText(_translate("Form", "Profili Düzenle"))
        self.btnSendMoney.setText(_translate("Form", "Para Gönder"))
        self.btnProfileView.setText(_translate("Form", "Profili Görüntüle"))
        self.lbAccount.setText(_translate("Form", "Hesap İşlemleri"))
        self.lbProfileProcess.setText(_translate("Form", "Profil İşlemleri"))

    def userUpdateScreen(self):
        self.updateWindow=QtWidgets.QWidget()
        self.uiUpdateScreen=UI_UserUpdate(self.tcNumber)
        self.uiUpdateScreen.setupUi(self.updateWindow)
        self.updateWindow.show()

    def userOverviewProfile(self):
        self.uoverviewWindow=QtWidgets.QWidget()
        self.uiOverviewScreen=UI_ProfileInformation(self.tcNumber)
        self.uiOverviewScreen.setupUi(self.uoverviewWindow)
        self.uoverviewWindow.show()