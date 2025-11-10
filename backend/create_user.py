from backend.upload_file import update_file
from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx
from backend.write_xlsx import write_xlsx
from PyQt6.QtWidgets import QMessageBox


def create_user(username, password, role):
    file_name = "Users.xlsx"
    drive_files = list_drive_files()

    for file in drive_files:
        print(f"\nFile: {file['name']} File id: {file['id']}")
        if file["name"] == file_name:
            file_id = file["id"]
            download_file(file_id)
            break

    if not file_id:
        print("\nMaalesef dosya mevcut değil.\n")
        return False

    rows = read_xlsx(file_name)
    rows.append([username, password, role])

    write_xlsx(file_name, rows)
    update_file(file_id, file_name)
    QMessageBox.information(None, "User Created", "User created successfully.")
