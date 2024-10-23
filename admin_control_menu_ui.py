# Form implementation generated from reading ui file '/Users/yhtyyar/Documents/GitHub/Python-Module-Week7/admin_control_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-image: url(./assets/zemin-buyuk.jpg);\n"
"QWidget::setFixedSize(800, 600);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 70, 241, 41))
        self.label.setStyleSheet("color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none")
        self.label.setObjectName("label")
        self.etkinlik_kontrol = QtWidgets.QPushButton(parent=self.centralwidget)
        self.etkinlik_kontrol.setGeometry(QtCore.QRect(20, 170, 161, 41))
        self.etkinlik_kontrol.setStyleSheet("QPushButton{\n"
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
"}")
        self.etkinlik_kontrol.setObjectName("etkinlik_kontrol")
        self.cikis = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cikis.setGeometry(QtCore.QRect(20, 410, 161, 41))
        self.cikis.setStyleSheet("QPushButton{\n"
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
        self.cikis.setObjectName("cikis")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 170, 581, 411))
        self.tableWidget.setStyleSheet("background:white;\n"
"border-radius:10px;\n"
"padding:5px;\n"
"color:black")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.mail_gonder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mail_gonder.setGeometry(QtCore.QRect(20, 250, 161, 41))
        self.mail_gonder.setStyleSheet("QPushButton{\n"
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
"}")
        self.mail_gonder.setObjectName("mail_gonder")
        self.tercihler = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tercihler.setGeometry(QtCore.QRect(20, 330, 161, 41))
        self.tercihler.setStyleSheet("QPushButton{\n"
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
"}")
        self.tercihler.setObjectName("tercihler")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADMIN MENU"))
        self.etkinlik_kontrol.setText(_translate("MainWindow", "Etkinlik Kontrol"))
        self.cikis.setText(_translate("MainWindow", "Çıkış"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Etkinlik Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Başlanıç Zamanı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Katılımcı Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Oranizatör Email"))
        self.mail_gonder.setText(_translate("MainWindow", "Mail  Gönder"))
        self.tercihler.setText(_translate("MainWindow", "Tercihler"))
