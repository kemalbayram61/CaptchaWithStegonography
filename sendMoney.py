# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMoneyModule.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.txtDestinationTcNumber.setObjectName("txtDestinationTcNumber")
        self.txtDestinationTcNumber_2 = QtWidgets.QLineEdit(Dialog)
        self.txtDestinationTcNumber_2.setGeometry(QtCore.QRect(160, 160, 200, 20))
        self.txtDestinationTcNumber_2.setObjectName("txtDestinationTcNumber_2")
        self.txtBalance = QtWidgets.QLineEdit(Dialog)
        self.txtBalance.setGeometry(QtCore.QRect(160, 210, 200, 20))
        self.txtBalance.setObjectName("txtBalance")
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
        self.txtSendAmount.setObjectName("txtSendAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SendMoneyModule"))
        self.lbSendAmount.setText(_translate("Dialog", "Gönderilecek Tutar"))
        self.lbSourceTcNumber.setText(_translate("Dialog", "T.C.  Kimlik No"))
        self.lbDestinationTcNumber.setText(_translate("Dialog", " Alıcı Kimlik No"))
        self.btnSendMoney.setText(_translate("Dialog", "Gönder"))
        self.lbBalance.setText(_translate("Dialog", "Mevcut Bakiye"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
