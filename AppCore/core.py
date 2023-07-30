import sqlite3

con = sqlite3.connect("data.sqlite")
cur = con.cursor()

cur.execute("""
    INSERT INTO Boards VALUES
                  (1,"main")
""")

con.commit()

res = cur.execute("SELECT name FROM Boards")
print(res.fetchone())