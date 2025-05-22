import sqlite3

con = sqlite3.connect("gsm_data.db")
con.execute("CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, STATE TEXT)")
con.commit
con.close