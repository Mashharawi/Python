import sqlite3
db=sqlite3.connect('C:/Ex/mydb.db')
data = db.execute('select * from song')
for row in data:
    print(row)
