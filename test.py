from backend.list_files import list_drive_files
from backend.download_file import download_file

file_lists = list_drive_files()
for file in file_lists:
    print(f"file : {file["name"]} fileID : {file["id"]}")
# Kullanicilar.xlsx fileID : 1jQmJFlS5y9ydZJFnL_Dt4lJBxBZU9fmX
# Mentor.xlsx fileID: 1VIGenwWW4gBECB5lFwkV2D2k2xTDaL6c
# Mulakatlar.xlsx fileID: 1jg6LcEbdGf-kSijN-YEum6JrasgNaoZi
# Basvurular.xlsx fileID : 1hpTJXh-NLbOyjHV1aTn6-XqzjYRRYdej
# test fileID : 1HwLew8hZNVw6obzBN-0j-7pCXOcL343VkMTH5PO6pV8

download_file("1jQmJFlS5y9ydZJFnL_Dt4lJBxBZU9fmX")
