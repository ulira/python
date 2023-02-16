import sqlite3
conn=sqlite3.connect('ulira.db')

conn.execute("INSERT INTO friends(PHONE,NAME,MUSIC,LIKES ) VALUES (08,'Ulira','EMO','music')")
conn.execute("INSERT INTO friends(PHONE,NAME,MUSIC,LIKES ) VALUES(09,'KAGOVELI','TRAP','friends')")
conn.execute("INSERT INTO friends(PHONE,NAME,MUSIC,LIKES ) VALUES (07,'steve','drills','rap')")
conn.execute("INSERT INTO friends(PHONE,NAME,MUSIC,LIKES) VALUES (06,'kim','TRAP','food')")

conn.commit()
print("records added successfully")
conn.close()