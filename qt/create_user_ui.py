# Form implementation generated from reading ui file '/Users/yhtyyar/Documents/GitHub/Python-Module-Week7/qt/create_user.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_user(object):
    def setupUi(self, create_user):
        create_user.setObjectName("create_user")
        create_user.resize(350, 300)
        create_user.setStyleSheet("background-image: url(./assets/create_user.jpg);")
        self.select_candidate = QtWidgets.QLabel(parent=create_user)
        self.select_candidate.setGeometry(QtCore.QRect(40, 180, 51, 16))
        self.select_candidate.setStyleSheet("font-weight:bold;\n"
"background:none;")
        self.select_candidate.setObjectName("select_candidate")
        self.role = QtWidgets.QComboBox(parent=create_user)
        self.role.setGeometry(QtCore.QRect(40, 200, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.role.setFont(font)
        self.role.setStyleSheet("QComboBox{\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"background:white;\n"
"color:black\n"
"}")
        self.role.setIconSize(QtCore.QSize(16, 16))
        self.role.setFrame(True)
        self.role.setObjectName("role")
        self.role.addItem("")
        self.role.addItem("")
        self.username = QtWidgets.QLineEdit(parent=create_user)
        self.username.setGeometry(QtCore.QRect(40, 60, 271, 31))
        self.username.setStyleSheet("padding:5px;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"background:white;\n"
"color:black\n"
"")
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(parent=create_user)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setStyleSheet("font-weight:bold;\n"
"background:none;")
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(parent=create_user)
        self.password.setGeometry(QtCore.QRect(42, 130, 271, 31))
        self.password.setStyleSheet("padding:5px;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"background:white;\n"
"color:black\n"
"")
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(parent=create_user)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 16))
        self.label_2.setStyleSheet("font-weight:bold;\n"
"background:none;")
        self.label_2.setObjectName("label_2")
        self.create_button = QtWidgets.QPushButton(parent=create_user)
        self.create_button.setGeometry(QtCore.QRect(110, 250, 120, 32))
        self.create_button.setStyleSheet("QPushButton{\n"
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
        self.create_button.setObjectName("create_button")

        self.retranslateUi(create_user)
        QtCore.QMetaObject.connectSlotsByName(create_user)

    def retranslateUi(self, create_user):
        _translate = QtCore.QCoreApplication.translate
        create_user.setWindowTitle(_translate("create_user", "Create User"))
        self.select_candidate.setText(_translate("create_user", "Role"))
        self.role.setCurrentText(_translate("create_user", "admin"))
        self.role.setItemText(0, _translate("create_user", "admin"))
        self.role.setItemText(1, _translate("create_user", "user"))
        self.username.setPlaceholderText(_translate("create_user", "Enter the username..."))
        self.label.setText(_translate("create_user", "Username"))
        self.password.setPlaceholderText(_translate("create_user", "Enter the password..."))
        self.label_2.setText(_translate("create_user", "Password"))
        self.create_button.setText(_translate("create_user", "Create"))
