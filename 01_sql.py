import sqlite3

# create a new database
conn = sqlite3.connect("new.db")

# create a cursor object used to execute sql statements
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
				(city TEXT,
				state TEXT,
				population INT
				)
	""")

# close the dadabase connection
conn.close()