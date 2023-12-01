import sqlite3

conn = sqlite3.connect('mydata.db')
sql = "CREATE TABLE plumbing (name TEXT, price TEXT, description TEXT)"
sql = "SELECT * FROM plumbing ORDER BY name"
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()
for r in res:
    print("Название: ", r[0])
    print("Цена: ", r[1])
    print("Описание: ", r[2])

conn.close()