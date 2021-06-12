import sqlite3
import random

with sqlite3.connect("new_num.db") as connection:
	# create a cursor object used to execute sql statements
	c = connection.cursor()
	# create a new table
	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers( number INT)")
	# create a number list
	num_list = [(random.randint(0,100),) for x in range(100)]
	# insert numbers to table numbers
	c.executemany("INSERT INTO numbers VALUES(?)", num_list)






