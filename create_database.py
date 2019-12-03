import sqlite3

conn = sqlite3.connect('images/pictures.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pictures_table (name TEXT, data BLOB)
""")

conn.commit()
cursor.close()
conn.close()