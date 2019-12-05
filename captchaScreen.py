# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptchaSelectionScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from questionAnswerScreen import UI_QA

class Ui_CaptchaSelectionScreenModule(object):
    dialog=''
    tcNumber=''
    def __init__(self,tcNumber):
        self.tcNumber=tcNumber

    def setupUi(self, CaptchaSelectionScreenModule):
        CaptchaSelectionScreenModule.setObjectName("CaptchaSelectionScreenModule")
        CaptchaSelectionScreenModule.setEnabled(True)
        CaptchaSelectionScreenModule.resize(400, 500)
        CaptchaSelectionScreenModule.setMinimumSize(QtCore.QSize(400, 500))
        CaptchaSelectionScreenModule.setMaximumSize(QtCore.QSize(400, 500))
        CaptchaSelectionScreenModule.setMouseTracking(True)
        self.btnParseSelect1 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect1.setGeometry(QtCore.QRect(70, 90, 61, 61))
        self.btnParseSelect1.setText("")
        self.btnParseSelect1.setCheckable(True)
        self.btnParseSelect1.setChecked(False)
        self.btnParseSelect1.setObjectName("btnParseSelect1")
        self.btnParseSelect2 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect2.setGeometry(QtCore.QRect(160, 90, 61, 61))
        self.btnParseSelect2.setText("")
        self.btnParseSelect2.setCheckable(True)
        self.btnParseSelect2.setChecked(False)
        self.btnParseSelect2.setObjectName("btnParseSelect2")
        self.btnParseSelect3 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect3.setEnabled(True)
        self.btnParseSelect3.setGeometry(QtCore.QRect(250, 90, 61, 61))
        self.btnParseSelect3.setText("")
        self.btnParseSelect3.setCheckable(True)
        self.btnParseSelect3.setChecked(False)
        self.btnParseSelect3.setFlat(False)
        self.btnParseSelect3.setObjectName("btnParseSelect3")
        self.btnParseSelect4 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect4.setGeometry(QtCore.QRect(70, 180, 61, 61))
        self.btnParseSelect4.setText("")
        self.btnParseSelect4.setCheckable(True)
        self.btnParseSelect4.setChecked(False)
        self.btnParseSelect4.setObjectName("btnParseSelect4")
        self.btnParseSelect5 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect5.setGeometry(QtCore.QRect(160, 180, 61, 61))
        self.btnParseSelect5.setText("")
        self.btnParseSelect5.setCheckable(True)
        self.btnParseSelect5.setChecked(False)
        self.btnParseSelect5.setObjectName("btnParseSelect5")
        self.btnParseSelect6 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect6.setGeometry(QtCore.QRect(250, 180, 61, 61))
        self.btnParseSelect6.setText("")
        self.btnParseSelect6.setCheckable(True)
        self.btnParseSelect6.setChecked(False)
        self.btnParseSelect6.setObjectName("btnParseSelect6")
        self.btnParseSelect7 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect7.setGeometry(QtCore.QRect(70, 270, 61, 61))
        self.btnParseSelect7.setText("")
        self.btnParseSelect7.setCheckable(True)
        self.btnParseSelect7.setChecked(False)
        self.btnParseSelect7.setObjectName("btnParseSelect7")
        self.btnParseSelect8 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect8.setGeometry(QtCore.QRect(160, 270, 61, 61))
        self.btnParseSelect8.setText("")
        self.btnParseSelect8.setCheckable(True)
        self.btnParseSelect8.setChecked(False)
        self.btnParseSelect8.setObjectName("btnParseSelect8")
        self.btnParseSelect9 = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnParseSelect9.setGeometry(QtCore.QRect(250, 270, 61, 61))
        self.btnParseSelect9.setText("")
        self.btnParseSelect9.setCheckable(True)
        self.btnParseSelect9.setChecked(False)
        self.btnParseSelect9.setObjectName("btnParseSelect9")
        self.btnDone = QtWidgets.QPushButton(CaptchaSelectionScreenModule)
        self.btnDone.setGeometry(QtCore.QRect(100, 380, 180, 30))
        self.btnDone.setMouseTracking(False)
        self.btnDone.setObjectName("btnDone")

        self.retranslateUi(CaptchaSelectionScreenModule)
        QtCore.QMetaObject.connectSlotsByName(CaptchaSelectionScreenModule)
        self.dialog=CaptchaSelectionScreenModule
        self.btnDone.clicked.connect(self.questionScreen)

    def retranslateUi(self, CaptchaSelectionScreenModule):
        _translate = QtCore.QCoreApplication.translate
        CaptchaSelectionScreenModule.setWindowTitle(_translate("CaptchaSelectionScreenModule", "CaptchaSelectionScreenModule"))
        self.btnDone.setText(_translate("CaptchaSelectionScreenModule", "Onayla"))

    def questionScreen(self):
        self.questionWindow=QtWidgets.QWidget()
        self.uiquestion=UI_QA(self.tcNumber)
        self.uiquestion.setupUi(self.questionWindow)
        self.questionWindow.show()
        self.dialog.close()
