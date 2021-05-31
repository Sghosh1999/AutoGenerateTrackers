# this is a file to cleare the db, delete a table and then re create the table

import sqlite3
conn = sqlite3.connect('users.db')
# try:
#     conn.execute('''DROP TABLE USERS;''')
# except:
#     pass

conn.execute('''CREATE TABLE USERS
 ( EMAIL   TEXT  PRIMARY KEY    NOT NULL,
 UPDATE_DATE            TEXT     NOT NULL,
 DAY_GAP INT
 
 );''')

conn.close()