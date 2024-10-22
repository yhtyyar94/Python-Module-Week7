from backend.auth import authenticate
from googleapiclient.discovery import build


def list_drive_files():
    print("Kimlik doğrulama başlatiliyor...")
    creds = authenticate()
    print(f"Kimlik doğrulama sonucu: {creds}")  # sonucu burada yazdırıyoruz.

    # Google Drive API client oluşturuyoruz
    # Burada google'a ne istediğimizi gönderiyoruz.
    service = build("drive", "v3", credentials=creds)
    # Google Drive'daki dosyaları listelemek için API çağrısı
    print("Google Drive'daki dosyalar listeleniyor...")

    results = (
        service.files()
        .list(
            pageSize=10,
            fields="nextPageToken, files(id, name)",
        )
        .execute()
    )
    items = results.get("files", [])

    if not items:
        print("Hicbir dosya bulunamadi")
        return []
    else:

        # Bu alanda da google'ın gönderdiği dosya listesini ekrana yazdırıyoruz.
        print('Google Drive\'daki dosyalar:')
        for item in items:
            print(f"Dosya Adı: {item['name']} (ID: {item['id']})")

        print("İşlem tamamlandı.")
