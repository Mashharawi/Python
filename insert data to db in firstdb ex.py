import sqlite3
db=sqlite3.connect('C:/Ex/mydb.db')
db.execute('insert into song (title, author, rating) values ("The map of reality", "The New Smiths",9)')
db.commit()
