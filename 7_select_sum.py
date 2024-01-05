import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(jmlh_skrg) FROM FAUNA")
total_populasi = cursor.fetchone()[0]

print(f"Total populasi hewan langka : {total_populasi}")

# Menutup koneksi
conn.close()
