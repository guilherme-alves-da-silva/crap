import sqlite3
import sys
import os
"""
#for row in sqlite3.connect(sys.argv[1]).cursor().execute('SELECT * FROM '+sys.argv[2]):
for row in sqlite3.connect(sys.argv[1]).cursor().execute(sys.argv[2]):
	print(*row, sep = '\t')
	#print('{}|{}'.format(*row))
"""
if len(sys.argv) != 3:
	print("\n--- please enter 2 arguments for", sys.argv[0], "---")
	print("\nargv 1: database file.\nargv 2: sql command or file with sql commands.\n")

else:
	conn = sqlite3.connect(sys.argv[1])
	cursor = conn.cursor()

	if os.path.isfile(sys.argv[2]): #check if sys.argv[2] is a file
		f = open(sys.argv[2], "r")
		fileContents = f.read()

		if fileContents.split(' ', 1)[0].lower() == 'select':
			for row in cursor.execute(fileContents):
				print(*row, sep = '\t')

		else: cursor.executescript(fileContents)

	elif sys.argv[2].split(' ', 1)[0].lower() == 'select' or sys.argv[2].split(' ', 1)[0].lower() == 'pragma':
		for row in cursor.execute(sys.argv[2]):
			print(*row, sep = '\t')

	elif sys.argv[2] == 'e': #only for backward compatibility
		script = os.environ[sys.argv[2]]

		if script.split(' ', 1)[0].lower() == 'select':
			for row in cursor.execute(script):
				print(*row, sep = '\t')

		else: cursor.executescript(script)

	else: cursor.executescript(sys.argv[2])

	#cursor.executescript(open(sys.argv[2], "r").read()) #this with the conn and cursor can run commands from a file
	conn.commit()
