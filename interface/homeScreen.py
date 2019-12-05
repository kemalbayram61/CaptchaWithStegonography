# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 400, 250))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnSendMoney = QtWidgets.QPushButton(self.groupBox)
        self.btnSendMoney.setGeometry(QtCore.QRect(110, 60, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSendMoney.setFont(font)
        self.btnSendMoney.setObjectName("btnSendMoney")
        self.btnAccountAbstract = QtWidgets.QPushButton(self.groupBox)
        self.btnAccountAbstract.setGeometry(QtCore.QRect(110, 120, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAbstract.setFont(font)
        self.btnAccountAbstract.setObjectName("btnAccountAbstract")
        self.btnAccountAction = QtWidgets.QPushButton(self.groupBox)
        self.btnAccountAction.setGeometry(QtCore.QRect(110, 180, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAccountAction.setFont(font)
        self.btnAccountAction.setObjectName("btnAccountAction")
        self.lbNameView = QtWidgets.QLabel(self.groupBox)
        self.lbNameView.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.lbNameView.setObjectName("lbNameView")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 250, 400, 250))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnProfileView = QtWidgets.QPushButton(self.groupBox_2)
        self.btnProfileView.setGeometry(QtCore.QRect(110, 60, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileView.setFont(font)
        self.btnProfileView.setObjectName("btnProfileView")
        self.btnProfileSetting = QtWidgets.QPushButton(self.groupBox_2)
        self.btnProfileSetting.setGeometry(QtCore.QRect(110, 120, 180, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnProfileSetting.setFont(font)
        self.btnProfileSetting.setObjectName("btnProfileSetting")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ana Sayfa"))
        self.groupBox.setTitle(_translate("Form", "Hesap işlemleri"))
        self.btnSendMoney.setText(_translate("Form", "Para Gönder"))
        self.btnAccountAbstract.setText(_translate("Form", "Hesap Özeti"))
        self.btnAccountAction.setText(_translate("Form", "Hesap Hareketleri"))
        self.lbNameView.setText(_translate("Form", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Form", "Profil İşlemleri"))
        self.btnProfileView.setText(_translate("Form", "Profili Görüntüle"))
        self.btnProfileSetting.setText(_translate("Form", "Profili Düzenle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
