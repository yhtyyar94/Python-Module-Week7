from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from backend.auth import authenticate


def update_file(
    file_id,
    filename,
    mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
):
    creds = authenticate()

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_metadata = {
            "name": "Werhere CRM Project",
            "mimeType": mimeType,
        }
        media = MediaFileUpload(
            filename,
            mimetype=mimeType,
        )

        # Update the file on Google Drive
        updated_file = (
            service.files().update(fileId=file_id, media_body=media).execute()
        )

        print(f"File ID: {updated_file.get('id')}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return updated_file.get("id")


if __name__ == "__main__":
    update_file(
        "15FRa722m3AzI5t5ss02m_upI6ArAYyLVU1I3g5E-RyY",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
