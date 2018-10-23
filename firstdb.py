import sqlite3
db=sqlite3.connect('C:/Ex/mydb.db')
#db.execute('droptable if exists song')
# يوجد خطأ في السطر اعلاه للبحث فيما بعد
db.execute('create table song(title text,author text,rating int)')
db.commit()
 
