from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx
from PyQt6 import QtWidgets, QtCore


def set_table_data(window, file_name):

    print("\nDriver'daki dosyalar : \n")

    # Google Drive'daki dosyaları listele
    drive_files = list_drive_files()
    print(drive_files)

    file_id = None
    # Dosyaları kontrol et ve aradığımız dosyayı bul
    for file in drive_files:
        print(f"\nFile: {file['name']} File id: {file['id']}")
        if file["name"] == file_name:
            print(f"\n\033[93mAradığınız dosya bulundu: {file['name']}\n")
            file_id = file["id"]
            download_file(file_id)
            print("\nDosya indirildi.\n")
            break

    # Dosya bulunamadıysa işlemi sonlandır
    if not file_id:
        print("\nMaalesef dosya mevcut değil.\n")
        print("İşlem sonlandırılıyor...\n")
        return False

    # Excel dosyasını oku
    file_data = read_xlsx(file_name)
    # Exel dosyasindaki bos hucreleri sil
    clean_file_data = [list(filter(lambda cel: cel is not None, item))
                       for item in file_data]
    print(f"\n\033[95mTemizlenmis dosyamiz :\n\n {clean_file_data}\n")

    # Tabloyu oluşturuyoruz
    window.tableWidget.setRowCount(len(clean_file_data))
    window.tableWidget.setColumnCount(len(clean_file_data[0]))

    # Tabloya başlık ekleme (ilk satırı başlık olarak kullanıyoruz)
    header_labels = clean_file_data[0]
    window.tableWidget.setHorizontalHeaderLabels(header_labels)

    # Tabloya veri ekliyoruz (başlık satırını atlayarak)
    for row, rowData in enumerate(clean_file_data[1:], start=1):
        for column, item in enumerate(rowData):
            table_item = QtWidgets.QTableWidgetItem(str(item))

            # Metin hizalamasını ayarlıyoruz (hücreler için)
            table_item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter)

            window.tableWidget.setItem(row, column, table_item)

    # Tablo başlıklarını hizalıyoruz
    header = window.tableWidget.horizontalHeader()
    header.setDefaultAlignment(
        QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter)

    print("\nTablo başarıyla dolduruldu.\n")
