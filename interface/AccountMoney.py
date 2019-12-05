# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountMoney.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hesapozeti(object):
    def setupUi(self, Hesapozeti):
        Hesapozeti.setObjectName("Hesapozeti")
        Hesapozeti.resize(400, 500)
        Hesapozeti.setMinimumSize(QtCore.QSize(400, 500))
        Hesapozeti.setMaximumSize(QtCore.QSize(400, 500))
        Hesapozeti.setSizeIncrement(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Hesapozeti.setFont(font)
        self.lbAccounMoneyNoFunction = QtWidgets.QLabel(Hesapozeti)
        self.lbAccounMoneyNoFunction.setGeometry(QtCore.QRect(40, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lbAccounMoneyNoFunction.setFont(font)
        self.lbAccounMoneyNoFunction.setObjectName("lbAccounMoneyNoFunction")
        self.lbAccountMoneyView = QtWidgets.QLabel(Hesapozeti)
        self.lbAccountMoneyView.setGeometry(QtCore.QRect(110, 120, 221, 21))
        self.lbAccountMoneyView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbAccountMoneyView.setObjectName("lbAccountMoneyView")
        self.lbUserName = QtWidgets.QLabel(Hesapozeti)
        self.lbUserName.setGeometry(QtCore.QRect(40, 45, 231, 21))
        self.lbUserName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbUserName.setText("")
        self.lbUserName.setObjectName("lbUserName")
        self.btnDone = QtWidgets.QPushButton(Hesapozeti)
        self.btnDone.setGeometry(QtCore.QRect(130, 200, 180, 30))
        self.btnDone.setObjectName("btnDone")

        self.retranslateUi(Hesapozeti)
        QtCore.QMetaObject.connectSlotsByName(Hesapozeti)

    def retranslateUi(self, Hesapozeti):
        _translate = QtCore.QCoreApplication.translate
        Hesapozeti.setWindowTitle(_translate("Hesapozeti", "Hesap Özeti"))
        self.lbAccounMoneyNoFunction.setText(_translate("Hesapozeti", "Miktar"))
        self.lbAccountMoneyView.setText(_translate("Hesapozeti", "TextLabel"))
        self.btnDone.setText(_translate("Hesapozeti", "Tamam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hesapozeti = QtWidgets.QWidget()
    ui = Ui_Hesapozeti()
    ui.setupUi(Hesapozeti)
    Hesapozeti.show()
    sys.exit(app.exec_())
