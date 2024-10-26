from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx
from PyQt6 import QtWidgets, QtCore


def set_table_data(window, file_name):
    # Google Drive'daki dosyaları listele
    drive_files = list_drive_files()

    file_id = None
    # Dosyaları kontrol et ve aradığımız dosyayı bul
    for file in drive_files:
        print(f"\nFile: {file['name']} File id: {file['id']}")
        if file["name"] == file_name:
            file_id = file["id"]
            download_file(file_id)
            break

    # Dosya bulunamadıysa işlemi sonlandır
    if not file_id:
        print("\nMaalesef dosya mevcut değil.\n")
        return False

    # Excel dosyasını oku
    rows = read_xlsx(file_name)
    headers = [header for header in rows[0] if header is not None]
    window.tableWidget.setColumnCount(len(headers))
    window.tableWidget.setRowCount(len(rows) - 1)

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        window.tableWidget.setHorizontalHeaderItem(i, item)

    for i in range(1, len(rows)):
        for j in range(len(headers)):
            if rows[i][j] is None:
                continue
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            item.setText(str(rows[i][j]))
            window.tableWidget.setItem(i - 1, j, item)
