#!/usr/bin/env python
PKG = 'ICP'
import time
import timeit
import message_filters
from message_filters import TimeSynchronizer, Subscriber
import rospy
import numpy as np
from gulliview_server.msg import Pos
from icp.msg import Vehicle
from robotclient.srv import GetCoord
import MeasurementMixer as me
import algorithm
import Distribution
import DataCollect
import matplotlib.pyplot as plt
import Kalman
count = 0
T_s = 0.20
data = DataCollect.DataCollect(2, 1)
veh, fea = [0, 0]

def callback(pos, pos2):
    global count
    count = count + 1
    start_time = rospy.get_time()
    #print "Inside Callback"
    srv1 = 'get_coord0'
    srv2 = 'get_coord1'
    #Gps_x1, Gps_y1, Gps_x2, Gps_y2 = 0
    rospy.wait_for_service(srv1)
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

    rospy.wait_for_service(srv2)
    error_count = 0
    try:
         get_coords2 = rospy.ServiceProxy(srv2, GetCoord)
         f = get_coords2(1)
         tmp_pos2 = f.data.data
         while error_count < 10:
            if np.size(tmp_pos2) != 3:
                Gps_x2 = tmp_pos2[0]
                Gps_y2 = tmp_pos2[1]
                error_count = 11
            else:
                error_count += 1
                Gps_x2 = None
                Gps_y2 = None
    except rospy.ServiceException as exc2:
        print("Service2 did not process request: " + str(exc2))

    if (Gps_x1 and Gps_x2 and Gps_y1 and Gps_y2) is not None:
        mean_v = [np.matrix([[Gps_x1], [Gps_y1]]), np.matrix([[Gps_x2], [Gps_y2]])]
        mean_f = [[np.matrix([[float(pos.x1)/1000], [float(pos.y1)/1000]]), np.matrix([[float(pos2.x1)/1000], [float(pos2.y1)/1000]])]]
        #data = DataCollect.DataCollect(2, 1)

        T_s = 0.1
        meas = me.MeasurementMixer(2, 1, mean_v, mean_f)
        print "Feature 1 Measurement X = " + str(float(meas.meas_fea[0][0][0])) + " , Y = " + str(float(meas.meas_fea[0][0][1]))
        print "Feature 2 Measurement X = " + str(float(meas.meas_fea[0][1][1])) + " , Y = " + str(float(meas.meas_fea[0][1][1]))
        print "Vehicle 1 Measurement X = " + str(float(meas.meas_veh[0][0])) + " , Y = " + str(float(meas.meas_veh[0][1]))
        print "Vehicle 2 Measurement X = " + str(float(meas.meas_veh[1][0])) + " , Y = " + str(float(meas.meas_veh[1][1]))
        #print v
        #print "Feature in callback" + str(fea)
        algorithm.main_loop(veh, fea, meas, 7, 1, data)
        actual1 = data.get_veh_belief(0)
        actual2 = data.get_veh_belief(1)
        last_x = actual1[0][-1]
        last_y = actual1[1][-1]
        last_x2 = actual2[0][-1]
        last_y2 = actual2[1][-1]

        print 'Vehicle 1 ICP X = ' + str(last_x) + ', Y = ' + str(last_y)
        print 'Vehicle 2 ICP X = ' + str(last_x2) + ', Y = ' + str(last_y2)
        global T_s
        stop_time = rospy.get_time()
        T_s = stop_time - start_time
        print T_s, "Sampling Time"
        print str(count) + "Runs"

def listener():
    global data
    global veh, fea
    data = DataCollect.DataCollect(2, 1)
    p1 = np.matrix('1.01; 0.1')
    p2 = np.matrix('2.9; 1.9')
    cov1 = np.matrix('0.5 0; 0 0.5')
    cov2 = np.matrix('0.5 0; 0 0.5')
    init_veh_distr = [Distribution.Distribution(p1, cov1), Distribution.Distribution(p2, cov2)]
    p3 = np.matrix('0.5; 0.5')
    cov3 = np.matrix('5 0; 0 5')
    init_feat_distr = [Distribution.Distribution(p3, cov3)]

    data.init(2, 1, init_veh_distr, init_feat_distr)
    var_pos1 = 200
    var_pos2 = 200
    var_init = [[var_pos1, var_pos1], [var_pos2, var_pos2]]
    veh = algorithm.init_veh(2, 1, init_veh_distr, var_init)
    fea = algorithm.init_feat(1, 2, init_feat_distr)
    #print "Feature in listner" + str(fea)
    rospy.init_node('listener', anonymous=True)
   # rospy.Subscriber("position2", Pos, callback, queue_size=100)
   # spin() simply keeps python from exiting until this node is stopped
    #print "inside listener"
    pos = message_filters.Subscriber('position', Pos)
    pos2 = message_filters.Subscriber('position2', Pos)
    ts = message_filters.ApproximateTimeSynchronizer([pos, pos2], 2, 1)
    ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
