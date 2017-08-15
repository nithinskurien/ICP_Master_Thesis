#!/usr/bin/env python
PKG = 'ICP'
import rospy
import tf
import numpy as np
import message_filters
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from controller.msg import Vehicle


prev_x = 0.0
prev_y = 0.0
ang_gull = np.array([], dtype=np.float32)
ang_encod = np.array([], dtype=np.float32)
ang_pred = np.array([], dtype=np.float32)
covx = 0.0
covy = 0.0
cov = 0.0
count = 0

def callback(rob0, rob1):

    global ang_gull, ang_encod, ang_pred, prev_x, prev_y, count
    if count!=0:
        Quaternion1 = (rob1.pose.pose.orientation.x, rob1.pose.pose.orientation.y, rob1.pose.pose.orientation.z,
                   rob1.pose.pose.orientation.w)
        euler1 = tf.transformations.euler_from_quaternion(Quaternion1)
        euler2 = float(np.arctan((prev_y - rob0.y1)/(prev_x - rob0.x1)))
        print rob0.heading
        print euler1[2]
        print euler2

        if rob0.heading != 0.0 and euler1[2] != 0.0:
            ang_gull = np.append(ang_gull, rob0.heading)
            ang_encod = np.append(ang_encod, euler1[2])
            ang_pred = np.append(ang_pred, euler2)
            cov_gull = np.cov(ang_gull)
            cov_encod = np.cov(ang_encod)
            cov_pred = np.cov(ang_pred)
        print "_________***__________"
        print "Covariance Gulliview: " + str(cov_gull)
        print "Covariance Encoder: " + str(cov_encod)
        print "Covariance Step: " + str(cov_pred)
    prev_x = rob0.x1
    prev_y = rob0.y1
    count += 1

def listener():
    rospy.init_node('Variance_Calculator', anonymous=True)
    # rospy.Subscriber('Robot0/config', Vehicle, callback, queue_size=100)
    # spin() simply keeps python from exiting until this node is stopped
    print "inside listener"
    rospy.sleep(2)
    rob0 = message_filters.Subscriber('Robot0/config', Vehicle)
    rob1 = message_filters.Subscriber('Robot0/pose', Odometry)
    ts = message_filters.ApproximateTimeSynchronizer([rob0, rob1], 2, 1)
    ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
