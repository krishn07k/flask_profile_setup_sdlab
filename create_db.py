import sqlite3

connie=sqlite3.connect('profile.db')
c=connie.cursor()

c.execute("""
CREATE TABLE profile(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Email TEXT,
    Phone TEXT,
    Gender TEXT,
    Dob DATE FORMAT 'dd-mm-yyyy'
)
""")

connie.commit()
connie.close()
