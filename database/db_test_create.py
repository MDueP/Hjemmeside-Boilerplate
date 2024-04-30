import sqlite3
try:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    #find ud af hvordan man hasher passwords evt bcrypt
    cur.execute("""CREATE TABLE IF NOT EXISTS basic (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        USERNAME TEXT NOT NULL, 
        PASSWORD TEXT NOT NULL);""")
    conn.commit()
except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    conn.close()
