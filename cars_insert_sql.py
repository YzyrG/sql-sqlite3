import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	insert_list = [
		('Fords', 'f001', 'best'),
		('Fords', 'f002', 'middle'),
		('Fords', 'f003', 'low'),
		('Hondas', 'h001', 'best'),
		('Hondas', 'h002', 'best'),
	]

	c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", insert_list)
