#!/bin/bash
source /opt/ros/kinetic/setup.bash
source ~/TheTitans/robot_ws/devel/setup.bash 
gnome-terminal -e "roscore"
sleep 1
cd $HOME/TheTitans/robot_ws/src/visionlocalization/build/
gnome-terminal -e "./GulliView -f Tag16h5 -d 1"
sleep 1
source ~/TheTitans/robot_ws/devel/setup.bash
gnome-terminal -e "rosrun robotclient get_coord_server.py __name:=get_coord_server0 get_coord:=get_coord0 _ip_of_uwb:=100"
sleep 1
source ~/TheTitans/robot_ws/devel/setup.bash
gnome-terminal -e "rosrun gulliview_server gulliview"
sleep 1
source ~/TheTitans/robot_ws/devel/setup.bash
gnome-terminal -e "rosrun rosaria RosAria __name:=Robot0 _port:=/dev/ttyUSB0" 
#Chat Conversation End

