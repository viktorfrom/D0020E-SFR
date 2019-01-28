import psycopg2
import psycopg2.extras
import sys
import rospy 

def dbconfig():
	conn_string = "host = 'localhost' dbname = 'testdb' user = 'willow' password = 'willow'"
	print "Connecting to database\n	->%s" % (conn_string)
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
	work_mem = 2048
	cursor.execute('SET work_mem TO %s', (work_mem,))
	cursor.execute('SHOW work_mem')
	memory = cursor.fetchone()
	print "Value: ", memory[0]
	print "Row:	", memory

def dbconfiglite():
    conn_string = "host = 'localhost' dbname = 'testdb' user = 'willow' password = 'willow'"
    return conn_string