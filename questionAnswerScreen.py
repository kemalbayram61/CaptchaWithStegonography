# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionAuthenticationScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation
import stepic
from PIL import Image

class UI_QA(object):
    dialog=''
    tcNumber=''
    dstTc=''
    questionId=0
    amount=0
    answerCount=0

    def __init__(self,tcNumber,dstTc,amount):
        self.tcNumber=tcNumber
        self.dstTc=dstTc
        self.amount=amount

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        self.lbQuestionView = QtWidgets.QLabel(Form)
        self.lbQuestionView.setGeometry(QtCore.QRect(50, 180, 291, 20))
        self.lbQuestionView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbQuestionView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbQuestionView.setFrameShape(QtWidgets.QFrame.Box)
        self.lbQuestionView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbQuestionView.setText("")
        self.lbQuestionView.setObjectName("lbQuestionView")
        self.txtAnswerEnter = QtWidgets.QLineEdit(Form)
        self.txtAnswerEnter.setGeometry(QtCore.QRect(50, 220, 291, 20))
        self.txtAnswerEnter.setObjectName("txtAnswerEnter")
        self.btnDone = QtWidgets.QPushButton(Form)
        self.btnDone.setGeometry(QtCore.QRect(110, 270, 180, 30))
        self.btnDone.setObjectName("btnDone")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.dialog=Form
        self.btnDone.clicked.connect(self.complate)
        self.getQuestions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QuestionAuthenticationScreenModule"))
        self.btnDone.setText(_translate("Form", "Onayla"))

    def complate(self):
        accountOpr=databaseOperation.accountOperations('database.db')
        if(self.controlAnswer()):
            if(self.controlStegoImage()):
                if(accountOpr.transferMoney(self.tcNumber,self.dstTc,self.amount)):
                        print("Para Transferi Basarılı...")
                        self.dialog.close()
                else:
                    print("Veri Tabanına ekleme Hatası Oluştu...")
            else:
                print("Resime Gizlenen Bilgi Değiştirilmiş İşlem İptal Edildi...")
                self.dialog.close()
        elif(self.answerCount<3):
            print("Son "+(str)(3-self.answerCount)+" Hakkınız Kaldı...")
        else:
            print("Transfer Yapılamadı...")
            self.dialog.close()
    
    def getQuestions(self):
        import random
        questionOpr=databaseOperation.QuestionOperations('database.db')
        questions=questionOpr.getQuestions()
        if(len(questions)>0):
            qindex=random.randint(0,len(questions)-1)
            self.questionId=questions[qindex][0]
            self.lbQuestionView.setText(questions[qindex][1])

    def controlAnswer(self):
        answerOpr=databaseOperation.AnswerOperations('database.db')
        answer=answerOpr.getAnswer(self.tcNumber,self.questionId)
        if(self.txtAnswerEnter.text()==answer[0][2]):
            return True
        else:
            self.answerCount+=1
            return False

    def controlStegoImage(self):
        self.key="kaobkaob"
        im=Image.open("frames/f5.png")
        message=stepic.decode(im)
        ###########################################¶tcnumbe decode
        im=Image.open("frames/f6.png")
        tcNumStego=stepic.decode(im)

        if(message==self.key and self.tcNumber==tcNumStego):
            print("Gizlenen:"+message+" Key:"+self.key)
            print("Gizlenen Tc:"+tcNumStego+" Sonuc Tc:"+self.tcNumber)
            return True
        else:
            print("Gizlenen:"+message+" Key:"+self.key)
            print("Gizlenen Tc:"+tcNumStego+" Sonuc Tc:"+self.tcNumber)
            return False
