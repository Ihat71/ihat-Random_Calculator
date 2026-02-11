import sqlite3 as sq
from tabulate import tabulate
conn = sq.connect("training.db")
cursor = conn.cursor()
# conn.execute('''DROP TABLE IF EXISTS product''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    stock INTEGER      
)
''')

cursor.execute('''insert into product (name, price, stock) values ('car', 30000, 5)''')
cursor.execute('''insert into product (name, price, stock) values ('toy', 3, 30)''')
cursor.execute('''insert into product (name, price, stock) values ('tank', 5000000, 1)''')
cursor.execute('''insert into product (name, price, stock) values ('pencil', 0.5, 100)''')
cursor.execute('''insert into product (name, price, stock) values ('water', 1, 50)''')
cursor.execute('''insert into product (name, price, stock) values ('juice', 1, 1)''')
cursor.execute('''insert into product (name, price, stock) values ('biscuit', 300, 30)''')
cursor.execute('''insert into product (name, price, stock) values ('lunch', 10, 50)''')
conn.commit()


#y=cursor.execute('''select name from product where price < 1''')
cursor.execute('''select stock, MAX(price) AS 'Highest price', MIN(price) AS 'lowest price'
                 From product
                 GROUP BY stock
                 ''')
x = cursor.fetchall()
print(tabulate(x, headers=["Stock", "Highest price", "Lowest price"], tablefmt="grid"))



conn.close()