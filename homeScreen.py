# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation
import userUpdate

class Ui_Form(object):
    tcNumber=''

    def __init__(self,tcNumber):
        self.tcNumber=tcNumber

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSendMoney = QtWidgets.QPushButton(Form)
        self.btnSendMoney.setGeometry(QtCore.QRect(110, 60, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSendMoney.setFont(font)
        self.btnSendMoney.setObjectName("btnSendMoney")
        self.btnAccountAbstract = QtWidgets.QPushButton(Form)
        self.btnAccountAbstract.setGeometry(QtCore.QRect(110, 120, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAbstract.setFont(font)
        self.btnAccountAbstract.setObjectName("btnAccountAbstract")
        self.btnAccountAction = QtWidgets.QPushButton(Form)
        self.btnAccountAction.setGeometry(QtCore.QRect(110, 180, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAction.setFont(font)
        self.btnAccountAction.setObjectName("btnAccountAction")
        self.lbNameView = QtWidgets.QLabel(Form)
        self.lbNameView.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.lbNameView.setObjectName("lbNameView")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.btnProfileView = QtWidgets.QPushButton(Form)
        self.btnProfileView.setGeometry(QtCore.QRect(110, 60, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileView.setFont(font)
        self.btnProfileView.setObjectName("btnProfileView")
        self.btnProfileSetting = QtWidgets.QPushButton(Form)
        self.btnProfileSetting.setGeometry(QtCore.QRect(110, 120, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileSetting.setFont(font)
        self.btnProfileSetting.setObjectName("btnProfileSetting")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnProfileSetting.clicked.connect(self.userUpdateScreen)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ana Sayfa"))

        self.btnSendMoney.setText(_translate("Form", "Para Gönder"))
        self.btnAccountAbstract.setText(_translate("Form", "Hesap Özeti"))
        self.btnAccountAction.setText(_translate("Form", "Hesap Hareketleri"))
        self.lbNameView.setText(_translate("Form", "TextLabel"))

        self.btnProfileView.setText(_translate("Form", "Profili Görüntüle"))
        self.btnProfileSetting.setText(_translate("Form", "Profili Düzenle"))

    def userUpdateScreen(self):
        print("acılıyor")
        dialog=QtWidgets.QDialog()
        ui=userUpdate.UI_UserUpdate(self.tcNumber)
        ui.setupUi(dialog)
        dialog.show()
