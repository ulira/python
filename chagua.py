import sqlite3
conn=sqlite3.connect('ulira.db')
# print("oppened db successfully")
data=conn.execute("select * from friends")
for row in data:
    print("PHONE=", row[0])
    print("NAME=", row[1])
    print("MUSIC=", row[2])
    print("LIKES=", row[3],"\n")
conn.close()