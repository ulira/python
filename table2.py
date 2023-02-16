import sqlite3
conn=sqlite3.connect('ulira.db')
conn.execute("CREATE TABLE friends "
             "(PHONE INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "MUSIC TEXT NOT NULL,"
             "LIKES  TEXT NOT NULL)")
print("Table created successfully")
conn.close()