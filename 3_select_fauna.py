import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
#select all data pegawai

kursor = koneksi.cursor()
#mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA")
# Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

#membuat format table dengan method format()
print("Tabel fauna 2023")
print("="*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID fauna", "nama fauna", "jenis", "asal", "jlmh skrg", "thn ditemukan"))
print("-"*80)
#tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris [1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()