from auth import authentication  # auth.py dosyasından authentication fonksiyonunu çağırıyoruz
from googleapiclient.discovery import build

def main():
    print("Kimlik doğrulama başlatılıyor...")
    creds = authentication()
    print(f"Kimlik doğrulama sonucu: {creds}")

    # Google Drive API istemcisini oluşturuyoruz
    service = build('drive', 'v3', credentials=creds)

    # Google Drive'daki dosyaları listelemek için API çağrısı
    print("Google Drive'daki dosyalar listeleniyor...")
    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('Hiç dosya bulunamadı.')
    else:
        print('Google Drive\'daki dosyalar:')
        for item in items:
            print(f"{item['name']} (ID: {item['id']})")

    print("İşlem tamamlandı.")

# Program doğrudan çalıştırıldığında main() fonksiyonunu çağır
if __name__ == '__main__':
    main()
