
import csv

def write_csv(file_name, rows):
    try:
        # CSV dosyasını yazma modunda aç
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Satırları yaz
            writer.writerows(rows)
        
        print("Veriler başarıyla kaydedildi.")
    
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Örnek kullanım
if __name__ == "__main__":
    rows = [
        ["Başlık 1", "Başlık 2", "Başlık 3"],
        ["Veri 1", "Veri 2", "Veri 3"],
        ["Veri 4", "Veri 5", "Veri 6"]
    ]
    
    write_csv("test.csv", rows)
