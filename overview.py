# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation

class Ui_txtRegisterScreen(object):
    tcNumber=''
    firstName=''
    lastName=''
    password=''
    birthday=''
    address=''

    def setupUi(self, txtRegisterScreen):
        txtRegisterScreen.setObjectName("txtRegisterScreen")
        txtRegisterScreen.setWindowModality(QtCore.Qt.WindowModal)
        txtRegisterScreen.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(txtRegisterScreen.sizePolicy().hasHeightForWidth())
        txtRegisterScreen.setSizePolicy(sizePolicy)
        txtRegisterScreen.setMinimumSize(QtCore.QSize(400, 500))
        txtRegisterScreen.setMaximumSize(QtCore.QSize(400, 500))
        txtRegisterScreen.setSizeIncrement(QtCore.QSize(400, 500))
        txtRegisterScreen.setBaseSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        txtRegisterScreen.setFont(font)
        txtRegisterScreen.setMouseTracking(True)
        txtRegisterScreen.setFocusPolicy(QtCore.Qt.ClickFocus)
        txtRegisterScreen.setStyleSheet("")
        txtRegisterScreen.setSizeGripEnabled(False)
        txtRegisterScreen.setModal(False)
        self.txtTcNumber_2 = QtWidgets.QLabel(txtRegisterScreen)
        self.txtTcNumber_2.setGeometry(QtCore.QRect(10, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtTcNumber_2.setFont(font)
        self.txtTcNumber_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtTcNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txtTcNumber_2.setObjectName("txtTcNumber_2")
        self.lnTcNumber = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnTcNumber.setGeometry(QtCore.QRect(130, 10, 201, 20))
        self.lnTcNumber.setMinimumSize(QtCore.QSize(0, 0))
        self.lnTcNumber.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.lnTcNumber.setText("")
        self.lnTcNumber.setMaxLength(11)
        self.lnTcNumber.setClearButtonEnabled(True)
        self.lnTcNumber.setProperty("numberOnly", "")
        self.lnTcNumber.setObjectName("lnTcNumber")
        self.groupBox = QtWidgets.QGroupBox(txtRegisterScreen)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 361, 361))
        self.groupBox.setObjectName("groupBox")
        self.lnPasswordNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lnPasswordNumber.setGeometry(QtCore.QRect(120, 150, 201, 20))
        self.lnPasswordNumber.setToolTipDuration(1)
        self.lnPasswordNumber.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lnPasswordNumber.setMaxLength(16)
        self.lnPasswordNumber.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lnPasswordNumber.setClearButtonEnabled(True)
        self.lnPasswordNumber.setObjectName("lnPasswordNumber")
        self.txtPasswordNumber = QtWidgets.QLabel(self.groupBox)
        self.txtPasswordNumber.setGeometry(QtCore.QRect(10, 150, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtPasswordNumber.setFont(font)
        self.txtPasswordNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtPasswordNumber.setObjectName("txtPasswordNumber")
        self.txtDateTime = QtWidgets.QLabel(self.groupBox)
        self.txtDateTime.setGeometry(QtCore.QRect(10, 200, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtDateTime.setFont(font)
        self.txtDateTime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtDateTime.setObjectName("txtDateTime")
        self.lnAddress = QtWidgets.QLineEdit(self.groupBox)
        self.lnAddress.setGeometry(QtCore.QRect(120, 270, 200, 80))
        self.lnAddress.setMinimumSize(QtCore.QSize(200, 80))
        self.lnAddress.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.lnAddress.setFont(font)
        self.lnAddress.setToolTip("")
        self.lnAddress.setToolTipDuration(0)
        self.lnAddress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lnAddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lnAddress.setInputMask("")
        self.lnAddress.setText("")
        self.lnAddress.setMaxLength(100)
        self.lnAddress.setCursorPosition(0)
        self.lnAddress.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lnAddress.setClearButtonEnabled(True)
        self.lnAddress.setObjectName("lnAddress")
        self.txtName = QtWidgets.QLabel(self.groupBox)
        self.txtName.setGeometry(QtCore.QRect(10, 30, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtName.setFont(font)
        self.txtName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtName.setObjectName("txtName")
        self.txtNameP = QtWidgets.QLabel(self.groupBox)
        self.txtNameP.setGeometry(QtCore.QRect(10, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtNameP.setFont(font)
        self.txtNameP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtNameP.setObjectName("txtNameP")
        self.lnName = QtWidgets.QLineEdit(self.groupBox)
        self.lnName.setGeometry(QtCore.QRect(120, 30, 201, 20))
        self.lnName.setMaxLength(20)
        self.lnName.setClearButtonEnabled(True)
        self.lnName.setObjectName("lnName")
        self.lnNameP = QtWidgets.QLineEdit(self.groupBox)
        self.lnNameP.setGeometry(QtCore.QRect(120, 90, 201, 20))
        self.lnNameP.setMaxLength(20)
        self.lnNameP.setClearButtonEnabled(True)
        self.lnNameP.setObjectName("lnNameP")
        self.txtAddress = QtWidgets.QLabel(self.groupBox)
        self.txtAddress.setGeometry(QtCore.QRect(10, 270, 51, 16))
        self.txtAddress.setMaximumSize(QtCore.QSize(1000, 1000))
        self.txtAddress.setSizeIncrement(QtCore.QSize(1000, 1000))
        self.txtAddress.setBaseSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtAddress.setFont(font)
        self.txtAddress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtAddress.setObjectName("txtAddress")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 200, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.btnSearch = QtWidgets.QPushButton(txtRegisterScreen)
        self.btnSearch.setGeometry(QtCore.QRect(150, 50, 180, 30))
        self.btnSearch.setObjectName("btnSearch")
        self.btnSearch.clicked.connect(self.getUser) #arama komutu
        self.btnUpdate = QtWidgets.QPushButton(txtRegisterScreen)
        self.btnUpdate.setGeometry(QtCore.QRect(10, 460, 180, 30))
        self.btnUpdate.clicked.connect(self.updateUser) #güncelleme komutu
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnClear = QtWidgets.QPushButton(txtRegisterScreen)
        self.btnClear.setGeometry(QtCore.QRect(210, 460, 180, 30))
        self.btnClear.clicked.connect(self.deleteUser) #silme komutu
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")

        self.retranslateUi(txtRegisterScreen)
        QtCore.QMetaObject.connectSlotsByName(txtRegisterScreen)

    def retranslateUi(self, txtRegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        txtRegisterScreen.setWindowTitle(_translate("txtRegisterScreen", "arama ekranı"))
        self.txtTcNumber_2.setText(_translate("txtRegisterScreen", "T.C. KİMLİK NO"))
        self.groupBox.setTitle(_translate("txtRegisterScreen", "BİLGİLER"))
        self.txtPasswordNumber.setText(_translate("txtRegisterScreen", "ŞİFRE"))
        self.txtDateTime.setText(_translate("txtRegisterScreen", "DOĞUM TARİHİ"))
        self.txtName.setText(_translate("txtRegisterScreen", "ADI"))
        self.txtNameP.setText(_translate("txtRegisterScreen", "SOYADI"))
        self.txtAddress.setText(_translate("txtRegisterScreen", "ADRES"))
        self.btnSearch.setText(_translate("txtRegisterScreen", "Ara"))
        self.btnUpdate.setText(_translate("txtRegisterScreen", "Güncelle"))
        self.btnClear.setText(_translate("txtRegisterScreen", "Sil"))

    def clearForm(self):
        self.lnName.setText('')
        self.lnNameP.setText('')
        self.lnPasswordNumber.setText('')
        self.lineEdit.setText('')
        self.lnAddress.setText('')

    def controlUser(self):

        for element in self.tcNumber:
            if(element not in ['1','2','3','4','5','6','7','8','9','0']):
                return False
        if(self.firstName=='' or self.lastName=='' or self.address=='' or self.birthday=='' or self.password==''):
            return False
        if(len(self.tcNumber)!=11):
            return False
        return True

    def getUser(self):
        self.clearForm()
        userOperation=databaseOperation.UserOperations('database.db')
        self.tcNumber=self.lnTcNumber.text()
        user=userOperation.getUser(self.tcNumber)

        if(len(user)!=0):
            self.lnTcNumber.setText(user[0][0])
            self.lnName.setText(user[0][1])
            self.lnNameP.setText(user[0][2])
            self.lnPasswordNumber.setText(user[0][3])
            self.lineEdit.setText(user[0][4])
            self.lnAddress.setText(user[0][5])

    def updateUser(self):
        self.clearForm()
        userOperation=databaseOperation.UserOperations('database.db')
        self.firstName=self.lnName.text()
        self.lastName=self.lnNameP.text()
        self.tcNumber=self.lnTcNumber.text()
        self.birthday=self.lineEdit.text()
        self.password=self.lnPasswordNumber.text()
        self.address=self.lnAddress.text()
        if(self.controlUser() and userOperation.updateUser(self.tcNumber,self.firstName,self.lastName,self.birthday,self.password,self.address)):
            print("Kullanıcı Güncellendi...")
        else:
            print("Hata Oluştu...!")

    def deleteUser(self):
        self.clearForm()
        userOperation=databaseOperation.UserOperations('database.db')
        self.tcNumber=self.lnTcNumber.text()
        if(userOperation.dropUser(self.tcNumber)):
            print("Kullanıcı Silindi...")
        else:
            print("Hata Oluştu...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    txtRegisterScreen = QtWidgets.QDialog()
    ui = Ui_txtRegisterScreen()
    ui.setupUi(txtRegisterScreen)
    txtRegisterScreen.show()
    sys.exit(app.exec_())
