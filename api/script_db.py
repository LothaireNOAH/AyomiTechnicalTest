import sqlite3
conn = sqlite3.connect('expressions.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS expressions (
                    id INTEGER PRIMARY KEY,
                    expression TEXT,
                    result REAL
                  )''')

conn.close()
