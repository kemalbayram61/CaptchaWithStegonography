# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation
import homeScreen
import registerScreen
import userUpdate

class Ui_Dialog(object):
    tcNumber=''
    password=''

    def __init__(self,HomeScreen,RegisterScreen,UserUpdate):
        self.home=HomeScreen
        self.register=RegisterScreen
        self.uupdate=UserUpdate

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 500)
        Dialog.setMinimumSize(QtCore.QSize(400, 500))
        Dialog.setMaximumSize(QtCore.QSize(400, 500))
        Dialog.setSizeIncrement(QtCore.QSize(400, 500))
        Dialog.setBaseSize(QtCore.QSize(400, 500))
        self.txtTcNumber = QtWidgets.QLineEdit(Dialog)
        self.txtTcNumber.setGeometry(QtCore.QRect(170, 120, 200, 20))
        self.txtTcNumber.setMaxLength(11)
        self.txtTcNumber.setClearButtonEnabled(True)
        self.txtTcNumber.setObjectName("txtTcNumber")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        self.txtPassword.setGeometry(QtCore.QRect(170, 180, 200, 20))
        self.txtPassword.setText("")
        self.txtPassword.setMaxLength(20)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setClearButtonEnabled(True)
        self.txtPassword.setObjectName("txtPassword")
        self.lnTcNumber = QtWidgets.QLabel(Dialog)
        self.lnTcNumber.setGeometry(QtCore.QRect(20, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lnTcNumber.setFont(font)
        self.lnTcNumber.setObjectName("lnTcNumber")
        self.lnPassword = QtWidgets.QLabel(Dialog)
        self.lnPassword.setGeometry(QtCore.QRect(40, 180, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lnPassword.setFont(font)
        self.lnPassword.setObjectName("lnPassword")
        self.btnEnter = QtWidgets.QPushButton(Dialog)
        self.btnEnter.setGeometry(QtCore.QRect(90, 240, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEnter.setFont(font)
        self.btnEnter.setObjectName("btnEnter")
        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(90, 290, 180, 30))
        self.btnRegister.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
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
                uiHome=homeScreen.Ui_Form(self.tcNumber)
                uiHome.setupUi(self.home)
                self.home.show()
                
        else:
            print("Kullanıcı Kayıtlı Değil...")

    def userRegister(self):
        uiRegister=registerScreen.Ui_txtRegisterScreen()
        uiRegister.setupUi(self.register)
        self.register.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    DialogHome=QtWidgets.QDialog()

    DialogRegister=QtWidgets.QDialog()

    DialogUserUpdate=QtWidgets.QDialog()
    
    ui = Ui_Dialog(DialogHome,DialogRegister,DialogUserUpdate)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
