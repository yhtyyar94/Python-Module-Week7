import os
import subprocess

# Klasör yolu (aynı klasör içindeki tüm .ui dosyalarını dönüştürmek için)
folder_path = ("C:\Git\Python_Modul_Week_2\Python_Modul_Week_2\pract-2\Python-Module-Week7\English")  # Buraya klasör yolunu girin

# .ui dosyalarını bul ve dönüştür
for file_name in os.listdir(folder_path):
    if file_name.endswith(".ui"):
        ui_file = os.path.join(folder_path, file_name)
        py_file = os.path.join(folder_path, file_name.replace(".ui", ".py"))
        
        # pyuic6 ile .ui dosyasını .py dosyasına çevir
        command = f"pyuic6 {ui_file} -o {py_file}"  # PyQt5 için pyuic5 kullanın
        subprocess.run(command, shell=True)
        print(f"{file_name} dosyası başarıyla {py_file} dosyasına dönüştürüldü.")
