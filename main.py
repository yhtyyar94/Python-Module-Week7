from check_assets import check_asset_path_and_fix_size
from set_table_data import set_table_data


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

    role = None

    def get_role(setup):
        global role
        role = setup

    def admin_setup():
        admin_menu.setupUi(MainWindow)
        admin_menu.Basvurular.clicked.connect(applications_setup)
        admin_menu.Mentor.clicked.connect(mentor_setup)
        admin_menu.Basvurular_2.clicked.connect(interviews_menu_setup)
        admin_menu.Adminmenu.clicked.connect(setup_admin_control_menu)
        admin_menu.pushButton.clicked.connect(MainWindow.close)

    def applications_setup():
        applications_menu.setupUi(MainWindow)
        set_table_data(applications_menu, "Basvurular.xlsx")
        applications_menu.pushButton_9.clicked.connect(role)
        applications_menu.pushButton_10.clicked.connect(MainWindow.close)

    def mentor_setup():
        mentor_menu.setupUi(MainWindow)
        set_table_data(mentor_menu, "Mentor.xlsx")
        mentor_menu.pushButton_5.clicked.connect(role)
        mentor_menu.pushButton_4.clicked.connect(MainWindow.close)

    def interviews_menu_setup():
        interviews_menu.setupUi(MainWindow)
        set_table_data(interviews_menu, "Mulakatlar.xlsx")
        interviews_menu.pushButton_tercih.clicked.connect(role)
        interviews_menu.pushButton_exit.clicked.connect(MainWindow.close)

    def user_setup():
        user_menu.setupUi(MainWindow)
        user_menu.basvurular.clicked.connect(applications_setup)
        user_menu.mentor_gorusmesi.clicked.connect(mentor_setup)
        user_menu.mulakatlar.clicked.connect(interviews_menu_setup)
        user_menu.cikis.clicked.connect(MainWindow.close)

    def setup_admin_control_menu():
        admin_control_menu.setupUi(MainWindow)
        admin_control_menu.tercihler.clicked.connect(role)
        admin_control_menu.cikis.clicked.connect(MainWindow.close)

    ui.pushButton.clicked.connect(
        lambda: login(
            ui.lineEdit.text(),
            ui.lineEdit_2.text(),
            ui,
            admin_setup,
            user_setup,
            get_role,
        )
    )
    ui.pushButton_2.clicked.connect(MainWindow.close)

    MainWindow.show()
    sys.exit(app.exec())
