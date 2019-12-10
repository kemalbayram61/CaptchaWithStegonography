# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptchaSelectionScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from questionAnswerScreen import UI_QA
import imageParser
import numpy as np
import cv2
import stepic
from PIL import Image

class Ui_CaptchaSelectionScreenModule(object):
    dialog=''
    tcNumber=''
    dstTc=''
    amount=0
    frames=''
    caseB1=False
    caseB2=False
    caseB3=False
    caseB4=False
    caseB5=False
    caseB6=False
    caseB7=False
    caseB8=False
    caseB9=False
    objectFrames=''

    def __init__(self,tcNumber,dstTc,amount):
        self.tcNumber=tcNumber
        self.dstTc=dstTc
        self.amount=amount

    def setupUi(self, CaptchaSelectionScreenModule):
        CaptchaSelectionScreenModule.setObjectName("CaptchaSelectionScreenModule")
        CaptchaSelectionScreenModule.setEnabled(True)
        CaptchaSelectionScreenModule.resize(400, 500)
        CaptchaSelectionScreenModule.setMinimumSize(QtCore.QSize(400, 500))
        CaptchaSelectionScreenModule.setMaximumSize(QtCore.QSize(400, 500))
        CaptchaSelectionScreenModule.setMouseTracking(True)
        self.lblCaptchaQ = QtWidgets.QLabel(CaptchaSelectionScreenModule)
        self.lblCaptchaQ.setGeometry(QtCore.QRect(10, 00, 141, 21))
        self.lblCaptchaQ.setObjectName("lbCaptchaQuestion")

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
        self.getImage()
        self.btnDone.clicked.connect(self.questionScreen)
        self.btnParseSelect1.clicked.connect(self.clickedBtn1)
        self.btnParseSelect2.clicked.connect(self.clickedBtn2)
        self.btnParseSelect3.clicked.connect(self.clickedBtn3)
        self.btnParseSelect4.clicked.connect(self.clickedBtn4)
        self.btnParseSelect5.clicked.connect(self.clickedBtn5)
        self.btnParseSelect6.clicked.connect(self.clickedBtn6)
        self.btnParseSelect7.clicked.connect(self.clickedBtn7)
        self.btnParseSelect8.clicked.connect(self.clickedBtn8)
        self.btnParseSelect9.clicked.connect(self.clickedBtn9)

        orgImage=Image.open("frames/f5.png") ############################Stegonography encode işlemi
        stgImage = stepic.encode(orgImage, b'kaobkaob')
        stgImage.save("frames/f5.png", 'PNG')

    def retranslateUi(self, CaptchaSelectionScreenModule):
        _translate = QtCore.QCoreApplication.translate
        CaptchaSelectionScreenModule.setWindowTitle(_translate("CaptchaSelectionScreenModule", "CaptchaSelectionScreenModule"))
        self.btnDone.setText(_translate("CaptchaSelectionScreenModule", "Onayla"))
        self.lblCaptchaQ.setText(_translate("CaptchaSelectionScreenModule", "Captcha Soru"))

    def questionScreen(self):
        if(self.controlClickedFrames()):
            self.questionWindow=QtWidgets.QWidget()
            self.uiquestion=UI_QA(self.tcNumber,self.dstTc,self.amount)
            self.uiquestion.setupUi(self.questionWindow)
            self.questionWindow.show()
            self.dialog.close()
        else:
            self.dialog.close()

    def getImage(self):
        imageProcessing=imageParser.ParseProcess()
        imagepars=imageProcessing.getFrames()
        self.frames=imagepars[0]
        self.objectFrames=imagepars[1]
        self.lblCaptchaQ.setText(imagepars[2]+" olan kareleri seçiniz...")
        if(len(self.frames)==9):
            imageProcessing.saveClickedFrames(self.frames)
            cv2.imwrite('frames/f1.png',self.frames[0])
            self.btnParseSelect1.setIcon(QtGui.QIcon('frames\\f1.png'))
            self.btnParseSelect1.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f2.png',self.frames[1])
            self.btnParseSelect2.setIcon(QtGui.QIcon('frames\\f2.png'))
            self.btnParseSelect2.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f3.png',self.frames[2])
            self.btnParseSelect3.setIcon(QtGui.QIcon('frames\\f3.png'))
            self.btnParseSelect3.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f4.png',self.frames[3])
            self.btnParseSelect4.setIcon(QtGui.QIcon('frames\\f4.png'))
            self.btnParseSelect4.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f5.png',self.frames[4])
            self.btnParseSelect5.setIcon(QtGui.QIcon('frames\\f5.png'))
            self.btnParseSelect5.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f6.png',self.frames[5])
            self.btnParseSelect6.setIcon(QtGui.QIcon('frames\\f6.png'))
            self.btnParseSelect6.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f7.png',self.frames[6])
            self.btnParseSelect7.setIcon(QtGui.QIcon('frames\\f7.png'))
            self.btnParseSelect7.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f8.png',self.frames[7])
            self.btnParseSelect8.setIcon(QtGui.QIcon('frames\\f8.png'))
            self.btnParseSelect8.setIconSize(QtCore.QSize(61,61))

            cv2.imwrite('frames/f9.png',self.frames[8])
            self.btnParseSelect9.setIcon(QtGui.QIcon('frames\\f9.png'))
            self.btnParseSelect9.setIconSize(QtCore.QSize(61,61))



    def clickedBtn1(self):
        if(self.caseB1==False):
            self.caseB1=True
            self.btnParseSelect1.setIcon(QtGui.QIcon('frames\\bf1.png'))
            self.btnParseSelect1.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB1=False
            self.btnParseSelect1.setIcon(QtGui.QIcon('frames\\f1.png'))
            self.btnParseSelect1.setIconSize(QtCore.QSize(61,61))

    def clickedBtn2(self):
        if(self.caseB2==False):
            self.caseB2=True
            self.btnParseSelect2.setIcon(QtGui.QIcon('frames\\bf2.png'))
            self.btnParseSelect2.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB2=False
            self.btnParseSelect2.setIcon(QtGui.QIcon('frames\\f2.png'))
            self.btnParseSelect2.setIconSize(QtCore.QSize(61,61))
    def clickedBtn3(self):
        if(self.caseB3==False):
            self.caseB3=True
            self.btnParseSelect3.setIcon(QtGui.QIcon('frames\\bf3.png'))
            self.btnParseSelect3.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB3=False
            self.btnParseSelect3.setIcon(QtGui.QIcon('frames\\f3.png'))
            self.btnParseSelect3.setIconSize(QtCore.QSize(61,61))
    def clickedBtn4(self):
        if(self.caseB4==False):
            self.caseB4=True
            self.btnParseSelect4.setIcon(QtGui.QIcon('frames\\bf4.png'))
            self.btnParseSelect4.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB4=False
            self.btnParseSelect4.setIcon(QtGui.QIcon('frames\\f4.png'))
            self.btnParseSelect4.setIconSize(QtCore.QSize(61,61))
    def clickedBtn5(self):
        if(self.caseB5==False):
            self.caseB5=True
            self.btnParseSelect5.setIcon(QtGui.QIcon('frames\\bf5.png'))
            self.btnParseSelect5.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB5=False
            self.btnParseSelect5.setIcon(QtGui.QIcon('frames\\f5.png'))
            self.btnParseSelect5.setIconSize(QtCore.QSize(61,61))
    def clickedBtn6(self):
        if(self.caseB6==False):
            self.caseB6=True
            self.btnParseSelect6.setIcon(QtGui.QIcon('frames\\bf6.png'))
            self.btnParseSelect6.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB6=False
            self.btnParseSelect6.setIcon(QtGui.QIcon('frames\\f6.png'))
            self.btnParseSelect6.setIconSize(QtCore.QSize(61,61))
    def clickedBtn7(self):
        if(self.caseB7==False):
            self.caseB7=True
            self.btnParseSelect7.setIcon(QtGui.QIcon('frames\\bf7.png'))
            self.btnParseSelect7.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB7=False
            self.btnParseSelect7.setIcon(QtGui.QIcon('frames\\f7.png'))
            self.btnParseSelect7.setIconSize(QtCore.QSize(61,61))
    def clickedBtn8(self):
        if(self.caseB8==False):
            self.caseB8=True
            self.btnParseSelect8.setIcon(QtGui.QIcon('frames\\bf8.png'))
            self.btnParseSelect8.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB8=False
            self.btnParseSelect8.setIcon(QtGui.QIcon('frames\\f8.png'))
            self.btnParseSelect8.setIconSize(QtCore.QSize(61,61))
    def clickedBtn9(self):
        if(self.caseB9==False):
            self.caseB9=True
            self.btnParseSelect9.setIcon(QtGui.QIcon('frames\\bf9.png'))
            self.btnParseSelect9.setIconSize(QtCore.QSize(61,61))
        else:
            self.caseB9=False
            self.btnParseSelect9.setIcon(QtGui.QIcon('frames\\f9.png'))
            self.btnParseSelect9.setIconSize(QtCore.QSize(61,61))

    def getClickedFrames(self):
        clicked=''
        if(self.caseB1):
            clicked+='1,'
        if(self.caseB2):
            clicked+='2,'
        if(self.caseB3):
            clicked+='3,'
        if(self.caseB4):
            clicked+='4,'
        if(self.caseB5):
            clicked+='5,'
        if(self.caseB6):
            clicked+='6,'
        if(self.caseB7):
            clicked+='7,'
        if(self.caseB8):
            clicked+='8,'
        if(self.caseB9):
            clicked+='9'
        return clicked

    def controlClickedFrames(self):
        print(self.objectFrames)
        print(self.getClickedFrames())
        if(self.objectFrames==self.getClickedFrames()):
            return True
        else:
            return False