import psycopg2
import psycopg2.extras
import sys
import rospy 

class Config(object):
	def __init__(self, host, dbname, user, password):
		self.host = host
		self.dbname = dbname
		self.user = user
		self.password = password
		self.workMem = 2048

	def dbconfig(self):
		connString = ("host = " + self.host + " dbname = " + self.dbname + " user = " + self.user 
					+ " password = " + self.password)
		print "Connecting to database\n	->%s" % (connString)

		conn = psycopg2.connect(connString)
		cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		cursor.execute('SET workMem TO %s', (self.workMem,))
		cursor.execute('SHOW workMem')
		memory = cursor.fetchone()

		print "Value: ", memory[0]
		print "Row:	", memory

	def dbconfiglite(self):
		connString = ("host = " + self.host + " dbname = " + self.dbname + " user = " + self.user 
					+ " password = " + self.password)
		return connString


