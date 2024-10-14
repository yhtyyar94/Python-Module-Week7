import sys
from PyQt6 import QtWidgets
from login import Ui_MainWindow  # login.py dosyasındaki Ui_MainWindow sınıfını içe aktarıyoruz


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
