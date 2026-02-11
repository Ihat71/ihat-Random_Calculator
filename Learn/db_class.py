import sqlite3 as sq
#SQL is not case sensitive
conn = sq.connect("training.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    productID INTEGER PRIMARY KEY AUTOINCREMENT,
    productCode CHAR(3) NOT NULL DEFAULT'',  
    name VARCHAR(30) NOT NULL DEFAULT'',
    quantity INTEGER UNSIGNED NOT NULL DEFAULT 0      
               )
''')
conn.commit()

conn.close()