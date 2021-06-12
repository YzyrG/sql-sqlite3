import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("DELETE  FROM inventory WHERE Quanlity = 'low'")

	rows = c.execute("SELECT * FROM inventory WHERE Make = 'Fords'")

	for r in rows:
		print(r[0], r[1], r[2])
