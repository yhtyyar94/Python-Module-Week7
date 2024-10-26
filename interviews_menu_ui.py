# Form implementation generated from reading ui file '/Users/yhtyyarannayev/Documents/GitHub/Python-Module-Week7/English/interviews_menu.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-image: url(./assets/zemin-buyuk.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color:white;\n" "font-size:36px;\n" "font-weight:bold;\n" "background:none"
        )
        self.label.setObjectName("label")
        self.exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_Button.setGeometry(QtCore.QRect(700, 180, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.exit_Button.setFont(font)
        self.exit_Button.setStyleSheet(
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
        self.exit_Button.setObjectName("exit_Button")
        self.project_send_Button = QtWidgets.QPushButton(self.centralwidget)
        self.project_send_Button.setGeometry(QtCore.QRect(290, 180, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.project_send_Button.setFont(font)
        self.project_send_Button.setStyleSheet(
            "QPushButton{\n"
            "color:black;\n"
            "background:white;\n"
            "border-radius:10px;\n"
            "font-weight:bold;\n"
            "}\n"
            "QPushButton::hover{\n"
            "color:white;\n"
            "background:#47545a;\n"
            "border-radius:10px;\n"
            "font-weight:bold\n"
            "}"
        )
        self.project_send_Button.setObjectName("project_send_Button")
        self.search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.search_Button.setGeometry(QtCore.QRect(700, 130, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.search_Button.setFont(font)
        self.search_Button.setStyleSheet(
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
        self.search_Button.setObjectName("search_Button")
        self.project_submitted_Button = QtWidgets.QPushButton(self.centralwidget)
        self.project_submitted_Button.setGeometry(QtCore.QRect(20, 180, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.project_submitted_Button.setFont(font)
        self.project_submitted_Button.setStyleSheet(
            "QPushButton{\n"
            "color:black;\n"
            "background:white;\n"
            "border-radius:10px;\n"
            "font-weight:bold;\n"
            "}\n"
            "QPushButton::hover{\n"
            "color:white;\n"
            "background:#47545a;\n"
            "border-radius:10px;\n"
            "font-weight:bold\n"
            "}"
        )
        self.project_submitted_Button.setObjectName("project_submitted_Button")
        self.mainmenu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_Button.setGeometry(QtCore.QRect(560, 180, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.mainmenu_Button.setFont(font)
        self.mainmenu_Button.setStyleSheet(
            "QPushButton{\n"
            "color:black;\n"
            "background:white;\n"
            "border-radius:10px;\n"
            "font-weight:bold;\n"
            "}\n"
            "QPushButton::hover{\n"
            "color:white;\n"
            "background:#47545a;\n"
            "border-radius:10px;\n"
            "font-weight:bold\n"
            "}"
        )
        self.mainmenu_Button.setObjectName("mainmenu_Button")
        self.search_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.search_Line.setGeometry(QtCore.QRect(20, 130, 661, 31))
        self.search_Line.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:10px;\n"
            "background:none;\n"
            "padding:5px\n"
            "}\n"
            ""
        )
        self.search_Line.setText("")
        self.search_Line.setObjectName("search_Line")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 240, 761, 351))
        font = QtGui.QFont()
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("\n" "font-weight:bold;\n" "background:none")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(
            _translate(
                "MainWindow",
                '<html><head/><body><p><img src=":/arkaplan/WhatsApp Image 2024-10-17 at 23.49.08.jpeg"/></p></body></html>',
            )
        )
        self.label.setText(_translate("MainWindow", "INTERVIEWS"))
        self.exit_Button.setText(_translate("MainWindow", "EXIT"))
        self.project_send_Button.setText(
            _translate("MainWindow", "PROJECT SEND CANDIDATES")
        )
        self.search_Button.setText(_translate("MainWindow", "SEARCH"))
        self.project_submitted_Button.setText(
            _translate("MainWindow", "PROJECT SUBMITTED CANDIDATES")
        )
        self.mainmenu_Button.setText(_translate("MainWindow", "MAIN MENU"))
        self.search_Line.setPlaceholderText(
            _translate("MainWindow", "Enter a Text to Search")
        )
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name Surname"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project Submission Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Project Sent Date"))
