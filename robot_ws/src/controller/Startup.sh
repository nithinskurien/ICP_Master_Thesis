#!/bin/bash
#To run everything
MobileSim --nomap -r p3dx:Robot0 & #-r p3dx:Robot1 &
cd ~/Thesis/robot_ws 
source devel/setup.bash
killall -9 roscore
killall -9 rosmaster
roscore &
rosrun rosaria RosAria __name:=Robot0 _port:=localhost:8101 &
#rosrun rosaria RosAria __name:=Robot1 _port:=localhost:8102 &
