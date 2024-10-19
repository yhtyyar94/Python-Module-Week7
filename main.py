from check_assets import check_asset_path_and_fix_size


if __name__ == "__main__":
    check_asset_path_and_fix_size()
    import sys
    from PyQt6 import QtWidgets
    from login_ui import Ui_MainWindow as LoginUI
    from admin_menu_ui import Ui_MainWindow as AdminUI
    from application_menu_ui import Ui_MainWindow as ApplicationsUI
    from mentor_menu_ui import Ui_MainWindow as MentorUI
    from interviews_menu_ui import Ui_MainWindow as InterviewsUI

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUI()
    ui.setupUi(MainWindow)
    admin_menu = AdminUI()
    applications_menu = ApplicationsUI()
    mentor_menu = MentorUI()
    interviews_menu = InterviewsUI()

    def admin_setup():
        admin_menu.setupUi(MainWindow)
        admin_menu.Basvurular.clicked.connect(lambda: applications_setup())

        admin_menu.Mentor.clicked.connect(lambda: mentor_setup())
        admin_menu.Basvurular_2.clicked.connect(lambda: interviews_menu_setup())
        admin_menu.pushButton.clicked.connect(MainWindow.close)

    def applications_setup():
        applications_menu.setupUi(MainWindow)
        applications_menu.pushButton_9.clicked.connect(admin_setup)
        applications_menu.pushButton_10.clicked.connect(MainWindow.close)

    def mentor_setup():
        mentor_menu.setupUi(MainWindow)
        mentor_menu.pushButton_5.clicked.connect(admin_setup)
        mentor_menu.pushButton_4.clicked.connect(MainWindow.close)

    def interviews_menu_setup():
        interviews_menu.setupUi(MainWindow)
        interviews_menu.pushButton_tercih.clicked.connect(admin_setup)
        interviews_menu.pushButton_exit.clicked.connect(MainWindow.close)

    ui.pushButton.clicked.connect(admin_setup)

    MainWindow.show()
    sys.exit(app.exec())
