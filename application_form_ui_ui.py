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
)
import sys


class VITForm(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self):

        self.window().setFixedSize(800, 600)

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
        self.state_combo.setPlaceholderText("Eyalet Seçiniz")
        self.state_combo.addItems(
            [
                "Drenthe",
                "Flevoland",
                "Friesland",
                "Gelderland",
                "Groningen",
                "Limburg",
                "Noord-Brabant",
                "Noord-Holland",
                "Overijssel",
                "Utrecht",
                "Zeeland",
                "Zuid-Holland",
            ]
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
        self.a1_checkbox = QRadioButton("A1")
        self.a2_checkbox = QRadioButton("A2")
        self.b1_checkbox = QRadioButton("B1")
        self.b2_checkbox = QRadioButton("B2")
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
        self.email = self.email_input.text()
        self.name = self.name_input.text()
        self.phone = self.phone_input.text()
        self.postcode = self.postcode_input.text()
        self.state = self.state_combo.currentText()
        self.education = self.education_input.text()
        self.a1 = self.a1_checkbox.isChecked()
        self.a2 = self.a2_checkbox.isChecked()
        self.b1 = self.b1_checkbox.isChecked()
        self.b2 = self.b2_checkbox.isChecked()
        self.it_course = self.it_course_input.toPlainText()
        self.it_experience = self.it_experience_input.toPlainText()
        self.project = self.project_input.toPlainText()
        self.cloud = self.cloud_checkbox.isChecked()
        self.tester = self.tester_checkbox.isChecked()
        self.scrum = self.scrum_checkbox.isChecked()
        self.devops = self.devops_checkbox.isChecked()
        self.web = self.web_checkbox.isChecked()
        self.software = self.software_checkbox.isChecked()
        self.data = self.data_checkbox.isChecked()
        self.cyber = self.cyber_checkbox.isChecked()
        self.motivation = self.motivation_input.toPlainText()

        self.favorite_sector = [
            self.cloud_checkbox,
            self.tester_checkbox,
            self.scrum_checkbox,
            self.devops_checkbox,
            self.web_checkbox,
            self.software_checkbox,
            self.data_checkbox,
            self.cyber_checkbox,
        ]

        self.language_level = [
            self.a1_checkbox,
            self.a2_checkbox,
            self.b1_checkbox,
            self.b2_checkbox,
        ]

        self.form_data = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "postcode": self.postcode,
            "state": self.state,
            "education": self.education,
            "ecocomic_status": (
                lambda: (
                    self.economic_status_group.checkedButton().text()
                    if self.economic_status_group.checkedButton()
                    else None
                )
            )(),
            "follows_language_course": (
                lambda: "Evet" if self.course_yes.isChecked() else "Hayır"
            )(),
            "language_level": "".join(
                [*filter(lambda x: x.isChecked(), self.language_level)]
            ),
            "did_take_it_course": self.it_course,
            "it_experience": self.it_experience,
            "attended_project": self.project,
            "favorite_sector": [
                *map(
                    lambda x: x.text(),
                    [*filter(lambda x: x.isChecked(), self.favorite_sector)],
                )
            ],
        }

        print(self.form_data)

        if (
            not self.email
            or not self.name
            or not self.phone
            or not self.postcode
            or not self.state
            or not self.education
            or not self.form_data["ecocomic_status"]
            or not self.form_data["follows_language_course"]
            or not self.form_data["language_level"]
            or not self.it_course
            or not self.it_experience
            or not self.project
            or not self.form_data["favorite_sector"]
        ):
            QMessageBox.warning(self, "Hata", "Zorunlu alanlar doldurulmalı!")
        else:
            QMessageBox.information(self, "Başarılı", "Form başarıyla gönderildi!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VITForm()
    sys.exit(app.exec())
