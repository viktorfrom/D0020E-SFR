#!/bin/bash

#bash --rcfile <(echo '. ~/.bashrc; roscore')
#bash --rcfile <(echo '. ~/.bashrc; rosrun remote HMI.py')
#bash --rcfile <(echo '. ~/.bashrc; rosrun remote listener.py')

function teardown {
  killall -9 remote.sh
}

trap teardown EXIT

# Start script 1
nohup roscore > ~/catkin_ws/src/remote/scripts/roscore 2>&1 

# Start script 2
nohup rosrun remote listener.py > ~/catkin_ws/src/remote/scripts/listener.py 2>&1 

rosrun remote HMI.py