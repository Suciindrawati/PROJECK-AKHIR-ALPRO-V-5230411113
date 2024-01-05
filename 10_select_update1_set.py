# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_fauna = 10
jmlh_skrg_baru = 650

# Menjalankan query UPDATE
cursor.execute(f"UPDATE FAUNA SET jmlh_skrg = {jmlh_skrg_baru} WHERE id_fauna = {id_fauna}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data fauna dengan ID {id_fauna} berhasil diupdate.")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}.")

#mengambil semua data dalam tabel dan tampilkan
cursor.execute("SELECT *FROM fauna")
# Tampilkan dalam bentuk baris
baris_tabel = cursor.fetchall()

#membuat format table dengan method format()
print("Tabel fauna 2023")
print("="*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID fauna", "nama fauna", "jenis", "asal", "jlmh skrg", "thn ditemukan"))
print("-"*80)
#tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris [1], baris[2], baris[3], baris[4], baris[5]))

conn.close()
