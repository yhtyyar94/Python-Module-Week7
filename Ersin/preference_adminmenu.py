from PyQt6 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Resim yolunu belirleme
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, 'images', 'zemin_buyuk.jpg')
        image_url = f"file:///{image_path.replace(os.sep, '/')}"

        # Stil sayfasını ayarlama
        self.centralwidget.setStyleSheet(f"""
            QWidget {{
                background-image: url("{image_url}");
                background-repeat: no-repeat;
                background-position: center;
            }}
        """)

        # Diğer widget'ları ekleme
        self.Basvurular_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular_2.setGeometry(QtCore.QRect(300, 350, 141, 31))
        self.Basvurular_2.setAutoFillBackground(False)
        self.Basvurular_2.setStyleSheet("""
            QPushButton{
                color:black;
                background:white;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.Basvurular_2.setObjectName("Basvurular_2")

        self.Basvurular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular.setGeometry(QtCore.QRect(80, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("""
            QPushButton{
                color:black;
                background:white;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.Basvurular.setObjectName("Basvurular")

        self.Mentor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Mentor.setGeometry(QtCore.QRect(560, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("""
            QPushButton{
                color:black;
                background:white;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.Mentor.setObjectName("Mentor")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 540, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("""
            QPushButton{
                color:white;
                background:red;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.pushButton.setObjectName("pushButton")

        self.Adminmenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Adminmenu.setGeometry(QtCore.QRect(440, 280, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("""
            QPushButton{
                color:black;
                background:white;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.Adminmenu.setObjectName("Adminmenu")

        self.Anamenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Anamenu.setGeometry(QtCore.QRect(190, 280, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("""
            QPushButton{
                color:black;
                background:white;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                color:white;
                background:#47545a;
                border-radius:10px;
                font-weight:bold
            }
        """)
        self.Anamenu.setObjectName("Anamenu")

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
