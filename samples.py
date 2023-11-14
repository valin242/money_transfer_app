# create a database and fill it up with data

import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db') # crates a new database

# Create a cursor
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
            id INTERGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
)
""")

username1, password1 = 'valin242', hashlib.sha256('valinpassword'.encode()).hexdigest()
username2, password2 = 'tesh242', hashlib.sha256('teshpassword'.encode()).hexdigest()
username3, password3 = 'terro242', hashlib.sha256('terropassword'.encode()).hexdigest()
username4, password4 = 'noah242', hashlib.sha256('noahpassword'.encode()).hexdigest()

# Insert data into the database
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()


# Close db connection
cur.close()
conn.close()