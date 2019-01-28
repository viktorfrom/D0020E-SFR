#!/bin/bash

bash --rcfile <(echo '. ~/.bashrc; rosrun remote HMI.py')
bash --rcfile <(echo '. ~/.bashrc; rosrun remote listener.py')