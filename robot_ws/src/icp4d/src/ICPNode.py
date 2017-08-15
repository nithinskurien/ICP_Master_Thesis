#!/usr/bin/env python
PKG = 'ICP'
import time
import timeit
import message_filters
from message_filters import TimeSynchronizer, Subscriber
import rospy
import numpy as np
from gulliview_server.msg import Pos
from icp4d.msg import Vehicle
from robotclient.srv import GetCoord
import MeasurementMixer as me
import algorithm
import Distribution
import DataCollect
import threading
import matplotlib.pyplot as plt
import Kalman
import sys, select, termios, tty
import threading

msg = """
To Activate/Deactivate The ICP Estimate Feedback from the Robot!
---------------------------
ICP Toggle = 'i' 
---------------------------
Press the Key mentioned above to toggle between the ICP-Estimate or the Actual/Simulated Measurements to be fed to the Controller.

CTRL-C to quit
"""

icp_bool = True
count = 0
T_s = 0.35
data = DataCollect.DataCollect(2, 1)
veh, fea = [0, 0]
Gps_x1 = 0.0
Gps_y1 = 0.0
Gps_x0 = 0.0
Gps_y0 = 0.0
angle0 = 0.0
angle1 = 0.0
feat11_x = 0.0
feat11_y = 0.0
feat21_x = 0.0
feat21_y = 0.0
camera_1_x = -0
camera_1_y = 0
camera_2_x = -0
camera_2_y = 0
service1 = True
service2 = False

def callback1(pos):
    # print "Inside Callback1"
    global Gps_x0, Gps_y0, angle0, feat11_x, feat11_y, service1, service2, t1, icp_bool

    #print "Inside Callback"0.0


    #Gps_x1, Gps_y1, Gps_x2, Gps_y2 = 0
    if service1:
        service1 = False
        #print "Pinging Robot0 for Position"
        srv1 = 'get_coord0'
        rospy.wait_for_service(srv1)
        error_count = 0
        try:
            get_coords1 = rospy.ServiceProxy(srv1, GetCoord)
            f = get_coords1(1)
            tmp_pos1 = f.data.data
            while error_count < 4:
                if np.size(tmp_pos1) != 3:
                    Gps_x0 = tmp_pos1[0]
                    Gps_y0 = tmp_pos1[1]
                    error_count = 11
                else:
                    error_count += 1
                    Gps_x0 = None
                    Gps_y0 = None
        except rospy.ServiceException as exc1:
            print("Service1 did not process request: " + str(exc1))
        if error_count < 5:
            print("Error: Not Receiving Position Data From Vehicle 1")
        service2 = True

        if (pos.heading1 == 0):
            angle0 = 0.0
            feat11_x = 0.0
            feat11_y = 0.0

        if (pos.heading1 != 0 and icp_bool is False):
            angle0 = 2 * np.pi - euler0to360(pos.heading1 * (10 ** -6))
            feat11_x = 0.0
            feat11_y = 0.0

        if (pos.heading1 != 0 and icp_bool is True):
            angle0 = 2 * np.pi - euler0to360(pos.heading1 * (10 ** -6))
            feat11_x = pos.x1
            feat11_y = pos.y1
            # feat11_x = camera_1_x*np.cos(angle0)-camera_1_y*np.sin(angle0)+pos.x1
            # feat11_y = camera_1_x*np.sin(angle0)+camera_1_y*np.cos(angle0)+pos.y1
            #Plot.Print(meas, data)

def callback2(pos2):
    # print "Inside Callback2"
    global Gps_x1, Gps_y1, angle1, feat21_x, feat21_y, service1, service2, t1, icp_bool
    if service2:
        service2 = False
        # print "Pinging Robot1 for Position"
        srv2 = 'get_coord1'
        rospy.wait_for_service(srv2)
        error_count2 = 0
        try:
            get_coords2 = rospy.ServiceProxy(srv2, GetCoord)
            f = get_coords2(1)
            tmp_pos2 = f.data.data
            while error_count2 < 4:
                if np.size(tmp_pos2) != 3:
                    Gps_x1 = tmp_pos2[0]
                    Gps_y1 = tmp_pos2[1]
                    error_count2 = 11
                else:
                    error_count2 += 1
                    Gps_x1 = None
                    Gps_y1 = None
        except rospy.ServiceException as exc2:
            print("Service2 did not process request: " + str(exc2))
        if error_count2 < 5:
            print("Error: Not Receiving Position Data From Vehicle 2")
        service1 = True

        if (pos2.heading1 == 0):
            angle1 = 0.0
            feat21_x = 0.0
            feat21_y = 0.0

        if (pos2.heading1 != 0 and icp_bool is False):
            angle1 = 2 * np.pi - euler0to360(pos2.heading1 * (10 ** -6))
            feat21_x = 0.0
            feat21_y = 0.0

        if (pos2.heading1 != 0 and icp_bool is True):
            angle1 = 2 * np.pi - euler0to360(pos2.heading1 * (10 ** -6))
            feat21_x = pos2.x1
            feat21_y = pos2.y1
            # feat21_x = camera_2_x*np.cos(angle1)-camera_2_y*np.sin(angle1)+pos2.x1
            # feat21_y = camera_2_x*np.sin(angle1)+camera_2_y*np.cos(angle1)+pos2.y1

        icp()


def icp():

    global count, Gps_x0, Gps_y0, Gps_x1, Gps_y1, veh, fea, data
    if icp_bool:
        msg2 = ''' ( ICP Activated ) '''
    if not icp_bool:
        msg2 = ''' ( ICP De-Activated ) '''
    print "-------------------------------- ****** Run " + str(count) + str(msg2) +" ****** --------------------------------"
    if count == 0:
        n_v = 2
        n_f = 1
        p1 = np.matrix([[Gps_x0], [Gps_y0], [0], [0]])
        p2 = np.matrix([[Gps_x1], [Gps_y1], [0], [0]])
        cov1 = np.matrix('10 0 0 0; '
                         '0 10 0 0; '
                         '0 0 1 0; '
                         '0 0 0 1')
        cov2 = np.matrix('10 0 0 0; '
                         '0 10 0 0; '
                         '0 0 1 0; '
                         '0 0 0 1')
        init_veh_distr = [Distribution.Distribution(p1, cov1), Distribution.Distribution(p2, cov2)]
        p3 = np.matrix('1.7; 0.5')
        cov3 = np.matrix('10 0; 0 10')
        init_feat_distr = [Distribution.Distribution(p3, cov3)]
        q0 = 1.0e-2
        q1 = 1.0e-2
        var_init = [q0, q1]
        data = DataCollect.DataCollect(n_v, n_f)
        data.init(n_v, n_f, init_veh_distr, init_feat_distr)
        veh = algorithm.init_veh(n_v, n_f, init_veh_distr, init_feat_distr, var_init)

    count = count + 1
    start_time = rospy.get_time()
    if (Gps_x0 and Gps_x1 and Gps_y0 and Gps_y1) is not None:
        mean_v = [np.matrix([[Gps_x0], [Gps_y0]]), np.matrix([[Gps_x1], [Gps_y1]])]
        mean_f = [[np.matrix([[float(feat11_x)/1000], [float(feat11_y)/1000]]), np.matrix([[float(feat21_x)/1000], [float(feat21_y)/1000]])]]
        #data = DataCollect.DataCollect(2, 1)
        meas = me.MeasurementMixer(2, 1, mean_v, mean_f)
        print "Feature 1 Measurement X = " + str(float(meas.meas_fea[0][0][0])) + " , Y = " + str(float(meas.meas_fea[0][0][1]))
        print "Feature 2 Measurement X = " + str(float(meas.meas_fea[0][1][0])) + " , Y = " + str(float(meas.meas_fea[0][1][1]))
        print "Vehicle 1 Measurement X = " + str(float(meas.meas_veh[0][0])) + " , Y = " + str(float(meas.meas_veh[0][1]))
        print "Vehicle 2 Measurement X = " + str(float(meas.meas_veh[1][0])) + " , Y = " + str(float(meas.meas_veh[1][1]))
        #print v
        #print "Feature in callback" + str(fea)
        for v in veh:
            v.update_time_step(T_s)
        algorithm.main_loop(veh, meas, 2, 1, data)
        actual1 = data.get_veh_belief(0)
        actual2 = data.get_veh_belief(1)
        last_x0 = actual1[0][-1]
        last_y0 = actual1[1][-1]
        last_x1 = actual2[0][-1]
        last_y1 = actual2[1][-1]
        x_coord0 = float(meas.meas_veh[0][0])
        y_coord0 = float(meas.meas_veh[0][1])
        x_coord1 = float(meas.meas_veh[1][0])
        y_coord1 = float(meas.meas_veh[1][1])

        print 'Vehicle 1 ICP X = ' + str(last_x0) + ', Y = ' + str(last_y0)
        print 'Vehicle 2 ICP X = ' + str(last_x1) + ', Y = ' + str(last_y1)
        global T_s
        stop_time = rospy.get_time()
        # T_s = stop_time - start_time
        print T_s, "Sampling Time"
        print str(count) + "Runs"

        vehicle0 = Vehicle()
        vehicle0.heading = angle0
        vehicle0.header.stamp = rospy.get_rostime()
        vehicle0.x_meas = x_coord0
        vehicle0.y_meas = y_coord0
        vehicle0.x_icp = last_x0
        vehicle0.y_icp = last_y0
        vehicle0.x_actual_meas = Gps_x0
        vehicle0.y_actual_meas = Gps_y0


        vehicle1 = Vehicle()
        vehicle1.heading = angle1
        vehicle1.header.stamp = rospy.get_rostime()
        vehicle1.x_meas = x_coord1
        vehicle1.y_meas = y_coord1
        vehicle1.x_icp = last_x1
        vehicle1.y_icp = last_y1
        vehicle1.x_actual_meas = Gps_x1
        vehicle1.y_actual_meas = Gps_y1

        pub0 = rospy.Publisher("Robot0/config", Vehicle, queue_size=10)
        pub1 = rospy.Publisher("Robot1/config", Vehicle, queue_size=10)
        pub0.publish(vehicle0)
        pub1.publish(vehicle1)
        print "Heading Angle Robot 0: " + str(angle0)
        print "Heading Angle Robot 1: " + str(angle1)

def Get_Key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def Keyboard_Check():
    global icp_bool
    try:
        while True:
            # key = Get_Key()
            key = sys.stdin.read(1)
            if key == 'i':
                icp_bool = not icp_bool
            if key == '\x03':
                t1.exit()
    except:
        print sys.exc_info()[0]

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

def closedown():
    print "ICP has been successfully terminated"
    print_plots(data)

def listener():
    global t1
    # global data, service1, service2
    # global veh, fea
    # global t1
    # n_v = 2
    # n_f = 1
    # p1 = np.matrix('1; 0; 0; 0')
    # p2 = np.matrix('3; 2; 0; 0')
    # cov1 = np.matrix('1000000 0 0 0; '
    #                  '0 1000000 0 0; '
    #                  '0 0 1000000 0; '
    #                  '0 0 0 1000000')
    # cov2 = np.matrix('1000000 0 0 0; '
    #                  '0 1000000 0 0; '
    #                  '0 0 1000000 0; '
    #                  '0 0 0 1000000')
    # init_veh_distr = [Distribution.Distribution(p1, cov1), Distribution.Distribution(p2, cov2)]
    # p3 = np.matrix('0.5; 0.5')
    # cov3 = np.matrix('100000 0; 0 100000')
    # init_feat_distr = [Distribution.Distribution(p3, cov3)]
    # q0 = 10
    # q1 = 0.1
    # var_init = [q0, q1]
    # data = DataCollect.DataCollect(n_v, n_f)
    # data.init(n_v, n_f, init_veh_distr, init_feat_distr)
    # veh = algorithm.init_veh(n_v, n_f, init_veh_distr, init_feat_distr, var_init)
    #print "Feature in listner" + str(fea)
    t1.start()
    rospy.init_node('ICP_Node', anonymous=True)
    rospy.Subscriber("position0", Pos, callback1, queue_size=100)
    rospy.Subscriber("position1", Pos, callback2, queue_size=100)
    # t1 = threading.Thread(target=icp)
    # t1.daemon = True
   # spin() simply keeps python from exiting until this node is stopped
    #print "inside listener"
    # pos = message_filters.Subscriber('position0', Pos)
    # pos2 = message_filters.Subscriber('position1', Pos)
    # ts = message_filters.ApproximateTimeSynchronizer([pos, pos2], 2, 1)
    # ts.registerCallback(callback)
    # plt.ion()
    rospy.spin()
    rospy.on_shutdown(closedown)

def euler0to360(angle):

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    else:
        return angle

def print_plots(data):
    plt.figure()
    plt.subplot
    plt.plot(data.get_feat_belief(0, 0)[0], 'r', label='x')
    plt.plot(data.get_feat_belief(0, 0)[1], 'b', label='y')
    plt.plot(data.get_feat_belief(1, 0)[0]+0.01, 'g', label='x')
    plt.plot(data.get_feat_belief(1, 0)[1]+0.01, 'm', label='y')
    # plt.figure()
    # plt.plot(data.get_veh_belief(1)[0], 'r', label='Robot 0')
    # plt.plot(data.get_veh_belief(1)[1], 'b', label='Robot 1')
    # plt.plot(data.get_pred_veh_belief(1)[0], 'r', label='X')
    # plt.plot(data.get_pred_veh_belief(1)[1], 'b', label='Y')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print msg
    settings = termios.tcgetattr(sys.stdin)
    t1 = threading.Thread(target=Keyboard_Check)
    t1.daemon = True
    listener()
