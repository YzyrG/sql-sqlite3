import sqlite3

# create a new datebase
conn =  sqlite3.connect("cars.db")

# create a cursor object used to execute sql statement
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
				(
					Make TEXT,
					Model TEXT,
					Quanlity TEXT
				)
	""")

# close the datebase connection
conn.close()


