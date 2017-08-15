#!/usr/bin/env python
PKG = 'Controller'
import rospy
import numpy as np
from gulliview_server.msg import Pos
from robotclient.srv import GetCoord
from controller.msg import Vehicle

def callback(pos):
    start_time = rospy.get_time()
    #print "Inside Callback"
    srv1 = 'get_coord0'
    rospy.wait_for_service(srv1)
    angle = 0.0
    x_coord = 0.0
    y_coord = 0.0
    try:
        get_coords1 = rospy.ServiceProxy(srv1, GetCoord)
        f = get_coords1(1)
        tmp_pos1 = f.data.data
        error_count = 0
        while error_count < 10:
            if np.size(tmp_pos1) != 3:
                Gps_x1 = tmp_pos1[0]
                Gps_y1 = tmp_pos1[1]
                error_count = 11
            else:
                error_count += 1
                Gps_x1 = None
                Gps_y1 = None
    except rospy.ServiceException as exc1:
        print("Service1 did not process request: " + str(exc1))

    if (Gps_x1 and Gps_y1) is not None:
        x_coord = Gps_x1
        y_coord = Gps_y1

    if (pos.heading1 != 0):
        angle = 2*np.pi - euler0to360(pos.heading1*(10**-6))

    vehicle = Vehicle()
    vehicle.heading = angle
    vehicle.header.stamp = rospy.get_rostime()
    vehicle.x_meas = x_coord
    vehicle.y_meas = y_coord
    pub = rospy.Publisher("Robot0/config", Vehicle, queue_size=10)
    pub.publish(vehicle)
    print "Heading Angle: " + str(angle)

def euler0to360(angle):

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    else:
        return angle


def listener():
    #print "Feature in listner" + str(fea)
    rospy.init_node('Robot_Node', anonymous=True)
    rospy.Subscriber("position", Pos, callback, queue_size=1)
   # spin() simply keeps python from exiting until this node is stopped
    #print "inside listener"
    # rob0 = message_filters.Subscriber('Robot0/pose', Odometry)
    # rob1 = message_filters.Subscriber('Robot1/pose', Odometry)
    # ts = message_filters.ApproximateTimeSynchronizer([rob0, rob1], 2, 1)
    # ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
