#!/usr/bin/env python
PKG = 'Controller'
import time
import timeit
import tf
import Trajectory_Param as traj
import rospy
import message_filters
from message_filters import TimeSynchronizer, Subscriber
import numpy as np
from controller.msg import Pos
from controller.srv import GetCoord
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from controller.msg import Vehicle
import matplotlib.pyplot as plt
import Kalman
import LQR_Control as lqr
import sys, select, termios, tty
import threading


icp_bool = True
tra_mod = []
x_vec = []
y_vec = []
x_pred = []
y_pred = []
theta_pred = []
theta_vec = []
tra_plot_x = []
tra_plot_y = []
tra_plot_theta = []
tra_plot_time = []
tra_plot_time2 = []
no_tag_x = []
no_tag_y = []
x_meas = []
x_actual_meas_vec = []
y_actual_meas_vec = []
error_dist_vec = []
y_meas = []
x_icp_meas = []
y_icp_meas = []
theta_meas = []
theta2_meas = []
count = 0
count_tag = 0
loop = 0
prev_input = np.matrix([[0.1], [0.1]])
dist_outlier = 0.3
ang_outlier = 0.3
t_previous = 0
tra_start = 0
lin_vel_max = 0
ang_vel_max = 0
tra_samp = 0
prev_angle = 0.0
prev_encoder_angle = 0.0
prev_euler_angle = 0.0
prev_meas_x = 0.0
prev_meas_y = 0.0
X_int = np.matrix([[0.0], [0.0], [0.0]])
P_int = np.matrix([[100.0, 0.0, 0.0], [0.0, 100.0, 0.0], [0.0, 0.0, 100.0]])

def callback(rob0, rob1):
    print"--------------------------*** Robot 1 ***--------------------------"
    global prev_input, t_previous, count, tra_mod, lin_vel_max, ang_vel_max,\
           tra_start, tra_samp, prev_angle, prev_encoder_angle, X_int, P_int,\
           x_vec, y_vec, theta_vec, tra_plot_theta, tra_plot_x, tra_plot_y, tra_plot_time, tra_plot_time2, \
           dist_outlier, ang_outlier, x_pred, y_pred, theta_pred, x_meas, y_meas, theta_meas, theta2_meas, \
           x_icp_meas, y_icp_meas, prev_euler_angle, prev_meas_x, prev_meas_y, no_tag_x, no_tag_y, count_tag, \
           x_actual_meas_vec, y_actual_meas_vec, error_dist_vec
    # print "inside Callback"
    var_theta = 0.0
    var_theta2 = 0.0
    t_present = rob0.header.stamp.secs + rob0.header.stamp.nsecs*10**(-9)
    Quaternion1 = (rob1.pose.pose.orientation.x, rob1.pose.pose.orientation.y, rob1.pose.pose.orientation.z,
                       rob1.pose.pose.orientation.w)
    euler1 = tf.transformations.euler_from_quaternion(Quaternion1)
    euler_encoder = euler0to360(euler1[2])  # Angle Reading From Encoder
    euler_cor = euler0to360(rob0.heading)  # Angle Reading From Gulliview

    if icp_bool:
        x_meas_used = rob0.x_icp
        y_meas_used = rob0.y_icp

    if not icp_bool:
        x_meas_used = rob0.x_meas
        y_meas_used = rob0.y_meas
        # x_meas_used = rob0.x_actual_meas
        # y_meas_used = rob0.y_actual_meas


    if euler_cor == 0.0:  # Angle Update by taking difference update from Encoders if Tags are not visible
        print "##XXXXXXXXXXX---No Tags---XXXXXXXXXXX##"
        euler_cor = euler0to360(prev_angle + (euler_encoder - prev_encoder_angle))
        var_theta = 1.0e-5
        var_theta2 = 1.0

    if euler_cor != 0.0:
        var_theta = 2.5e-8
        var_theta2 = 1.0

    t_sampling = t_present - t_previous  #  Sampling Time
    if count == 0:
        t_sampling = 0.3
    # Kalman Filter

    X, P = Kalman.prediction(X_int, P_int, prev_input.item(0), prev_input.item(1), t_sampling)  # Prediction
    X[2][0] = euler0to360(X.item(2))
    x_pre_temp = X.item(0)
    y_pre_temp = X.item(1)
    theta_temp = X.item(2)

    if np.sqrt((prev_meas_x - x_meas_used)**2 + (prev_meas_y - y_meas_used)**2) < dist_outlier or count==0:  # UWB Outlier Detector
        Z_k = np.matrix([[x_meas_used], [y_meas_used]])
        X, P = Kalman.update(X, P, Z_k)
    else:
        print "XXPPPPPPPPPPPPPPPP---Outiler Detected for Position---PPPPPPPPPPPPPPPPXX"
    if np.fabs(prev_euler_angle - euler_check(euler_cor, prev_angle)) < ang_outlier or count==0:  # Angle Outlier
        X, P = Kalman.update_theta(X, P, euler_cor, var_theta)
        Z_k_theta = euler0to360(np.arctan2(-(X_int.item(1) - X.item(1)), -(X_int.item(0) - X.item(0))))
        theta2_meas.append(Z_k_theta)
        tra_plot_time2.append(count * tra_samp)
        X, P = Kalman.update_theta(X, P, Z_k_theta, var_theta2)
    else:
        print "XXAAAAAAAAAAAAAAAA---Outiler Detected for Angle---AAAAAAAAAAAAAAAAXX"
    X_int, P_int = X, P
    prev_angle = X.item(2)
    prev_encoder_angle = euler_encoder
    prev_euler_angle = euler_cor
    prev_meas_x = x_meas_used
    prev_meas_y = y_meas_used
    # prev_meas_x = rob0.x_meas
    # prev_meas_y = rob0.y_meas

    if icp_bool is True:
        ctrl_x = x_meas_used
        ctrl_y = y_meas_used
    else:
        ctrl_x = X.item(0)
        ctrl_y = X.item(1)

    if count==0:  # re-route function activated if no readings received in 2 secs
        tra_mod = []
        # tra_mod, tra_samp = traj.Trajectory(1.7, 1.1, 1.0).re_route(rob0.x_actual_meas, rob0.y_actual_meas, euler_cor, loop)
        tra_mod, tra_samp = traj.Trajectory(1.7, 1.1, 0.4).re_route(ctrl_x, ctrl_y, euler_cor, loop)
        tra_start = t_present
        prev_input = np.matrix([[0.1], [0.1]])
        print "Trajectory Planned"
    size = len(tra_mod[0])
    count = int((t_present - tra_start)/tra_samp)
    if rob0.heading == 0.0:
        count_tag += 1
        if count_tag > 2:
            no_tag_x.append(tra_mod[0][count])
            no_tag_y.append(tra_mod[1][count])
            count_tag = 0


    if count > int(size-1):
        rospy.signal_shutdown("Controller has been successfully terminated")

    prev_input = lqr.lqr(ctrl_x, ctrl_y, euler_check(prev_angle, tra_mod[2][count]),
                         tra_mod[0][count], tra_mod[1][count], tra_mod[2][count], prev_input.item(0),
                         prev_input.item(1), t_sampling)
    lin_vel = prev_input[0]
    ang_vel = prev_input[1]

    if lin_vel > lin_vel_max:  # Finding Maximum Linear Velocity
        lin_vel_max = lin_vel

    if ang_vel > ang_vel_max:  # Finding Maximum Angular Velocity
        ang_vel_max = ang_vel

    print "Maximum Linear Velocity: " + str(round(lin_vel_max, 3)) + ", Maximum Angular Velocity: " + str(round(ang_vel_max, 3))
    print "Robot: ang: " + str(round(X.item(2), 3)) + ", x: " + str(round(X.item(0), 3)) + ", y: " + str(round(X.item(1), 3)) +\
          ", Trajectory Orientation: ang: " + str(round(tra_mod[2][count], 3)) + ", x: " + str(round(tra_mod[0][count], 3)) + ", y: " + str(round(tra_mod[1][count], 3))
    if count==0:
        error_dist = np.sqrt((tra_mod[0][count] - rob0.x_actual_meas) ** 2 + (tra_mod[1][count] - rob0.y_actual_meas) ** 2)
    else:
        error_dist = np.sqrt((tra_mod[0][count - 1] - rob0.x_actual_meas) ** 2 + (tra_mod[1][count - 1] - rob0.y_actual_meas) ** 2)
    error_dist_vec.append(error_dist)
    x_meas.append(rob0.x_meas)
    y_meas.append(rob0.y_meas)
    x_actual_meas_vec.append(rob0.x_actual_meas)
    y_actual_meas_vec.append(rob0.y_actual_meas)
    x_icp_meas.append(rob0.x_icp)
    y_icp_meas.append(rob0.y_icp)
    theta_meas.append(euler_cor)
    x_vec.append(X.item(0))
    y_vec.append(X.item(1))
    theta_vec.append(X.item(2))
    tra_plot_x.append(tra_mod[0][count])
    tra_plot_y.append(tra_mod[1][count])
    tra_plot_theta.append(tra_mod[2][count])
    x_pred.append(x_pre_temp)
    y_pred.append(y_pre_temp)
    theta_pred.append(theta_temp)
    tra_plot_time.append(count*tra_samp)
    twist = Twist()
    twist.linear.x = lin_vel
    twist.angular.z = ang_vel
    pub = rospy.Publisher("Robot1/cmd_vel", Twist, queue_size=10)
    pub.publish(twist)
    # print "X_pred_Length" + str(len(x_pred))
    # print "Y_pred_Length" + str(len(y_pred))
    # print "Theta_pred_Length" + str(len(theta_pred))
    # print "Time_Length" + str(len(tra_plot_theta))
    print "Trajectory count : " + str(count) + ", Sampling Time : " + str(round(t_sampling, 3))
    t_previous = t_present
    count += 1

def euler0to360(angle):

    if angle < 0:
        angle = angle + 2 * np.pi
    elif angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    return angle

def euler_check(angle, angle2):

    # if angle < 0:
    #     angle = angle + 2 * np.pi
    # if angle > 2 * np.pi:
    #     angle = angle - 2 * np.pi
    if angle2 - angle > np.pi:
        return angle + 2 * np.pi
    elif angle2 - angle < -np.pi:
        return angle - 2 * np.pi
    else:
        return angle

def closedown():
    print "Controller has been successfully terminated"
    print_plots()


def print_plots():
    root_mean = sum(error_dist_vec) / float(len(error_dist_vec))
    textstr = '$\mathrm{Mean\ distance\ error} = %.2f$' % (root_mean)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    title_font = {'fontname': 'Arial', 'size': '20', 'color': 'black', 'weight': 'normal',
                  'verticalalignment': 'bottom'}  # Bottom vertical alignment for more space
    axis_font = {'fontname': 'Arial', 'size': '20'}
    fig1 = plt.figure()
    plt.plot(tra_mod[0], tra_mod[1], '--b', label='Reference Trajectory', linewidth=4.5, alpha=0.9, mec='b')
    # plt.plot(tra_plot_x, tra_plot_y, '--b', label='Reference Trajectory', linewidth=4.5, alpha=0.9, mec='b')
    if not icp_bool:
        plt.plot(x_vec, y_vec, 'r', label='Trajectory', linewidth=2.5, alpha=0.9, mec='b')
    if not icp_bool:
        plt.plot(x_pred[1:], y_pred[1:], '--g', label='Prediction', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(x_meas, y_meas, 'oc', label='Simulated Measurements', markersize=5.0, alpha=0.5, mec='b')
    plt.plot(x_actual_meas_vec, y_actual_meas_vec, '+g', label='Actual Measurements', markersize=8.0,  mew=3.0, alpha=0.5)
    if icp_bool:
        plt.plot(x_icp_meas, y_icp_meas, 'om', label='ICP Estimates', markersize=5.0, alpha=0.5, mec='b')
    plt.plot(no_tag_x, no_tag_y, 'xr', label='No-Tags Region', markersize=10.0,  mew=5, alpha=0.5)
    plt.grid(True)
    plt.title('Trajectory tracking Robot1')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.xlim((1, 3.0))
    plt.ylim((0.6, 1.8))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tick_params(labelsize=20)
    plt.legend(loc=2, prop={'size':8})
    # fig1.set_rasterized(True)
    # plt.savefig('Robot_0_Trajectory.eps', rasterized=True, dpi=300)
    plt.savefig('Robot_1_Trajectory.eps')
    fig2 = plt.figure()
    # plt.plot(tra_mod[2], '--b', label='Reference Theta', linewidth=4.5, alpha=0.9, mec='b')
    plt.plot(tra_plot_theta, tra_plot_time, '--b', label='Reference Theta', linewidth=4.5, alpha=0.9, mec='b')
    plt.plot(theta_vec, tra_plot_time, 'r', label='Theta', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(theta_pred, tra_plot_time, '--g', label='Theta Prediction', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(theta_meas, tra_plot_time, 'om', label='Measurement 1', markersize=5.0, alpha=0.5, mec='b')
    plt.plot(theta2_meas, tra_plot_time2, 'oc', label='Measurement 2', markersize=5.0, alpha=0.5, mec='b')
    plt.grid(True)
    plt.title('$\Theta$ tracking Robot1')
    plt.xlabel('Time (secs)')
    plt.ylabel('$\Theta\ $(rad)')
    plt.tick_params(labelsize=20)
    plt.legend(loc=2, prop={'size':8})
    # fig2.set_rasterized(True)
    # plt.savefig('Robot_0_Theta.eps', rasterized=True, dpi=300)
    plt.savefig('Robot_1_Theta.eps')
    # plt.figure()
    # plt.plot(x_icp_meas, tra_plot_time, 'r', label='X_ICP', linewidth=2.5, alpha=0.4)
    # plt.plot(y_icp_meas, tra_plot_time, 'b', label='Y_ICP', linewidth=2.5, alpha=0.4)
    fig3, ax = plt.subplots()
    plt.plot(tra_plot_time, error_dist_vec, 'r', label='Distance error', linewidth=1.5, alpha=0.9, mec='b')
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
    plt.xlabel('Time (secs)')
    plt.ylabel('Distance (m)')
    plt.grid(True)
    plt.legend()
    plt.title('Distance error Robot1')
    plt.savefig('Robot_1_Error.eps')
    plt.show()


def listener():
    rospy.init_node('Robot_Controller1', anonymous=True)
    global loop
    true_input = False
    while not true_input:
        try:
            loop = int(raw_input('Enter The no of Loops to Run:'))
            true_input = True
        except ValueError:
            print "Not a number"
    # rospy.Subscriber('Robot0/config', Vehicle, callback, queue_size=100)
    # spin() simply keeps python from exiting until this node is stopped
    print "inside listener"
    #t1.start()
    rob0 = message_filters.Subscriber('Robot1/config', Vehicle)
    rob1 = message_filters.Subscriber('Robot1/pose', Odometry)
    ts = message_filters.ApproximateTimeSynchronizer([rob0, rob1], 2, 50)
    ts.registerCallback(callback)
    rospy.spin()
    rospy.on_shutdown(closedown)

if __name__ == '__main__':
    listener()
