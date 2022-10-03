import sqlite3

conn = sqlite3.connect('signin_database.db')
print("Opened database successfully")

#conn.execute('CREATE TABLE signup (Name TEXT,email  TEXT,password  TEXT,retype password  TEXT)')
conn.execute('CREATE TABLE signin email  TEXT,password  TEXT)')
print("Table created successfully")
conn.close()