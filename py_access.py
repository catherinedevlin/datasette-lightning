import sqlite3

with sqlite3.connect('shakespeare.db') as con:
    curs = con.cursor()
    curs.execute('SELECT title, year FROM work') 
    print(curs.fetchall())
