# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionAuthenticationScreenModule.ui'
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QuestionAuthenticationScreenModule"))
        self.btnDone.setText(_translate("Form", "Onayla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())