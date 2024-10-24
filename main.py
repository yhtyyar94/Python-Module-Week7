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
    from user_menu_ui import Ui_MainWindow as UserUI
    from admin_control_menu_ui import Ui_MainWindow as AdminControlUI
    from backend.login import login

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUI()
    ui.setupUi(MainWindow)
    admin_menu = AdminUI()
    applications_menu = ApplicationsUI()
    mentor_menu = MentorUI()
    interviews_menu = InterviewsUI()
    user_menu = UserUI()
    admin_control_menu = AdminControlUI()

    role = ""

    def get_rol(user_role):
        global role
        role = user_role

    def admin_setup():
        admin_menu.setupUi(MainWindow)
        admin_menu.applications_Button.clicked.connect(applications_setup)
        admin_menu.Mentor_interview_Button.clicked.connect(mentor_setup)
        admin_menu.interviews_Button.clicked.connect(interviews_menu_setup)
        admin_menu.Admin_menu_Button.clicked.connect(setup_admin_control_menu)
        admin_menu.exit_Button.clicked.connect(MainWindow.close)

    def applications_setup():
        applications_menu.setupUi(MainWindow)
        applications_menu.main_menu.clicked.connect(admin_setup)
        applications_menu.exit.clicked.connect(MainWindow.close)

    def mentor_setup():
        mentor_menu.setupUi(MainWindow)
        mentor_menu.main_menu.clicked.connect(admin_setup)
        mentor_menu.exit_button.clicked.connect(MainWindow.close)

    def interviews_menu_setup():
        interviews_menu.setupUi(MainWindow)
        interviews_menu.mainmenu_Button.clicked.connect(admin_setup)
        interviews_menu.exit_Button.clicked.connect(MainWindow.close)

    def user_setup():
        user_menu.setupUi(MainWindow)
        user_menu.app_Button.clicked.connect(applications_setup)
        user_menu.mentor_interview_Button.clicked.connect(mentor_setup)
        user_menu.interviews_Button.clicked.connect(interviews_menu_setup)
        user_menu.exit_Button.clicked.connect(MainWindow.close)

    def setup_admin_control_menu():
        admin_control_menu.setupUi(MainWindow)
        admin_control_menu.send_email.clicked.connect(admin_setup)
        admin_control_menu.exit.clicked.connect(MainWindow.close)

    ui.pushButton_2.clicked.connect(MainWindow.close)
    ui.pushButton.clicked.connect(lambda: print("Button clicked!"))
    ui.pushButton.clicked.connect(lambda: login(
        ui.lineEdit.text(), ui.lineEdit_2.text(), ui, admin_setup, user_setup, get_rol))
    ui.error_message.hide()

    MainWindow.show()
    sys.exit(app.exec())
