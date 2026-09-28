import sqlite3

conn = sqlite3.connect("SalesElectronic/sales_electronics.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales_electronics")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()