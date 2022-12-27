import sqlite3

conn = sqlite3.connect('info.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user TEXT PRIMARY KEY,
   title TEXT,
   subtitle TEXT,
   img TEXT,
   avatar TEXT);
""")
conn.commit()