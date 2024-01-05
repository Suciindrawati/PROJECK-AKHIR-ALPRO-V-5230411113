import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan LIKE
nama = 'H%'  # Mencari nama yang dimulai dengan 'John'
kursor.execute(f"SELECT * FROM FAUNA WHERE nama_fauna LIKE ?", (nama ,))
baris_table = kursor.fetchall()

print("Tabel Fauna:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10}  {:<10}".format("ID fauna", "nama fauna", "jenis", "asal", "jmlh skrg", "thn ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<10}  {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()