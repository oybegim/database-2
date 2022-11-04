import sqlite3 as sql

malumot1 = sql.connect("Uy.db")

malumot2 = malumot1.cursor()

malumot2.execute(''' 
CREATE TABLE IF NOT EXISTS Xovli(
    joyi TEXT
    sotix INTEGER
)
''')

malumot2.execute(''' 
CREATE TABLE IF NOT EXISTS Dom(
    qavat INTEGER
    padez INTEGER
)
''')