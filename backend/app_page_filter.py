from PyQt6 import QtWidgets, QtCore
from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx


def app_page_filter(search_text, page_window, but_value):
    file_name = "Basvurular.xlsx"
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
    page_window.tableWidget.setColumnCount(
        len(headers))  # bu satir neden lazim ?
    page_window.tableWidget.clear()

    def is_dublicate(but_value, rows):
        duplicates = []
        seen = set()
        unique_rows = []

        for row in rows[1:]:  # Başlık satırını atlayarak döngüye başla
            name = row[1]
            postal_code = row[4]

            if (name, postal_code) in seen:
                # Mükerrer olanları 'duplicates' listesine ekle
                duplicates.append(row)
            else:
                seen.add((name, postal_code))
                # Benzersiz olanları 'unique_rows' listesine ekle
                unique_rows.append(row)

        if but_value == "DUPLICATE":
            return duplicates
        elif but_value == "UNDUPLICATE":
            return unique_rows

    if search_text:
        rows = [
            row
            for row in rows
            if search_text.lower() in " ".join([str(cell) for cell in row]).lower()
        ]
        # "ATANDI" durumu
    elif (but_value) == "OK":

        rows = [row for row in rows if row[14] == "OK"]
        print("Assigned seçeneği seçildi..\n")
        # "ATANMADI" durumu
    elif but_value == "ATANMADI":
        rows = [row for row in rows if row[14] == "ATANMADI"]
        print("Unassigned seçeneği seçildi..\n")

    elif but_value in ["VIT4", "VIT3", "VIT2", "VIT1"]:

        rows = [row for row in rows if row[15] == but_value]

    elif but_value == "DUPLICATE":

        rows = is_dublicate(but_value, rows)
    elif but_value == "UNDUPLICATE":
        rows = is_dublicate(but_value, rows)

    page_window.tableWidget.setRowCount(len(rows))

    # QT ye tablolarda satir ve sutunlara veriyi yazdirma
    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        page_window.tableWidget.setHorizontalHeaderItem(i, item)

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
            page_window.tableWidget.setItem(i, j, item)
