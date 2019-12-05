# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionAnswerScreenModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import databaseOperation
from homeScreen import Ui_Form

class Ui_FormQuestion(object):
    tcNumber=''
    dialog=''

    def __init__(self,tcNumber):
        self.tcNumber=tcNumber

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        self.txtAnswer1 = QtWidgets.QLineEdit(Form)
        self.txtAnswer1.setGeometry(QtCore.QRect(100, 120, 201, 20))
        self.txtAnswer1.setObjectName("txtAnswer1")
        self.txtAnswer2 = QtWidgets.QLineEdit(Form)
        self.txtAnswer2.setGeometry(QtCore.QRect(100, 200, 201, 20))
        self.txtAnswer2.setObjectName("txtAnswer2")
        self.txtAnswer3 = QtWidgets.QLineEdit(Form)
        self.txtAnswer3.setGeometry(QtCore.QRect(100, 280, 201, 20))
        self.txtAnswer3.setObjectName("txtAnswer3")
        self.cmbQuestion1 = QtWidgets.QComboBox(Form)
        self.cmbQuestion1.setGeometry(QtCore.QRect(100, 90, 200, 20))
        self.cmbQuestion1.setObjectName("cmbQuestion1")
        self.cmbQuestion3 = QtWidgets.QComboBox(Form)
        self.cmbQuestion3.setGeometry(QtCore.QRect(100, 240, 200, 20))
        self.cmbQuestion3.setObjectName("cmbQuestion3")
        self.cmbQuestion2 = QtWidgets.QComboBox(Form)
        self.cmbQuestion2.setGeometry(QtCore.QRect(100, 160, 200, 20))
        self.cmbQuestion2.setObjectName("cmbQuestion2")
        self.lbQuestion1 = QtWidgets.QLabel(Form)
        self.lbQuestion1.setGeometry(QtCore.QRect(30, 90, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbQuestion1.setFont(font)
        self.lbQuestion1.setObjectName("lbQuestion1")
        self.lbAnswer1 = QtWidgets.QLabel(Form)
        self.lbAnswer1.setGeometry(QtCore.QRect(30, 120, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbAnswer1.setFont(font)
        self.lbAnswer1.setObjectName("lbAnswer1")
        self.lbQuestion2 = QtWidgets.QLabel(Form)
        self.lbQuestion2.setGeometry(QtCore.QRect(30, 160, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbQuestion2.setFont(font)
        self.lbQuestion2.setObjectName("lbQuestion2")
        self.lbAnswer2 = QtWidgets.QLabel(Form)
        self.lbAnswer2.setGeometry(QtCore.QRect(30, 200, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbAnswer2.setFont(font)
        self.lbAnswer2.setObjectName("lbAnswer2")
        self.lbQuestion3 = QtWidgets.QLabel(Form)
        self.lbQuestion3.setGeometry(QtCore.QRect(30, 240, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbQuestion3.setFont(font)
        self.lbQuestion3.setObjectName("lbQuestion3")
        self.lbAnswer3 = QtWidgets.QLabel(Form)
        self.lbAnswer3.setGeometry(QtCore.QRect(30, 280, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbAnswer3.setFont(font)
        self.lbAnswer3.setObjectName("lbAnswer3")
        self.btnDone = QtWidgets.QPushButton(Form)
        self.btnDone.setEnabled(True)
        self.btnDone.setGeometry(QtCore.QRect(110, 330, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDone.setFont(font)
        self.btnDone.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btnDone.setDefault(False)
        self.btnDone.setFlat(False)
        self.btnDone.setObjectName("btnDone")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.dialog=Form
        self.loadQuestions()
        self.btnDone.clicked.connect(self.addAnswers)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QuestionAnswerScreenModule"))
        self.lbQuestion1.setText(_translate("Form", "1.Soru"))
        self.lbAnswer1.setText(_translate("Form", "1.Cevap"))
        self.lbQuestion2.setText(_translate("Form", "2.Soru"))
        self.lbAnswer2.setText(_translate("Form", "2.Cevap"))
        self.lbQuestion3.setText(_translate("Form", "3.Soru"))
        self.lbAnswer3.setText(_translate("Form", "3.Cevap"))
        self.btnDone.setText(_translate("Form", "Tamam"))

    def loadQuestions(self):
        questionsOpr=databaseOperation.QuestionOperations('database.db')
        questions=questionsOpr.getQuestions()
        if(len(questions)!=0):
            for question in questions:
                self.cmbQuestion1.addItem(question[1])
                self.cmbQuestion2.addItem(question[1])
                self.cmbQuestion3.addItem(question[1])

    def addAnswers(self):
        questionsOpr=databaseOperation.QuestionOperations('database.db')
        answerOpr=databaseOperation.AnswerOperations('database.db')
        if(len(self.txtAnswer1.text())>0 and len(self.txtAnswer2.text())>0 and len(self.txtAnswer3.text())>0):
            print(questionsOpr.getQuestionID(self.cmbQuestion1.currentText()))
            answerOpr.addAnswer(questionsOpr.getQuestionID(self.cmbQuestion1.currentText()),self.tcNumber,self.txtAnswer1.text())
            answerOpr.addAnswer(questionsOpr.getQuestionID(self.cmbQuestion2.currentText()),self.tcNumber,self.txtAnswer2.text())
            answerOpr.addAnswer(questionsOpr.getQuestionID(self.cmbQuestion3.currentText()),self.tcNumber,self.txtAnswer3.text())
        print("Yanıtlarınız Eklendi...")
        self.dialog.close()
        self.homeWindow=QtWidgets.QWidget()
        self.uiHomeScreen=Ui_Form(self.tcNumber)
        self.uiHomeScreen.setupUi(self.homeWindow)
        self.homeWindow.show()