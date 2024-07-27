import sqlite3

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('example.db')

# Membuat cursor
cur = conn.cursor()

# Menjalankan query SQL untuk membuat tabel
cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Menambahkan data
cur.execute("INSERT INTO users (name) VALUES (?)", ('John Doe',))

# Mengambil data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()
