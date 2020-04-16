# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
class Ui_Form(object):
    numbers = [0,1,2,3,4,5,6,7,8,9] 
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(319, 400)
        self.n7 = QtWidgets.QPushButton(Form)
        self.n7.setGeometry(QtCore.QRect(10, 110, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n7.setFont(font)
        self.n7.setObjectName("n7")
        self.n6 = QtWidgets.QPushButton(Form)
        self.n6.setGeometry(QtCore.QRect(150, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n6.setFont(font)
        self.n6.setObjectName("n6")
        self.n5 = QtWidgets.QPushButton(Form)
        self.n5.setGeometry(QtCore.QRect(80, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n5.setFont(font)
        self.n5.setObjectName("n5")
        self.n4 = QtWidgets.QPushButton(Form)
        self.n4.setGeometry(QtCore.QRect(10, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n4.setFont(font)
        self.n4.setObjectName("n4")
        self.n1 = QtWidgets.QPushButton(Form)
        self.n1.setGeometry(QtCore.QRect(10, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n1.setFont(font)
        self.n1.setObjectName("n1")
        self.n2 = QtWidgets.QPushButton(Form)
        self.n2.setGeometry(QtCore.QRect(80, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n2.setFont(font)
        self.n2.setObjectName("n2")
        self.n8 = QtWidgets.QPushButton(Form)
        self.n8.setGeometry(QtCore.QRect(80, 110, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n8.setFont(font)
        self.n8.setObjectName("n8")
        self.n9 = QtWidgets.QPushButton(Form)
        self.n9.setGeometry(QtCore.QRect(150, 110, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n9.setFont(font)
        self.n9.setObjectName("n9")
        self.n3 = QtWidgets.QPushButton(Form)
        self.n3.setGeometry(QtCore.QRect(150, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n3.setFont(font)
        self.n3.setObjectName("n3")
        self.n0 = QtWidgets.QPushButton(Form)
        self.n0.setGeometry(QtCore.QRect(10, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.n0.setFont(font)
        self.n0.setObjectName("n0")
        self.lPantalla = QtWidgets.QLabel(Form)
        self.lPantalla.setEnabled(True)
        self.lPantalla.setGeometry(QtCore.QRect(10, 30, 301, 61))
        self.lPantalla.setStyleSheet("background-color: rgb(0, 0, 100);color: rgb(255,255,255);")
        self.lPantalla.setText("")
        self.lPantalla.setObjectName("lPantalla")
        self.nPunto = QtWidgets.QPushButton(Form)
        self.nPunto.setGeometry(QtCore.QRect(80, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nPunto.setFont(font)
        self.nPunto.setObjectName("nPunto")
        self.nIgual = QtWidgets.QPushButton(Form)
        self.nIgual.setGeometry(QtCore.QRect(150, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nIgual.setFont(font)
        self.nIgual.setObjectName("nIgual")
        self.bBorrar = QtWidgets.QPushButton(Form)
        self.bBorrar.setGeometry(QtCore.QRect(240, 120, 70, 54))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bBorrar.setFont(font)
        self.bBorrar.setObjectName("bBorrar")
        self.bDividir = QtWidgets.QPushButton(Form)
        self.bDividir.setGeometry(QtCore.QRect(240, 170, 70, 54))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bDividir.setFont(font)
        self.bDividir.setObjectName("bDividir")
        self.bMultiplicar = QtWidgets.QPushButton(Form)
        self.bMultiplicar.setGeometry(QtCore.QRect(240, 220, 70, 54))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bMultiplicar.setFont(font)
        self.bMultiplicar.setObjectName("bMultiplicar")
        self.bRestar = QtWidgets.QPushButton(Form)
        self.bRestar.setGeometry(QtCore.QRect(240, 270, 70, 54))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bRestar.setFont(font)
        self.bRestar.setObjectName("bRestar")
        self.bSumar = QtWidgets.QPushButton(Form)
        self.bSumar.setGeometry(QtCore.QRect(240, 320, 70, 54))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bSumar.setFont(font)
        self.bSumar.setObjectName("bSumar")
        
        
        self.n0.clicked.connect(self.imprimir)
        self.n1.clicked.connect(self.imprimir1)
        
        self.n2.clicked.connect(self.imprimir2)
        self.n3.clicked.connect(self.imprimir3)
        self.n4.clicked.connect(self.imprimir4)
        self.n5.clicked.connect(self.imprimir5)
        self.n6.clicked.connect(self.imprimir6)
        self.n7.clicked.connect(self.imprimir7)
        self.n8.clicked.connect(self.imprimir8)
        self.n9.clicked.connect(self.imprimir9)
        self.bSumar.clicked.connect(self.imprimirplus)
        self.bRestar.clicked.connect(self.imprimirminus)
        self.bMultiplicar.clicked.connect(self.imprimirby)
        self.bDividir.clicked.connect(self.imprimirdiv)
        self.nIgual.clicked.connect(self.resultado)
        self.bBorrar.clicked.connect(self.delete)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

        self.number = ''
        self.number1 = ''
        self.operador = '' 
        self.result = '' 
  
        
    def imprimir(self):
        
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '0')
            self.number = self.number + '0'        
        else:
            self.lPantalla.setText(str(self.number1) + '0')
            self.number1 = self.number1 + '0'
    
    def imprimir1(self):
        
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '1')
            self.number = self.number + '1'
        else:
            self.lPantalla.setText(str(self.number1) + '1')
            self.number1 = self.number1 + '1'

    def imprimir2(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '2')
            self.number = self.number + '2'
        else:
            self.lPantalla.setText(str(self.number1) + '2')
            self.number1 = self.number1 + '2'
        
    def imprimir3(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '3')
            self.number = self.number + '3'
        else:
            self.lPantalla.setText(str(self.number1) + '3')
            self.number1 = self.number1 + '3'
    def imprimir4(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '4')
            self.number = self.number + '4'
        else:
            self.lPantalla.setText(str(self.number1) + '4')
            self.number1 = self.number1 + '4'
    def imprimir5(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '5')
            self.number = self.number + '5'
        else:
            self.lPantalla.setText(str(self.number1) + '5')
            self.number1 = self.number1 + '5'
    def imprimir6(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '6')
            self.number = self.number + '6'
        else:
            self.lPantalla.setText(str(self.number1) + '6')
            self.number1 = self.number1 + '6'
    def imprimir7(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '7')
            self.number = self.number + '7'
        else:
            self.lPantalla.setText(str(self.number1) + '7')
            self.number1 = self.number1 + '7'
    def imprimir8(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '8')
            self.number = self.number + '8'
        else:
            self.lPantalla.setText(str(self.number1) + '8')
            self.number1 = self.number1 + '8'
    def imprimir9(self):
        if self.operador == '':
            self.lPantalla.setText(str(self.number) + '9')
            self.number = self.number + '9'
        else:
            self.lPantalla.setText(str(self.number1) + '9')
            self.number1 = self.number1 + '9'
        

         

    def imprimirplus(self):
        self.lPantalla.setText(str(self.number) + ' + ')
        self.operador = '+'
        time.sleep(0.5)
        self.lPantalla.clear()
    def imprimirminus(self):
        self.lPantalla.setText(str(self.number) + ' -')
        self.operador = '-'
        time.sleep(0.5)
        self.lPantalla.clear()
    def imprimirby(self):
        self.lPantalla.setText(str(self.number) + ' *')
        self.operador = '*'
        time.sleep(0.5)
        self.lPantalla.clear()
    def imprimirdiv(self):
        self.lPantalla.setText(str(self.number) + ' /')
        self.operador = '/'
        time.sleep(0.5)
        self.lPantalla.clear()

    def resultado(self):
        self.lPantalla.clear()
        if self.operador == '':
            self.result = self.number
            

        elif self.operador == '-':
            self.result = int(self.number)-int(self.number1)
            self.number = self.result
            

        elif self.operador == '*':
            self.result = int(self.number)*int(self.number1)
            self.number = self.result
            

        elif self.operador == '/':
            self.result = int(self.number)//int(self.number1)
            self.number = self.result
            
        
        elif self.operador == '+':
            self.result = int(self.number)+int(self.number1)  

        self.lPantalla.setText(str(self.result))
        self.number = self.result
        self.operador = ''
        self.number1 = ''
        self.result =''

    def delete(self):
        self.number = ''
        self.number1 = ''
        self.operador = ''
        self.result = '' 
        self.lPantalla.clear()   

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "calculadora"))
        self.n7.setText(_translate("Form", "7"))
        self.n6.setText(_translate("Form", "6"))
        self.n5.setText(_translate("Form", "5"))
        self.n4.setText(_translate("Form", "4"))
        self.n1.setText(_translate("Form", "1"))
        self.n2.setText(_translate("Form", "2"))
        self.n8.setText(_translate("Form", "8"))
        self.n9.setText(_translate("Form", "9"))
        self.n3.setText(_translate("Form", "3"))
        self.n0.setText(_translate("Form", "0"))
        self.nPunto.setText(_translate("Form", "."))
        self.nIgual.setText(_translate("Form", "="))
        self.bBorrar.setText(_translate("Form", "Del"))
        self.bDividir.setText(_translate("Form", "/"))
        self.bMultiplicar.setText(_translate("Form", "x"))
        self.bRestar.setText(_translate("Form", "-"))
        self.bSumar.setText(_translate("Form", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

