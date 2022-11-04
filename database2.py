import sqlite3 as sql

a = sql.connect("Maktablar.db")

b = a.cursor()

b.execute(''' 
CREATE TABLE IF NOT EXISTS Maktab6(
    qavati INTEGER
    maydoni INTEGER
)
''')

b.execute('''
CREATE TABLE IF NOT EXISTS Maktab13(
    maydoni INTEGER
    qavati INTEGER
) 
''')