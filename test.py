from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QRadioButton,
    QButtonGroup,
    QCheckBox,
    QMessageBox,
    QTextEdit,
    QScrollArea,
    QFrame,
    QMainWindow,
)
import sys


class VITForm(QWidget):
    def __init__(self):
        super().__init__()
        MainWindow = QMainWindow()
        self.init_ui(MainWindow)

    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-image: url(./assets/zemin-buyuk.jpg);")
        # Form Layout
        form_layout = QVBoxLayout()

        # Email field
        self.email_label = QLabel("Email Adresiniz:")
        self.email_input = QLineEdit()
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)

        # Adınız Soyadınız
        self.name_label = QLabel("Adınız Soyadınız:")
        self.name_input = QLineEdit()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)

        # Telefon Numaranız
        self.phone_label = QLabel("Telefon Numaranız:")
        self.phone_input = QLineEdit()
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)

        # Posta Kodu
        self.postcode_label = QLabel("Posta Kodunuz:")
        self.postcode_input = QLineEdit()
        form_layout.addWidget(self.postcode_label)
        form_layout.addWidget(self.postcode_input)

        # Yaşadığınız Eyalet
        self.state_label = QLabel("Yaşadığınız Eyalet:")
        self.state_combo = QComboBox()
        self.state_combo.addItems(
            ["Seçenek 1", "Seçenek 2", "Seçenek 3"]
        )  # Seçenekleri özelleştirebilirsiniz
        form_layout.addWidget(self.state_label)
        form_layout.addWidget(self.state_combo)

        # Eğitim Durumu
        self.education_label = QLabel("Eğitim Durumunuz veya Uzmanlık Alanınız:")
        self.education_input = QLineEdit()
        form_layout.addWidget(self.education_label)
        form_layout.addWidget(self.education_input)

        # Ekonomik Durum (RadioButton)
        self.economic_status_label = QLabel("Ekonomik Durumunuz:")
        self.economic_status_group = QButtonGroup(self)
        self.uitkering_btn = QRadioButton("Uitkering Alıyorum")
        self.part_time_btn = QRadioButton(
            "Kısmen Uitkering Alıyorum - Parttime Çalışıyorum"
        )
        self.uwv_btn = QRadioButton("UWV den uitkering alıyorum")
        self.no_uitkering_btn = QRadioButton("Çalışıyorum (Uitkerinden Çıktım)")
        self.no_income_btn = QRadioButton("Kampta kaldığım için uitkering almıyorum")
        form_layout.addWidget(self.economic_status_label)
        form_layout.addWidget(self.uitkering_btn)
        form_layout.addWidget(self.part_time_btn)
        form_layout.addWidget(self.uwv_btn)
        form_layout.addWidget(self.no_uitkering_btn)
        form_layout.addWidget(self.no_income_btn)
        self.economic_status_group.addButton(self.uitkering_btn)
        self.economic_status_group.addButton(self.part_time_btn)
        self.economic_status_group.addButton(self.uwv_btn)
        self.economic_status_group.addButton(self.no_uitkering_btn)
        self.economic_status_group.addButton(self.no_income_btn)

        # Şu anda bir dil kursuna devam ediyor musunuz?
        self.course_label = QLabel("Şu anda bir dil kursuna devam ediyor musunuz?")
        self.course_yes = QRadioButton("Evet")
        self.course_no = QRadioButton("Hayır")
        self.course_group = QButtonGroup(self)
        self.course_group.addButton(self.course_yes)
        self.course_group.addButton(self.course_no)
        form_layout.addWidget(self.course_label)
        form_layout.addWidget(self.course_yes)
        form_layout.addWidget(self.course_no)

        # Yabancı Dil Seviyeniz (Checkbox)
        self.language_label = QLabel("Yabancı Dil Seviyeniz:")
        self.a1_checkbox = QCheckBox("A1")
        self.a2_checkbox = QCheckBox("A2")
        self.b1_checkbox = QCheckBox("B1")
        self.b2_checkbox = QCheckBox("B2")
        form_layout.addWidget(self.language_label)
        form_layout.addWidget(self.a1_checkbox)
        form_layout.addWidget(self.a2_checkbox)
        form_layout.addWidget(self.b1_checkbox)
        form_layout.addWidget(self.b2_checkbox)

        # IT Kursu/Tecrübe/Projeler (Multiple Text Areas)
        self.it_course_label = QLabel(
            "Başka bir IT kursu aldınız mı? (Eğer cevabınız evet ise detayları yazın)"
        )
        self.it_course_input = QTextEdit()
        form_layout.addWidget(self.it_course_label)
        form_layout.addWidget(self.it_course_input)

        self.it_experience_label = QLabel(
            "Daha önce herhangi bir IT iş tecrübeniz var mı?"
        )
        self.it_experience_input = QTextEdit()
        form_layout.addWidget(self.it_experience_label)
        form_layout.addWidget(self.it_experience_input)

        self.project_label = QLabel(
            "Öğretmenlik projesi veya Leerwerktraject gibi bir projeye dahil misiniz?"
        )
        self.project_input = QTextEdit()
        form_layout.addWidget(self.project_label)
        form_layout.addWidget(self.project_input)

        # IT Sektörü (CheckBoxes)
        self.it_sector_label = QLabel(
            "IT sektöründe hangi bölümde çalışmak istersiniz?"
        )
        self.cloud_checkbox = QCheckBox("Cloud Engineer")
        self.tester_checkbox = QCheckBox("Tester")
        self.scrum_checkbox = QCheckBox("Scrum Master")
        self.devops_checkbox = QCheckBox("DevOps Engineer")
        self.web_checkbox = QCheckBox("Web Tasarım")
        self.software_checkbox = QCheckBox("Software Developer")
        self.data_checkbox = QCheckBox("Data Engineer")
        self.cyber_checkbox = QCheckBox("Cyber Security")
        form_layout.addWidget(self.it_sector_label)
        form_layout.addWidget(self.cloud_checkbox)
        form_layout.addWidget(self.tester_checkbox)
        form_layout.addWidget(self.scrum_checkbox)
        form_layout.addWidget(self.devops_checkbox)
        form_layout.addWidget(self.web_checkbox)
        form_layout.addWidget(self.software_checkbox)
        form_layout.addWidget(self.data_checkbox)
        form_layout.addWidget(self.cyber_checkbox)

        # IT Motivasyon (Text Area)
        self.motivation_label = QLabel(
            "IT sektöründe kariyer yapmak için sizi harekete geçiren motivasyon nedir?"
        )
        self.motivation_input = QTextEdit()
        form_layout.addWidget(self.motivation_label)
        form_layout.addWidget(self.motivation_input)

        # Submit Button
        self.submit_button = QPushButton("Gönder")
        self.submit_button.clicked.connect(self.submit_form)
        form_layout.addWidget(self.submit_button)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_content.setLayout(form_layout)
        scroll_area.setWidget(scroll_content)

        # Set main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        # Set window size
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("VIT Projesi Başvuru Formu")
        self.show()

    def submit_form(self):
        # Example form validation (you can expand this)
        email = self.email_input.text()
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not email or not name or not phone:
            QMessageBox.warning(self, "Hata", "Zorunlu alanlar doldurulmalı!")
        else:
            QMessageBox.information(self, "Başarılı", "Form başarıyla gönderildi!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VITForm()
    sys.exit(app.exec())
