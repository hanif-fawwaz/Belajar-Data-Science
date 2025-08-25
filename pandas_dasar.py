import pandas as pd

'''
- Pandas: Library untuk mengolah data (bentuk tabel, mirip Exel)
- Struktur utama:
 - Series (seperti 1 kolom)
 - DataFrame (seperti tabel Exel)
'''
# Contoh kode pandas
# Membuat DataFrame
data = {
    "Nama": ["Hanif", "Arib", "Fawwaz"],
    "Umur": [21, 18, 19],
    "Kota": ["Brebes", "Tegal", "Bandung"]
}

df = pd.DataFrame(data)
print("DataFrame:", df)

# Akses kolom
print("Kolom Umur:\n", df["Umur"])

# Info data
print("\nInfo:")
print(df.info())

print("\nDeskripsi Statistik:")
print(df.describe())

# Filter umur umur < 20
print("\nUmur < 20:\n", df[df["Umur"] < 20])