from PyQt6 import QtWidgets, QtCore

from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def set_table_data(table, file_name):
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
    # filter out empty rows
    headers = [header for header in rows[0] if header is not None]
    table.tableWidget.setColumnCount(len(headers))
    table.tableWidget.setRowCount(len(rows) - 1)

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        table.tableWidget.setHorizontalHeaderItem(i, item)

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
            table.tableWidget.setItem(i - 1, j, item)
