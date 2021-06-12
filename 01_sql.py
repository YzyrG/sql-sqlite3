import sqlite3

# create a new datebase
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commends
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
					(city TEXT,
					state TEXT,
					population INT
					)
	""") 

# close the datebase connection
conn.close()

