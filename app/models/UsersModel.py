import sqlite3
conn = sqlite3.connect('wheatland.db')

class UsersModel:
	# Lookup the next available ID in the DB
	def getNextID(self):
		return 0
