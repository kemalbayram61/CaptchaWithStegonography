# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMoneyModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from captchaScreen import Ui_CaptchaSelectionScreenModule

class UI_SendMoney(object):
    tcNumber=''
    dialog=''
    def __init__(self,tcNumber):
        self.tcNumber=tcNumber

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 500)
        Dialog.setMinimumSize(QtCore.QSize(400, 500))
        Dialog.setMaximumSize(QtCore.QSize(400, 500))
        Dialog.setSizeIncrement(QtCore.QSize(400, 500))
        self.lbSendAmount = QtWidgets.QLabel(Dialog)
        self.lbSendAmount.setGeometry(QtCore.QRect(10, 260, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSendAmount.setFont(font)
        self.lbSendAmount.setObjectName("lbSendAmount")
        self.lbSourceTcNumber = QtWidgets.QLabel(Dialog)
        self.lbSourceTcNumber.setGeometry(QtCore.QRect(10, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSourceTcNumber.setFont(font)
        self.lbSourceTcNumber.setObjectName("lbSourceTcNumber")
        self.lbDestinationTcNumber = QtWidgets.QLabel(Dialog)
        self.lbDestinationTcNumber.setGeometry(QtCore.QRect(10, 160, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbDestinationTcNumber.setFont(font)
        self.lbDestinationTcNumber.setObjectName("lbDestinationTcNumber")
        self.btnSendMoney = QtWidgets.QPushButton(Dialog)
        self.btnSendMoney.setGeometry(QtCore.QRect(180, 320, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSendMoney.setFont(font)
        self.btnSendMoney.setObjectName("btnSendMoney")
        self.txtDestinationTcNumber = QtWidgets.QLineEdit(Dialog)
        self.txtDestinationTcNumber.setGeometry(QtCore.QRect(160, 120, 200, 20))
        self.txtDestinationTcNumber.setMaxLength(11)
        self.txtDestinationTcNumber.setClearButtonEnabled(True)
        self.txtDestinationTcNumber.setObjectName("txtDestinationTcNumber")
        self.txtDestinationTcNumber_2 = QtWidgets.QLineEdit(Dialog)
        self.txtDestinationTcNumber_2.setGeometry(QtCore.QRect(160, 160, 200, 20))
        self.txtDestinationTcNumber_2.setMaxLength(11)
        self.txtDestinationTcNumber_2.setClearButtonEnabled(True)
        self.txtDestinationTcNumber_2.setObjectName("txtDestinationTcNumber_2")
        self.lbBalance = QtWidgets.QLabel(Dialog)
        self.lbBalance.setGeometry(QtCore.QRect(10, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbBalance.setFont(font)
        self.lbBalance.setObjectName("lbBalance")
        self.txtSendAmount = QtWidgets.QLineEdit(Dialog)
        self.txtSendAmount.setGeometry(QtCore.QRect(160, 260, 200, 20))
        self.txtSendAmount.setMaxLength(500000)
        self.txtSendAmount.setClearButtonEnabled(True)
        self.txtSendAmount.setObjectName("txtSendAmount")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 210, 201, 21))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnSendMoney.clicked.connect(self.captchaScreen)
        self.dialog=Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SendMoneyModule"))
        self.lbSendAmount.setText(_translate("Dialog", "Gönderilecek Tutar"))
        self.lbSourceTcNumber.setText(_translate("Dialog", "T.C.  Kimlik No"))
        self.lbDestinationTcNumber.setText(_translate("Dialog", " Alıcı Kimlik No"))
        self.btnSendMoney.setText(_translate("Dialog", "Gönder"))
        self.lbBalance.setText(_translate("Dialog", "Mevcut Bakiye"))

    def captchaScreen(self):
        self.captchaWindow=QtWidgets.QWidget()
        self.uiCaptcha=Ui_CaptchaSelectionScreenModule(self.tcNumber)
        self.uiCaptcha.setupUi(self.captchaWindow)
        self.captchaWindow.show()
        self.dialog.close()
