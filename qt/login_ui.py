# Form implementation generated from reading ui file '/Users/yhtyyar/Documents/GitHub/Python-Module-Week7/qt/login.ui'
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
        MainWindow.setFixedSize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet("background-image: url(./assets/login.jpg);\n"
"QWidget::setFixedSize(800, 600);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 270, 151, 61))
        self.label.setStyleSheet("color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 101, 20))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:18px;\n"
"font-weight:400;\n"
"background:none")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 290, 281, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"background:none;\n"
"padding:5px\n"
"}\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 370, 281, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"background:none;\n"
"padding:5px\n"
"}\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 340, 101, 20))
        self.label_3.setStyleSheet("color:white;\n"
"font-size:18px;\n"
"font-weight:400;\n"
"background:none")
        self.label_3.setObjectName("label_3")
        self.login_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(460, 430, 121, 32))
        self.login_button.setStyleSheet("QPushButton{\n"
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
"}")
        self.login_button.setObjectName("login_button")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(620, 430, 121, 32))
        self.exit_button.setStyleSheet("QPushButton{\n"
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
"}")
        self.exit_button.setObjectName("exit_button")
        self.apply_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.apply_button.setGeometry(QtCore.QRect(100, 340, 201, 41))
        self.apply_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.apply_button.setStyleSheet("QPushButton::hover{\n"
"color:white;\n"
"background:#db1e3c;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:#db1e3c;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.apply_button.setObjectName("apply_button")
        self.error_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(180, 530, 421, 20))
        self.error_message.setStyleSheet("color:red;\n"
"font-weight:bold;\n"
"font-size:18px;\n"
"background:none")
        self.error_message.setText("")
        self.error_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_message.setObjectName("error_message")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " CRM V.2"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your username..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your password..."))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.apply_button.setText(_translate("MainWindow", "Apply our next VIT course"))
