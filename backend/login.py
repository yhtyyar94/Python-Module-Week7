from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx


def login(username, password, login_window, admin_window, user_window, get_role):

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

    if len(user_info_list) != 0:
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
