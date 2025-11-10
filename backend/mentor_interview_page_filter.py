from PyQt6 import QtWidgets, QtCore
from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def mentor_interview_page_filter(comboBox, search_text, mentor_interview_window):
    file_name = "Mentors.xlsx"
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

    mentor_interview_window.tableWidget.clear()
    mentor_interview_window.tableWidget.setColumnCount(len(headers))

    if search_text:
        rows = [
            row
            for row in rows
            if search_text.lower() in " ".join([str(cell) for cell in row]).lower()
        ]
    else:
        rows = [row for row in rows if comboBox.currentText() == row[4]]

    mentor_interview_window.tableWidget.setRowCount(len(rows))

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        mentor_interview_window.tableWidget.setHorizontalHeaderItem(i, item)

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
            mentor_interview_window.tableWidget.setItem(i, j, item)
