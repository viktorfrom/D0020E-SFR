#!/bin/bash

#IP address of LiDAR, needs to be configured manually
IPADDR = '127.168.0.1'
bash --rcfile <(echo '. ~/.bashrc; roslaunch lms1xx LMS1xx.launch host:=$IPADDR')
bash --rcfile <(echo '. ~/.bashrc; rosrun lms1xx LMS1xx_node')
bash --rcfile <(echo '. ~/.bashrc; rosrun embedded talker.py')