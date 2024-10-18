from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Basvurular_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular_2.setGeometry(QtCore.QRect(300, 350, 141, 31))
        self.Basvurular_2.setAutoFillBackground(False)
        self.Basvurular_2.setStyleSheet("background-color:#d45500; font-size:12pt; color:white")
        self.Basvurular_2.setObjectName("Basvurular_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/testx/Users/Windows 10/Downloads/zemin-kucuk.jpg);\n"
"width:800px;\n"
"height:600px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Basvurular = QtWidgets.QPushButton(parent=self.frame)
        self.Basvurular.setGeometry(QtCore.QRect(80, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("background-color:#05a90c; font-size:12pt; color:white")
        self.Basvurular.setObjectName("Basvurular")
        self.Mentor = QtWidgets.QPushButton(parent=self.frame)
        self.Mentor.setGeometry(QtCore.QRect(560, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("background-color:#4d0094; font-size:12pt; color:white")
        self.Mentor.setObjectName("Mentor")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(700, 540, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:#800000; font-size:12pt; color:white")
        self.pushButton.setObjectName("pushButton")
        self.Adminmenu = QtWidgets.QPushButton(parent=self.frame)
        self.Adminmenu.setGeometry(QtCore.QRect(440, 280, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("background-color:#7d003b; font-size:12pt; color:white")
        self.Adminmenu.setObjectName("Adminmenu")
        self.Anamenu = QtWidgets.QPushButton(parent=self.frame)
        self.Anamenu.setGeometry(QtCore.QRect(190, 280, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("background-color:#363636; font-size:12pt; color:white")
        self.Anamenu.setObjectName("Anamenu")
        self.frame.raise_()
        self.Basvurular_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Basvurular_2.setText(_translate("MainWindow", "MÜLAKATLAR"))
        self.Basvurular.setText(_translate("MainWindow", "BAŞVURULAR"))
        self.Mentor.setText(_translate("MainWindow", "MENTÖR GÖRÜŞMESİ"))
        self.pushButton.setText(_translate("MainWindow", "KAPAT"))
        self.Adminmenu.setText(_translate("MainWindow", "ADMIN MENÜ"))
        self.Anamenu.setText(_translate("MainWindow", "ANA MENÜ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
