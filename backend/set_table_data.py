from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx
import os


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
    rows = read_xlsx(file_name)
    clean_rows = [list(filter(lambda cel: cel is not None, row))
                  for row in rows]
    print(f"\n\033[95mTemizlenmis dosyamiz :\n\n {clean_rows}\n")

    window.
