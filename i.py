import sqlite3

# Buat koneksi ke database
conn = sqlite3.connect('database/fitness.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data_olahraga (
                    nomor INTEGER PRIMARY KEY,
                    hari TEXT,
                    nama TEXT,
                    total_kalori INTEGER,
                    lama_latihan INTEGER,
                    olahraga_terakhir TEXT
                  )''')



# Commit perubahan
conn.commit()

# Tutup koneksi
conn.close()
