import sqlite3
conn=sqlite3.connect('emobilis.db')
print("oppened db successfully")
data=conn.execute("select * from students")
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("AGE=", row[2])
    print("SCHOOL=", row[3],"\n")
conn.close()
