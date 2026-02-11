import sqlite3

conn = sqlite3.connect('practice_data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER)''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Tom', 9)")
conn.commit()