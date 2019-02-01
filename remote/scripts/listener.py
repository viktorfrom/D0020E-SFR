#!/usr/bin/env python
import rospy
import psycopg2
import psycopg2.extras
import sys
import config
from std_msgs.msg import String

class Listener(object):
    #Class listens to the data coming from Embedded PC and insert the data into a database
    def __init__(self):
        pass

    def callback(self, data):
        conn = psycopg2.connect(config.dbconfiglite)
        cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

        query = "INSERT INTO lidarData (timestamp, lidar) VALUES (" + data.data + ");"
        cursor.execute(query)
        conn.commit()

    def listener(self):
        rospy.init_node('listener', anonymous = True)
        rospy.spin()

if __name__ == '__main__':
    config.dbconfig()
    listener()
