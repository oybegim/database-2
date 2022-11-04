import sqlite3 as sql

a = sql.connect("Moshinalar.db")

b = a.cursor()

b.execute(''' 
CREATE TABLE IF NOT EXISTS Tracker(
    dvigateli TEXT
    masofa INTEGER
)
''')

b.execute('''
CREATE TABLE IF NOT EXISTS Lada(
    masofa INTEGER
    labooyna INTEGER
) 
''')