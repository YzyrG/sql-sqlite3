import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# update
	c.execute("UPDATE inventory SET model = 'ff01' WHERE Quanlity = 'best'")

	for row in c.execute("SELECT * FROM inventory"):
		print(row[0], row[1], row[2])

		