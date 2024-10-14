import io
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from auth import authenticate
from read_xlsx import read_xlsx_from_memory


def export_pdf(real_file_id):
    """Download a Document file in PDF format.
    Args:
        real_file_id : file ID of any workspace document format file
    Returns : IO object with location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = authenticate()

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().export_media(
            fileId=file_id,
            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")

        # Save the file to the disk
        file.seek(0)  # Move to the beginning of the BytesIO object
        with open("crm.xlsx", "wb") as f:
            f.write(file.getvalue())
        print(f"File saved as {"crm.xlsx"}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file.getvalue()


if __name__ == "__main__":
    value = export_pdf(real_file_id="15FRa722m3AzI5t5ss02m_upI6ArAYyLVU1I3g5E-RyY")
    print(read_xlsx_from_memory(value))
