

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path

# If modifying these scopes, delete the file token.json.

SCOPES = ["https://www.googleapis.com/auth/drive"]  # talebimiz.

# Kimlik dogrulama islemi yapiyor.


def authenticate():
    creds = None  # Ne sunacagiz.Istegimize karsilik kimligimiz.
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):  # Bu bizim gecici kullanimlik zeton.
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

       # bu kode API’ye erişim iznini kaydeder,
       # sonra ki grislerde bu zeton ile sorgusuz giris yapilir.
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds
