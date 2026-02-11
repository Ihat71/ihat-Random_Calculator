import sqlite3 as sq

'''
1. **Parameterized Queries**: `cursor.execute("...", params)`
2. **Bulk Operations**: `cursor.executemany("...", list_of_params)`
3. **Context Manager**: `with sqlite3.connect('mydatabase.db') as conn:`
4. **Row Factory**: `conn.row_factory = sqlite3.Row`
5. **Retrieve Last Inserted ID**: `cursor.lastrowid`
6. **Count Affected Rows**: `cursor.rowcount`
7. **Metadata Access**: `cursor.description`
'''

'''
Sql does not have double quotes "", only ''
Identifiers can not contain more than 30 chars
Identifiers must starts with an alphabetic character
Commas seperate parameters without a clause
Comments may be enclose with /* and */
-------------------------------------------
For Tables:
Create (creates tables), Alter (Alters tables) and Drop (deletes tables)
-------------------------------------------
For Access:
Grant, Revoke
'''

conn = sq.connect("training.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE       
)
''')
conn.commit()

userdata = [
('Muhammad', 18, 'NoroMuhammad3@gmail.com')
]
cursor.executemany('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?);

''', userdata)
conn.commit()





conn.close()