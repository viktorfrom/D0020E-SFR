#!/usr/bin/env python
#This script will listen on the data coming from Embedded PC and insert the data into a database
import rospy
import psycopg2
import psycopg2.extras
import sys
import config
from std_msgs.msg import String

conn = psycopg2.connect(config.dbconfiglite)
cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

def callback(data):
    query = "INSERT INTO lidarData (timestamp, lidar) VALUES (" + data.data + ");"
    cursor.execute(query)
    conn.commit()

def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('laser', String, callback)
    rospy.spin()

if __name__ == '__main__':
    config.dbconfig()
    listener()
