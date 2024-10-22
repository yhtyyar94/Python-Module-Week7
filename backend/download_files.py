import os
import io
from auth import authenticate
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError


def download_file(file_id, file_name):
    try:
        # Kimlik doğrulama işlemi
        creds = authenticate()
        service = build("drive", "v3", credentials=creds)

        # Dosya indirme isteği
        request = service.files().get_media(fileId=file_id)
        file_io = io.BytesIO()
        downloader = MediaIoBaseDownload(file_io, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}% complete.")

        # Downloads dizinine dosya kaydetme
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(downloads_dir, file_name)

        # İndirilen dosyayı yazma
        with open(file_path, "wb") as f:
            f.write(file_io.getvalue())

        print(f"File successfully downloaded to: {file_path}")
        return file_path

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == "__main__":
    file_id = '15qVZnE4z1bJoRK1ThqL5bSm59_OY5D5v'
    file_name = "Mentor.xlsx"
    download_file(file_id, file_name)
