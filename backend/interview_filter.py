from PyQt6 import QtWidgets, QtCore
from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def interviews_page_filter_function(project_type, search_text, interviews_window):
    file_name = "Mulakatlar.xlsx"
    drive_files = list_drive_files()

    file_id = None

    for file in drive_files:
        if file["name"] == file_name:
            file_id = file["id"]
            download_file(file_id)
            break

    if not file_id:
        print("\nMaalesef dosya mevcut değil.\n")
        return False

    rows = read_xlsx(file_name)

    headers = [header for header in rows[0] if header is not None]

    interviews_window.tableWidget.clear()
    interviews_window.tableWidget.setColumnCount(len(headers))

    if search_text:
        rows = [
            row
            for row in rows
            if search_text.lower() in " ".join([str(cell) for cell in row]).lower()
        ]
    else:
        # if project_type is "Proje gonderilis tarihi" then row[1] should not be None. if project_type is "Projenin gelis tarihi" then row[2] should not be None.
        rows = [
            row
            for row in rows
            if project_type == "Proje gonderilis tarihi"
            and row[1] is not None
            or project_type == "Projenin gelis tarihi"
            and row[2] is not None
        ]

    interviews_window.tableWidget.setRowCount(len(rows))

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        interviews_window.tableWidget.setHorizontalHeaderItem(i, item)

    for i in range(len(rows)):
        for j in range(len(headers)):
            if rows[i][j] is None:
                continue
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            item.setText(str(rows[i][j]))
            interviews_window.tableWidget.setItem(i, j, item)
