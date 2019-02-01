#!/usr/bin/env python
import rospy
import psycopg2
import psycopg2.extras
import sys
import time
import config
from std_msgs.msg import String
from datetime import datetime
from datetime import timedelta

class Replay(object):
    def __init__(self):
        self.lastTime = datetime(2018, 2, 16, 13, 25, 28, 688503)
        self.seconds = 100





    def talker(self):
        conn = psycopg2.connect(config.dbconfiglite())
        cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        
        lastTime = datetime(2018, 2, 16, 13, 25, 28, 688503)
        interval = timedelta(seconds = 100)

        pub = rospy.Publisher('replay', String, queue_size = 10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(5) # 100hz

        query = ('SELECT timestamp' 
                'FROM lidarData' 
                'WHERE timestamp >= ' + str(lastTime) + 'AND timestamp <' + str(lastTime + interval) + ';')
        cursor.execute(query)
        timeArr = cursor.fetchall()

        print(timeArr)
        print(query)
        print(len(timeArr))

        query = ('SELECT timestamp'
                'FROM lidarData' 
                'WHERE timestamp >= ' + str(lastTime) + 'AND timestamp <' + str(lastTime + interval) + ';')
        cursor.execute(query)
        lidarData = cursor.fetchall()[0][0]

        i = 0

        while i < len(timeArr):
            messageStr = "[" + str(lidarData[0])

            for j in range(1, len(lidarData)):
            messageStr += "," + str(lidarData[j])

            messageStr += "]"
            print(messageStr)
            pub.publish(messageStr)
            rate.sleep()
        i += 1

if __name__ == '__main__':
    config.dbconfig()
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
