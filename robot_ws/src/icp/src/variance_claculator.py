#!/usr/bin/env python
PKG = 'ICP'
import rospy
import numpy as np
from gulliview_server.msg import Pos
from robotclient.srv import GetCoord
import MeasurementMixer as me
import algorithm
import Distribution
import DataCollect
import matplotlib.pyplot as plt
import Kalman

xarr = np.array([], dtype=np.float32)
yarr = np.array([], dtype=np.float32)
covx = 0.0
covy = 0.0
cov = 0.0

def callback(pos):

    global xarr, yarr
    if pos.x1 & pos.y1 != 0:
        xarr = np.append(xarr, pos.x1)
        yarr = np.append(yarr, pos.y1)
        xmean = np.mean(xarr)
        ymean = np.mean(yarr)
        cov = np.cov(xarr, yarr)
        covx = np.cov(xarr)
        covy = np.cov(yarr)
        print cov
    '''print ('Cross-Covariance: %f' % cov)
    print ('Covariance X: %f' % covx)
    print ('Covariance Y: %f' % covy)'''

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("position", Pos, callback, queue_size=100)
  # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
