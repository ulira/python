import sqlite3
conn=sqlite3.connect('emobilis.db')
print("oppened db successfully")

conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (1,'Ulira',18,'emobilis')")
conn.execute("INSERT INTO students(ID,NAME, AGE,SCHOOL) VALUES(2,'KAGOVELI',19,'MACHAKOS')")
conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (3,'steve',18,'zetech')")
conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (4,'kim',18,'jkuat')")
conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (5,'kryss',19,'mit')")
conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (6,'alma',18,'mku')")
conn.execute("INSERT INTO students(ID,NAME,AGE,SCHOOL) VALUES (7,'tamara',18,'mmu')")

conn.commit()
print("records added successfully")
conn.close()