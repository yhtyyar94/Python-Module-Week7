from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx


def login(username, password, login_window, admin_window, user_window, get_role):
    print(f"Username: {username}, Password: {password}")
    print("\nLogin fonksiyonu çalıştı.")
    print("\nDriver'daki dosyalar : \n")

    # Google Drive'daki dosyaları listele
    drive_files = list_drive_files()
    print(drive_files)

    # Aranacak dosya adı
    file_name = "Kullanicilar.xlsx"
    file_id = None

    # Dosyaları kontrol et ve aradığımız dosyayı bul
    for file in drive_files:
        print(f"\nChecking file: {file['name']} id: {file['id']}")
        if file["name"] == file_name:
            print(f"\nAradığınız dosya bulundu: {file['name']}\n")
            file_id = file["id"]
            download_file(file_id)
            print("\nDosya indirildi.\n")
            print(f"\nDosya ID : {file_id}\n\n")
            break

    # Dosya bulunamadıysa işlemi sonlandır
    if not file_id:
        print("\nMaalesef dosya mevcut değil.\n")
        print("İşlem sonlandırılıyor...\n")
        return False

    # Excel dosyasını oku
    user_data_list = read_xlsx(file_name)
    print(f"Kullanıcı listesi: {user_data_list}")

    # Kullanıcı bilgileri varsa kontrol et
    if len(user_data_list) != 0:
        for user in user_data_list:
            print(f"Kullanıcı kontrol ediliyor: {user[0]}")
            if username == user[0] and password == user[1]:
                print(f"Kullanıcı bulundu: {username}")
                if user[2] == 'admin':
                    get_role(user[2])
                    admin_window()
                    print("\nAdmin penceresi çalıştırıldı.")
                elif user[2] == 'user':
                    get_role(user[2])
                    user_window()
                    print("\nUser penceresi çalıştırıldı.")
                return True  # Giriş başarılı, işlemi sonlandır
            else:
                print("Geçersiz kullanıcı adı veya şifre!")
                login_window.error_message.setText(
                    'Invalid username or password!')
                login_window.error_message.show()
    else:
        print("Hiçbir kullanıcı bulunamadı.")
        login_window.error_message.setText('No users found!')
        login_window.error_message.show()

    return False  # Giriş başarısız
