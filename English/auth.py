import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Google API erişimi için gerekli kapsamlar
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authentication():
    creds = None
    print("Başlangıç: credentials.json kontrol ediliyor...")
    
    # Çalışma dizininde credentials.json olup olmadığını kontrol ediyoruz
    credential_path = os.path.join(os.getcwd(), 'credentials.json')

    # Eğer token.json dosyası varsa kimlik bilgilerini yükle
    if os.path.exists('token.json'):
        print("token.json dosyası bulundu, kimlik bilgileri yükleniyor...")
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Kimlik bilgileri geçerli değilse veya yoksa, yeniden doğrulama yap
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Kimlik bilgileri süresi dolmuş, yenileniyor...")
            creds.refresh(Request())
        else:
            if os.path.exists(credential_path):
                print("credentials.json dosyası bulundu, OAuth süreci başlatılıyor...")
                flow = InstalledAppFlow.from_client_secrets_file(credential_path, SCOPES)
                creds = flow.run_local_server(port=0)
            else:
                print(f"credentials.json dosyası bulunamadı: {credential_path}")
                raise FileNotFoundError(f"'credentials.json' bu dizinde bulunamadı: {credential_path}")

        # Kimlik bilgilerini token.json dosyasına kaydediyoruz
        with open('token.json', 'w') as token:
            print("token.json oluşturuluyor ve kaydediliyor...")
            token.write(creds.to_json())

    print("Kimlik doğrulama tamamlandı.")
    return creds
