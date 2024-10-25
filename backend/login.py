from backend.list_files import list_drive_files
from backend.download_file import download_file
from backend.read_xlsx import read_xlsx


def login(username, password, login_window, admin_window, user_window, get_role):
    # Google Drive'daki dosyaları listele
    drive_files = list_drive_files()

    # Aranacak dosya adı
    file_name = "Kullanicilar.xlsx"
    file_id = None

    # Dosyaları kontrol et ve aradığımız dosyayı bul
    for file in drive_files:
        if file["name"] == file_name:
            file_id = file["id"]
            download_file(file_id)
            break

    # Dosya bulunamadıysa işlemi sonlandır
    if not file_id:
        login_window.error_message.setText("Something went wrong!")
        return False

    # Excel dosyasını oku
    user_data_list = read_xlsx(file_name)

    # Kullanıcı bilgileri varsa kontrol et
    if len(user_data_list) != 0:
        for user in user_data_list:
            if username == user[0] and password == user[1]:
                print(f"Kullanıcı bulundu: {username}")
                if user[2] == "admin":
                    get_role(user[2])
                    admin_window()

                elif user[2] == "user":
                    get_role(user[2])
                    user_window()

                return True  # Giriş başarılı, işlemi sonlandır
            else:

                login_window.error_message.setText("Invalid username or password!")

    else:
        print("Hiçbir kullanıcı bulunamadı.")
        login_window.error_message.setText("No users found!")

    return False  # Giriş başarısız
