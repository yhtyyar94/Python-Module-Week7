from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def login(username, password, login_window, admin_window, user_window, get_role):
    file_name = "Kullanicilar.xlsx"
    drive_files = list_drive_files()

    if len(drive_files) == 0:
        print("No files found.")
        return False
    elif file_name not in [file["name"] for file in drive_files]:
        print("No such file found.")
        return False
    else:
        file_id = [file["id"] for file in drive_files if file["name"] == file_name][0]
        download_file(file_id)

    rows = read_xlsx(file_name)

    global user
    user = False
    print(rows)
    print(username, password)

    for row in rows:
        if (row[0] == username and row[1] != password) or (
            row[0] != username and row[1] == password
        ):
            login_window.error_message.setText("Invalid username or password.")
            return False
        elif row[0] == username and row[1] == password:
            if row[2] == "admin":
                user = True
                get_role(admin_window)
                admin_window()
            elif row[2] == "user":
                get_role(user_window)
                user = True
                user_window()
