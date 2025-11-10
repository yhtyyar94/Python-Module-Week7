from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def fetch_canditate_emails(comboBox, email_set_field=None):
    file_name = "Applications.xlsx"
    drive_files = list_drive_files()
    file_id = None

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

    for row in rows[1:]:
        comboBox.addItem(row[1])
        comboBox.activated.connect(lambda i: email_set_field.setText(rows[i + 1][2]))
