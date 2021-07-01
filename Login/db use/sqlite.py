import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("""CREATE TABLE users  (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT

    )""")

conn.commit()       #Commits current transaction

conn.close()

