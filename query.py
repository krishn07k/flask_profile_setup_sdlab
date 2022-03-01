import sqlite3

connie=sqlite3.connect('profile.db')
c=connie.cursor()

c.execute("""
SELECT * FROM profile
""")
data=c.fetchall()

for i in data:
    print(i)
connie.commit()
connie.close()
