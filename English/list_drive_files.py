from auth import authentication  # auth.py dosyasından kimlik doğrulama fonksiyonunu kullanıyoruz
from googleapiclient.discovery import build

def list_drive_files():
    print("Kimlik doğrulama başlatılıyor...")
    creds = authentication()
    print(f"Kimlik doğrulama sonucu: {creds}")

    # Google Drive API istemcisini oluşturuyoruz
    service = build('drive', 'v3', credentials=creds)

    # Google Drive'daki dosyaları listelemek için API çağrısı
    print("Google Drive'daki dosyalar listeleniyor...")
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('Hiç dosya bulunamadı.')
    else:
        print('Google Drive\'daki dosyalar:')
        for item in items:
            print(f"Dosya Adı: {item['name']} (ID: {item['id']})")

    print("İşlem tamamlandı.")

if __name__ == '__main__':
    list_drive_files()