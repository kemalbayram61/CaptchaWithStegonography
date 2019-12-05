# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self,parent=None):
        object.__init__(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Para = QtWidgets.QWidget()
        self.Para.setObjectName("Para")
        self.btnMoneySend = QtWidgets.QPushButton(self.Para)
        self.btnMoneySend.setGeometry(QtCore.QRect(110, 170, 180, 30))
        self.btnMoneySend.setObjectName("btnMoneySend")
        self.btnMoneyStatement = QtWidgets.QPushButton(self.Para)
        self.btnMoneyStatement.setGeometry(QtCore.QRect(110, 230, 180, 30))
        self.btnMoneyStatement.setObjectName("btnMoneyStatement")
        self.lbNameView = QtWidgets.QLabel(self.Para)
        self.lbNameView.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.lbNameView.setObjectName("lbNameView")
        self.tabWidget.addTab(self.Para, "")
        self.Profil = QtWidgets.QWidget()
        self.Profil.setObjectName("Profil")
        self.btnProfile = QtWidgets.QPushButton(self.Profil)
        self.btnProfile.setGeometry(QtCore.QRect(110, 170, 180, 30))
        self.btnProfile.setObjectName("btnProfile")
        self.lbNameView_2 = QtWidgets.QLabel(self.Profil)
        self.lbNameView_2.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.lbNameView_2.setObjectName("lbNameView_2")
        self.btnProfileSetting = QtWidgets.QPushButton(self.Profil)
        self.btnProfileSetting.setGeometry(QtCore.QRect(110, 230, 180, 30))
        self.btnProfileSetting.setObjectName("btnProfileSetting")
        self.tabWidget.addTab(self.Profil, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HomeScreen"))
        self.btnMoneySend.setText(_translate("Form", "Para Gönder"))
        self.btnMoneyStatement.setText(_translate("Form", "Hesap Özeti"))
        self.lbNameView.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Para), _translate("Form", "Hesap İşlemleri"))
        self.btnProfile.setText(_translate("Form", "Profilim"))
        self.lbNameView_2.setText(_translate("Form", "TextLabel"))
        self.btnProfileSetting.setText(_translate("Form", "Profili Düzenle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Profil), _translate("Form", "Profil İşlemleri"))


def main():
    import sys
    appHome = QtWidgets.QApplication(sys.argv)
    FormHome = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(FormHome)
    FormHome.show()
    sys.exit(appHome.exec_())

if __name__ == "__main__":
    main()