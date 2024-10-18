import sys
from PyQt6 import QtWidgets

from check_assets import check_assets
from login import Ui_MainWindow as Login_Menu


if __name__ == "__main__":
    check_assets()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login_Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
