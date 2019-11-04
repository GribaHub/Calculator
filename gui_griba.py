# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_griba.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(235, 171)
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 161, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.pushButton2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton1.setText(_translate("Dialog", "Suma"))
        self.pushButton2.setText(_translate("Dialog", "Koniec"))
        self.label.setText(_translate("Dialog", "Podaj a="))
        self.label_2.setText(_translate("Dialog", "Podaj b="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

