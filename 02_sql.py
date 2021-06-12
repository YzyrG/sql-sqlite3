import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
	# insert data
	cursor.execute("INSERT INTO population VALUES('New York',\
		'NY', 8400000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco',\
		'CA', 800000)")

	conn.commit()
except sqlite3.OperationalError:
	print("Oops! Something went wrong. Try again... ")


conn.close()

# use with statement

# with sqlite3.connect("new.db") as connection:
# 	c = connection.cursor()
# 	cursor.execute("INSERT INTO population VALUES('New York',\
#  	'NY', 8400000)")
#  	cursor.execute("INSERT INTO population VALUES('San Francisco',\
#  	'CA', 800000)")