import sqlite3

with sqlite3.connect("new_num.db") as connection:
	c = connection.cursor()
	# user's inout
	prompt = ("""Please enter one of (AVG,MAX,MIN,SUM), you will get relevate result of 100 random int numbers.
or enter 'q' to quit this programming.\n""")
	
	# output
	sql = {
		'avg': "SELECT avg(number) FROM numbers",
		'max': "SELECT max(number) FROM numbers",
		'min': "SELECT min(number) FROM numbers",
		'sum': "SELECT sum(number) FROM numbers"
	}

	while True:
		agg = input(prompt)
		if agg == 'q':
			break
		elif agg.lower() in sql.keys():
			c.execute(sql[agg.lower()])
			result = c.fetchone()
			print(agg, ":", result[0],"\n")
		else:
			print("opps! you enter wrong commend. Try again.\n")
			continue




