import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# update
	c.execute("UPDATE population SET population = 9000000 WHERE city='New York'")

	# delete
	c.execute("DELETE FROM population WHERE city='Boston'")
	
	print("\n NEW DATA:\n")

	# c.execute("SELECT * FROM population")

	# rows = c.fetchall()

	# for r in rows:
	# 	print(r[0], r[1], r[2])

	for row in c.execute("SELECT * FROM population") :
		print(row[0], row[1], row[2])




