import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_griba import Ui_Dialog
 
class MyFirstGuiProgram(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		self.pushButton1.clicked.connect(self.suma)

	def suma(self):
		a=self.lineEdit1.text()
		b=self.lineEdit2.text()
		x=float(a)
		y=float(b)
		#print(x+y)
		wynik=str(x+y)
		#print(wynik)
		self.label_3.setText(wynik)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstGuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())
