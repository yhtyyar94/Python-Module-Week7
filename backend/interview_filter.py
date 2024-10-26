from backend.download_file import download_file
from backend.list_files import list_drive_files
from backend.read_xlsx import read_xlsx
from PyQt6 import QtWidgets, QtCore


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
    file_data = read_xlsx(file_name)
    # Exel dosyasindaki bos hucreleri sil
    clean_file_data = [
        list(filter(lambda cel: cel is not None, item)) for item in file_data
    ]
    print(clean_file_data)
    if filter_key:
        index = clean_file_data[0].index(filter_key)
        # Filter if a cell is empty
        clean_file_data = [*filter(lambda cell: cell[index] is None, clean_file_data)]

    # Tabloyu oluşturuyoruz
    window.tableWidget.setRowCount(len(clean_file_data) - 1)
    window.tableWidget.setColumnCount(len(clean_file_data[0]))

    # Tabloya başlık ekleme (ilk satırı başlık olarak kullanıyoruz)
    header_labels = clean_file_data[0]
    window.tableWidget.setHorizontalHeaderLabels(header_labels)

    # Tabloya veri ekliyoruz (başlık satırını atlayarak)
    for row, rowData in enumerate(clean_file_data[1:]):
        for column, item in enumerate(rowData):
            table_item = QtWidgets.QTableWidgetItem(str(item))

            # Metin hizalamasını ayarlıyoruz (hücreler için)
            table_item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )

            window.tableWidget.setItem(row, column, table_item)

    # Tablo başlıklarını hizalıyoruz
    header = window.tableWidget.horizontalHeader()
    header.setDefaultAlignment(
        QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
    )
