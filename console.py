from PyQt5 import QtCore, QtGui, QtWidgets
from rsa import RSA
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 650)				#(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 165, 101, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.GenKey)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(570, 410, 101, 40))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.encode)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 485, 101, 40))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.decode)

#        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_3.setGeometry(QtCore.QRect(570, 115, 101, 40))
#        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#        self.pushButton_3.setObjectName("pushButton_3")
#        self.pushButton_3.clicked.connect(self.readText)

#        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_4.setGeometry(QtCore.QRect(270, 550, 101, 40))
#        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#        self.pushButton_4.setObjectName("pushButton_4")
#        self.pushButton_4.clicked.connect(self.saveText)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)	
        self.label_1.setGeometry(QtCore.QRect(10, 110, 105, 50))		#QtCore.QRect(left, top, width, height)
        self.label_1.setObjectName("label_1")			
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 47, 22))	
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 245, 47, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 47, 22))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 315, 47, 22))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 350, 47, 22))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 400, 55, 22))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 480, 55, 22))
        self.label_8.setObjectName("label_8")

        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(115, 110, 445, 40))
        self.message.setObjectName("message")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 20, 200, 50))
        self.textEdit.setObjectName("textEdit")
        self.p1 = QtWidgets.QLineEdit(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(70, 210, 490, 22))
        self.p1.setObjectName("p1")
        self.q1 = QtWidgets.QLineEdit(self.centralwidget)
        self.q1.setGeometry(QtCore.QRect(70, 245, 490, 22))
        self.q1.setObjectName("q1")
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(70, 280, 490, 22))
        self.e1.setObjectName("e1")
        self.d1 = QtWidgets.QLineEdit(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(70, 315, 490, 22))
        self.d1.setObjectName("d1")
        self.N1 = QtWidgets.QLineEdit(self.centralwidget)
        self.N1.setGeometry(QtCore.QRect(70, 350, 490, 22))
        self.N1.setObjectName("N1")
        self.enc1 = QtWidgets.QTextEdit(self.centralwidget)
        self.enc1.setGeometry(QtCore.QRect(70, 400, 490, 60))
        self.enc1.setObjectName("enc1")
        self.enc1.setReadOnly = True
        self.dec1 = QtWidgets.QTextEdit(self.centralwidget)
        self.dec1.setGeometry(QtCore.QRect(70, 480, 490, 50))
        self.dec1.setObjectName("dec1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.enc = 0

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Connect with app
    
    def GenKey(self):
        self.rsa = RSA(keysize=32)

        self.p1.setText(str(self.rsa.p))
        self.q1.setText(str(self.rsa.q))
        self.d1.setText(str(self.rsa.d))
        self.e1.setText(str(self.rsa.e))
        self.N1.setText(str(self.rsa.N))

    def encode(self):
        msg = self.message.toPlainText()
        enc = self.rsa.encrypt(msg)
        self.enc = enc
        self.enc1.setText(str(enc))

    def decode(self):
        dec = self.rsa.decrypt(self.enc)
        self.dec1.setText(str(dec))

#    def readText(self):
#        print("read")
#    def saveText(self):
#        print("save")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA CRYPTOSYSTEM"))
        self.pushButton.setText(_translate("MainWindow", "Gen Key"))
        self.pushButton_1.setText(_translate("MainWindow", "Enc"))
        self.pushButton_2.setText(_translate("MainWindow", "Dec"))
#        self.pushButton_3.setText(_translate("MainWindow", "Read"))
#        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.label_1.setText(_translate("MainWindow", "Enter Message "))
        self.label_2.setText(_translate("MainWindow", "p"))
        self.label_3.setText(_translate("MainWindow", "q"))
        self.label_4.setText(_translate("MainWindow", "e"))
        self.label_5.setText(_translate("MainWindow", "d"))
        self.label_6.setText(_translate("MainWindow", "N"))
        self.label_7.setText(_translate("MainWindow", "Encrypt"))
        self.label_8.setText(_translate("MainWindow", "Decrypt"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\"></span>Hệ mật RSA</p></body></html>"))
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
