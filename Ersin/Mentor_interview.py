import os
from PyQt6 import QtCore, QtGui, QtWidgets
from preference_adminmenu import Ui_MainWindow as AdminMenuWindow  # Admin menu arayüzünü dahil et

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
        self.background_label.setScaledContents(True)  # Resmin QLabel boyutlarına göre ölçeklenmesini sağlar

        # Dinamik yol ile resim ekleme
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'zemin-buyuk.jpg')

        # Resmi QLabel'a ekle
        pixmap = QtGui.QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image: {image_path}")
        self.background_label.setPixmap(pixmap)
        self.background_label.lower()  # Resmi arka plana yerleştir

        # Başlık etiketi
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 70, 311, 61))
        self.label.setStyleSheet("""
            QLabel{
                color:white;
                font-size:36px;
                font-weight:bold;
                background:none;
            }
        """)
        self.label.setObjectName("label")

        # Kullanıcı adı girişi
        self.Username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(520, 230, 171, 31))
        self.Username.setObjectName("Username")
        self.Username.setPlaceholderText("UserName")

        # Şifre girişi
        self.Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(520, 270, 171, 31))
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Şifre gizleme
        self.Password.setPlaceholderText("Password")

        # Giriş butonu
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 320, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("LOGIN")
        self.pushButton.setStyleSheet("""
            QPushButton{
                background-color:#05a90c; 
                font-size:12pt; 
                color:white;
                border-radius:10px;
            }
            QPushButton::hover{
                background-color:#47545a;
            }
        """)

        # Diğer butonlar ve widget'lar
        self.Basvurular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular.setGeometry(QtCore.QRect(80, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("background-color:#05a90c; font-size:12pt; color:white")
        self.Basvurular.setObjectName("Basvurular")
        self.Basvurular.setText("BAŞVURULAR")

        self.Mentor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Mentor.setGeometry(QtCore.QRect(560, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("background-color:#4d0094; font-size:12pt; color:white")
        self.Mentor.setObjectName("Mentor")
        self.Mentor.setText("MENTÖR GÖRÜŞMESİ")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 170, 75, 24))
        self.pushButton_2.setStyleSheet("""
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
                font-weight:bold;
            }
        """)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("BUL")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 170, 241, 22))
        self.lineEdit.setStyleSheet("""
            QLineEdit{
                color:black;
                background:white;
                font-weight:bold;
            }
        """)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("ARANACAK METNİ GİRİNİZ")

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 10, 201, 24))
        self.pushButton_3.setStyleSheet("""
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
                font-weight:bold;
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("TÜM GÖRÜŞMELER")

        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 170, 281, 22))
        self.comboBox.setStyleSheet("""
            QComboBox{
                color:black;
                background:white;
                font-weight:bold;
            }
        """)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([
            "Vıt Projesinin Tamamına Katılması Uygun Olur",
            "VIT Projesi ilk IT Eğtimi Al... ya Yönlendirilmesi Uygun Olur",
            "VIT Projesi İngilizce Eğtimi Al... ya Yönlendirilmesi Uygun Olur",
            "Vit Pojesi Kapsamında Dir.. Yönlendirilmesi Uygun Olur",
            "Direkt Bireysel Koçluk İle İşe Yönlendirilmesi Uygun Olur",
            "Bir Sonraki VIT Projesine Katılması Daha Uygun Olur",
            "Başka Bir Sektöre Yönlendirilmesi",
            "Diğer"
        ])

        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 200, 800, 341))
        self.tableView.setStyleSheet("""
            QTableView{
                color:black;
                background:white;
                font-weight:bold;
            }
        """)
        self.tableView.setObjectName("tableView")

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 545, 75, 30))
        self.pushButton_4.setStyleSheet("""
            QPushButton{
                color:white;
                background:red;
                border-radius:10px;
                font-weight:bold;
            }
            QPushButton::hover{
                background:#47545a;
            }
        """)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("KAPAT")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 91, 24))
        self.pushButton_5.setStyleSheet("""
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
                font-weight:bold;
            }
        """)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("TERCİHLER")

        # Giriş butonuna tıklama olayı
        self.pushButton.clicked.connect(self.open_admin_menu)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Mentor Interview"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:30pt; font-weight:1200; color:#ffffff;\">CRM PROJECT</span></p></body></html>"))

    def open_admin_menu(self):
        # Admin menüyü açmak için
        self.window = QtWidgets.QMainWindow()  # Yeni bir QMainWindow oluşturuluyor
        self.ui = AdminMenuWindow()  # preference_admin_menu dosyasındaki Ui_MainWindow sınıfı kullanılıyor
        self.ui.setupUi(self.window)  # Arayüz setup ediliyor
        self.window.show()  # Yeni pencere gösteriliyor

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
