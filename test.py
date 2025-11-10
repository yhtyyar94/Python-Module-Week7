import sys
from PyQt6 import QtWidgets, QtGui
from qt.application_menu_ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
# set data to table widget
ui.tableWidget.setRowCount(10)
ui.tableWidget.setColumnCount(5)
ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Email", "Status", "Score"])
ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f"Yhtyyar, Annayev"))

MainWindow.show()
sys.exit(app.exec())
