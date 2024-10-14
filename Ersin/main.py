import sys
from PyQt6 import QtWidgets
from login import Ui_MainWindow  # login.py dosyasındaki sınıfı içe aktarıyoruz

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
