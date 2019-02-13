#!/bin/bash

#NOTICE: IP address of LiDAR, needs to be configured manually
#bash --rcfile <(echo '. ~/.bashrc; roslaunch lms1xx LMS1xx.launch host:=169.254.152.4')
#bash --rcfile <(echo '. ~/.bashrc; rosrun lms1xx LMS1xx_node')
#bash --rcfile <(echo '. ~/.bashrc; rosrun embedded talker.py')


function teardown {
  killall -9 embedded.sh
}

trap teardown EXIT

# Start script 1
nohup roslaunch lms1xx LMS1xx.launch host:=169.254.152.5 > ~/catkin_ws/src/remote/scripts/LMS1xx.launch 2>&1 

# Start script 2
nohup rosrun lms1xx LMS1xx_node > ~/catkin_ws/src/remote/scripts/LMS1xx_node 2>&1

rosrun embedded talker.py