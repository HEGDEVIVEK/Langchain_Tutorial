import sqlite3

conn = sqlite3.connect("SalesElectronic/sales_electronics.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_electronics (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        quantity INTEGER,
        price REAL
    )
""")

cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Laptop", 10, 1000))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Mouse", 100, 10))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Keyboard", 50, 20))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Monitor", 20, 300))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Webcam", 30, 50))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Headphone", 40, 100))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Phone", 10, 5000))
cursor.execute("INSERT INTO sales_electronics (product_name, quantity, price) VALUES (?, ?, ?)", ("Tablet", 20, 2000))

conn.commit()
conn.close()