from backend.list_files import list_drive_files
from PyQt6 import QtWidgets, QtCore
from backend.read_xlsx import read_xlsx


def application_page_filter(search=None, filter_key=None, window=None):
    from backend.download_file import download_file


def interview_filter(search=None, filter_key=None, window=None):
    file_name = "Mulakatlar.xlsx"
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
    print(rows)
    headers = [header for header in rows[0] if header is not None]

    # satir ve sutunlari olustur
    window.tableWidget.setColumnCount(len(headers))
    window.tableWidget.setRowCount(len(rows) - 1)

    # sutun basliklarini form`a tek tek yaz`
    for i, header in enumerate(headers):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        window.tableWidget.setHorizontalHeaderItem(i, item)

    # Ilgili sutun`a ilgili veriyi yaz.`
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

# Yapilacaklar :
# yapmam gerekenler sadece istenilen sutun u ve sadece istenilen hucre verisini for loop larda yazdiracagim,
#  boylece filtre olmus olacak ve istedigim veri ve sutun table ` a yansimis olacaktir.`
