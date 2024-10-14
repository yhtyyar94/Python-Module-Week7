import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Merkez widget oluştur
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # QLabel kullanarak arka plan resmi
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))

        # Dinamik yol ile resim ekleme
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'admin.jpg')
        print(f"Background image path: {image_path}")
        
        # Resmi QLabel'a ekle
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # Resmin QLabel boyutlarına göre ölçeklenmesi
        self.background_label.lower()  # Resmi arka plana yerleştir

        # Diğer UI elementleri
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 230, 411, 61))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 420, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:#800000; font-size:12pt; color:white")
        self.pushButton.setObjectName("pushButton")

        self.Basvurular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular.setGeometry(QtCore.QRect(180, 300, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("background-color:#05a90c; font-size:12pt; color:white")
        self.Basvurular.setObjectName("Basvurular")

        self.Mentor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Mentor.setGeometry(QtCore.QRect(350, 300, 261, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("background-color:#4d0094; font-size:12pt; color:white")
        self.Mentor.setObjectName("Mentor")

        self.Basvurular_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular_2.setGeometry(QtCore.QRect(300, 350, 141, 31))
        self.Basvurular_2.setAutoFillBackground(False)
        self.Basvurular_2.setStyleSheet("background-color:#d45500; font-size:12pt; color:white")
        self.Basvurular_2.setObjectName("Basvurular_2")

        self.Anamenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Anamenu.setGeometry(QtCore.QRect(140, 420, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("background-color:#363636; font-size:12pt; color:white")
        self.Anamenu.setObjectName("Anamenu")

        self.Adminmenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Adminmenu.setGeometry(QtCore.QRect(350, 420, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("background-color:#7d003b; font-size:12pt; color:white")
        self.Adminmenu.setObjectName("Adminmenu")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">YÖNETİM PANELİNE HOŞGELDİNİZ</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "KAPAT"))
        self.Basvurular.setText(_translate("MainWindow", "BAŞVURULAR"))
        self.Mentor.setText(_translate("MainWindow", "MENTÖR GÖRÜŞMESİ"))
        self.Basvurular_2.setText(_translate("MainWindow", "MÜLAKATLAR"))
        self.Anamenu.setText(_translate("MainWindow", "ANA MENÜ"))
        self.Adminmenu.setText(_translate("MainWindow", "ADMIN MENÜ"))
