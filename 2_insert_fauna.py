import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
#insert data ke tabel

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Harimau jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Kuskus beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Beruang madu', 'Mamalia', 'Sumatera', '1000', '2020')
                ''')  
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Pesut mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
                ''') 
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Burung maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Macan Dahan', 'Mamalia', 'Sumatra', '400', '2020')
                ''')  
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Kancil', 'Mamalia', 'jawa', '60', '2022')
                ''')  
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')  
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Elang Jawa', 'Burung', 'Jawa', '200', '2021')
                ''')   
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jmlh_skrg,   thn_ditemukan)
                VALUES('Katak Barneo', 'Amfibi', 'Kalimantan', '2000', '2023')
                ''')                                                                                                          
koneksi.commit()
koneksi.close() 