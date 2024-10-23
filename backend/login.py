from list_files import list_drive_files
from download_file import download_file
from read_xlsx import read_xlsx
import main


def login(username=main.ui.lineEdit.text(), password=main.ui.lineEdit.text(), login_window=main.ui, admin_window=main.admin_menu, user_window=main.user_menu, get_role=main.get_rol):

    items = list_drive_files()
    file_name = "Kullanicilar.xlsx"
    file_id = None
    for item in items:
        if item["name"] == file_name:
            file_id = item["id"]
            download_file(file_id)
        else:
            return False
    user_info_list = read_xlsx(file_name)

    if len(user_info_list) is not None:
        for user in user_info_list:
            if username == user[0] and password == user[1]:
                if user[2] == 'admin':
                    get_role(user[2])
                    admin_window
                elif user[2] == 'user':
                    get_role(user[2])
                    user_window
            else:
                login_window.error_message.setText(
                    'Invalid username or password!')
                login_window.error_message.show()
