# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(
            "background-image: url(./assets/login.jpg);\n"
            "QWidget::setFixedSize(800, 600);\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 270, 151, 61))
        self.label.setStyleSheet(
            "color:white;\n" "font-size:36px;\n" "font-weight:bold;\n" "background:none"
        )
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 101, 20))
        self.label_2.setStyleSheet(
            "color:white;\n" "font-size:18px;\n" "font-weight:400;\n" "background:none"
        )
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 290, 281, 31))
        self.lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:10px;\n"
            "background:none;\n"
            "padding:5px\n"
            "}\n"
            ""
        )
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 370, 281, 31))
        self.lineEdit_2.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:10px;\n"
            "background:none;\n"
            "padding:5px\n"
            "}\n"
            ""
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 340, 101, 20))
        self.label_3.setStyleSheet(
            "color:white;\n" "font-size:18px;\n" "font-weight:400;\n" "background:none"
        )
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 430, 121, 32))
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "color:white;\n"
            "background:#db1e3c;\n"
            "border-radius:10px;\n"
            "font-weight:bold;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "color:#db1e3c;\n"
            "background:white;\n"
            "border-radius:10px;\n"
            "font-weight:bold\n"
            "}"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 430, 121, 32))
        self.pushButton_2.setStyleSheet(
            "QPushButton{\n"
            "color:white;\n"
            "background:#47545a;\n"
            "border-radius:10px;\n"
            "font-weight:bold;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "color:#47545a;\n"
            "background:white;\n"
            "border-radius:10px;\n"
            "font-weight:bold\n"
            "}"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 330, 101, 61))
        self.label_4.setStyleSheet(
            "color:white;\n" "font-size:36px;\n" "font-weight:bold;\n" "background:none"
        )
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " CRM V.2"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter your username")
        )
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "Enter your password")
        )
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "VIT 5"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
