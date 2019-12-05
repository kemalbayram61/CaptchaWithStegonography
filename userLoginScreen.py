# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation
from homeScreen import Ui_Form
from registerScreen import Ui_txtRegisterScreen
from userUpdate import UI_UserUpdate
import sys

class Ui_Dialog(object):
    tcNumber=''
    password=''
    Dialog=''

    def setupUi(self, Dialog):
        self.Dialog=Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 500)
        self.Dialog.setMinimumSize(QtCore.QSize(400, 500))
        self.Dialog.setMaximumSize(QtCore.QSize(400, 500))
        self.Dialog.setSizeIncrement(QtCore.QSize(400, 500))
        self.Dialog.setBaseSize(QtCore.QSize(400, 500))
        self.txtTcNumber = QtWidgets.QLineEdit(self.Dialog)
        self.txtTcNumber.setGeometry(QtCore.QRect(170, 120, 200, 20))
        self.txtTcNumber.setMaxLength(11)
        self.txtTcNumber.setClearButtonEnabled(True)
        self.txtTcNumber.setObjectName("txtTcNumber")
        self.txtPassword = QtWidgets.QLineEdit(self.Dialog)
        self.txtPassword.setGeometry(QtCore.QRect(170, 180, 200, 20))
        self.txtPassword.setText("")
        self.txtPassword.setMaxLength(20)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setClearButtonEnabled(True)
        self.txtPassword.setObjectName("txtPassword")
        self.lnTcNumber = QtWidgets.QLabel(self.Dialog)
        self.lnTcNumber.setGeometry(QtCore.QRect(20, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lnTcNumber.setFont(font)
        self.lnTcNumber.setObjectName("lnTcNumber")
        self.lnPassword = QtWidgets.QLabel(self.Dialog)
        self.lnPassword.setGeometry(QtCore.QRect(40, 180, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lnPassword.setFont(font)
        self.lnPassword.setObjectName("lnPassword")
        self.btnEnter = QtWidgets.QPushButton(self.Dialog)
        self.btnEnter.setGeometry(QtCore.QRect(90, 240, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEnter.setFont(font)
        self.btnEnter.setObjectName("btnEnter")
        self.btnRegister = QtWidgets.QPushButton(self.Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(90, 290, 180, 30))
        self.btnRegister.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.btnEnter.clicked.connect(self.userLogin) #silme komutu
        self.btnRegister.clicked.connect(self.userRegister) #kayıt komutu

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EnterLoginModule"))
        self.lnTcNumber.setText(_translate("Dialog", "T.C. Kimlik No"))
        self.lnPassword.setText(_translate("Dialog", "Şifre"))
        self.btnEnter.setText(_translate("Dialog", "Tamam"))
        self.btnRegister.setText(_translate("Dialog", "Kayıt ol"))


    def userLogin(self):
        userOperations=databaseOperation.UserOperations('database.db')
        self.tcNumber=self.txtTcNumber.text()
        user=userOperations.getUser(self.tcNumber)
        if(len(user)!=0):
            self.password=user[0][3]
            if(self.txtPassword.text()!=self.password):
                print("Hatalı Şifre!!!")
            else:
                print("Giriş Başarılı...")
                self.homeWindow=QtWidgets.QWidget()
                self.uiHome=Ui_Form(self.tcNumber)
                self.uiHome.setupUi(self.homeWindow)
                self.homeWindow.show()
                self.Dialog.close()
                
                
        else:
            print("Kullanıcı Kayıtlı Değil...")

    def userRegister(self):
        self.registerWindow=QtWidgets.QWidget()
        self.uiRegister=Ui_txtRegisterScreen()
        self.uiRegister.setupUi(self.registerWindow)
        self.registerWindow.show()
        self.Dialog.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
