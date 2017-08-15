#!/usr/bin/env python
# To control the movement of the robots
PKG = 'Controller'
import time
import timeit
import tf
import Trajectory_0 as traj
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

msg = """
To Activate/Deactivate The ICP Estimate Feedback from the Robot!
---------------------------
Robot0 = 'i'
---------------------------
CTRL-C to quit
"""

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
x_meas = []
y_meas = []
theta_meas = []
theta2_meas = []
count = 0
loop = 0
prev_input = np.matrix([[1], [1]])
dist_outlier = 0.5
ang_outlier = 0.3
t_previous = 0
tra_start = 0
lin_vel_max = 0
ang_vel_max = 0
tra_samp = 0
prev_angle = 0.0
prev_encoder_angle = 0.0
X_int = np.matrix([[0.0], [0.0], [0.0]])
P_int = np.matrix([[100.0, 0.0, 0.0], [0.0, 100.0, 0.0], [0.0, 0.0, 100.0]])

def callback(rob0, rob1):
    print"--------------------------*******--------------------------"
    global prev_input, t_previous, count, tra_mod, lin_vel_max, ang_vel_max,\
           tra_start, tra_samp, prev_angle, prev_encoder_angle, X_int, P_int,\
           x_vec, y_vec, theta_vec, tra_plot_theta, tra_plot_x, tra_plot_y, tra_plot_time,\
           dist_outlier, ang_outlier, x_pred, y_pred, theta_pred, x_meas, y_meas, theta_meas, theta2_meas
    # print "inside Callback"
    var_theta = 0.0  #Variance for the gulliview orientation software
    var_theta2 = 0.0 #Variance for the arctan measurement update model
    t_present = rob0.header.stamp.secs + rob0.header.stamp.nsecs*10**(-9)
    Quaternion1 = (rob1.pose.pose.orientation.x, rob1.pose.pose.orientation.y, rob1.pose.pose.orientation.z,
                       rob1.pose.pose.orientation.w)
    euler1 = tf.transformations.euler_from_quaternion(Quaternion1)
    euler_encoder = euler0to360(euler1[2])  # Angle Reading From Encoder
    euler_cor = euler0to360(rob0.heading)  # Angle Reading From Gulliview

    if euler_cor == 0.0:  # Angle Update by taking difference update from Encoders if Tags are not visible
        print "##XXXXXXXXXXX---No Tags---XXXXXXXXXXX##"
        euler_cor = euler0to360(prev_angle + (euler_encoder - prev_encoder_angle))
        var_theta = 1.0e-5
        var_theta2 = 1.0

    if euler_cor != 0.0:   # Angle Update by taking difference update from Encoders if Tags are visible
        var_theta = 2.5e-8
        var_theta2 = 1.0

    t_sampling = t_present - t_previous  #  Sampling Time
    if count == 0:
        t_sampling = 0.1
    # Kalman Filter
    X, P = Kalman.prediction(X_int, P_int, prev_input.item(0), prev_input.item(1), t_sampling)  # Prediction
    X[2][0] = euler0to360(X.item(2))  #Conversion to prevent angle discontinuity 
    x_pred.append(X.item(0))
    y_pred.append(X.item(1))
    theta_pred.append(X.item(2))

    if np.sqrt((X_int.item(0)-rob0.x_meas)**2 + (X_int.item(1)-rob0.y_meas)**2) < dist_outlier or count==0:  # UWB Position Outlier Detector
        Z_k = np.matrix([[rob0.x_meas], [rob0.y_meas]])
        X, P = Kalman.update(X, P, Z_k)
    else:
        print "XXPPPPPPPPPPPPPPPP---Outiler Detected for Position---PPPPPPPPPPPPPPPPXX"
    if np.fabs(prev_angle - euler_check(euler_cor, prev_angle)) < ang_outlier or count==0:  # Angle Outlier
        X, P = Kalman.update_theta(X, P, euler_cor, var_theta)
        Z_k_theta = euler0to360(np.arctan2((X_int.item(1) - X.item(1)), (X_int.item(0) - X.item(0))))
        X, P = Kalman.update_theta(X, P, Z_k_theta, var_theta2)
    else:
        print "XXAAAAAAAAAAAAAAAA---Outiler Detected for Angle---AAAAAAAAAAAAAAAAXX"
    X_int, P_int = X, P
    prev_angle = X.item(2)
    prev_encoder_angle = euler_encoder

    if t_sampling > 10 or count==0:  # re-route function activated if no readings received in 2 secs
        tra_mod = []
        tra_mod, tra_samp = traj.Trajectory().re_route(rob0.x_meas, rob0.y_meas, euler_cor, loop)
        tra_start = t_present
        prev_input = np.matrix([[0.1], [0.1]])
        print "Trajectory Planned"
    size = len(tra_mod[0])
    count = int((t_present - tra_start)/tra_samp)

    if count > int(size-1):     # If measurement not updated for long time stop control (Robot may become unstable)
        rospy.signal_shutdown("Controller has been successfully terminated")

    prev_input = lqr.lqr(X.item(0), X.item(1), euler_check(prev_angle, tra_mod[2][count]),
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

    x_meas.append(rob0.x_meas)
    y_meas.append(rob0.y_meas)
    theta_meas.append(euler_cor)
    theta2_meas.append(Z_k_theta)
    x_vec.append(X.item(0))
    y_vec.append(X.item(1))
    theta_vec.append(X.item(2))
    tra_plot_x.append(tra_mod[0][count])
    tra_plot_y.append(tra_mod[1][count])
    tra_plot_theta.append(tra_mod[2][count])
    tra_plot_time.append(count*tra_samp)
    twist = Twist()
    twist.linear.x = lin_vel
    twist.angular.z = ang_vel
    pub = rospy.Publisher("Robot0/cmd_vel", Twist, queue_size=10)
    pub.publish(twist)
    print "Trajectory count : " + str(count) + ", Sampling Time : " + str(round(t_sampling, 3))
    t_previous = t_present
    count += 1

def euler0to360(angle):  # To convert the -pi to pi range to 0 to 2Pi

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    else:
        return angle

def euler_check(angle, angle2):  #To check for the angle discontinuity between 0 and 2Pi

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
    title_font = {'fontname': 'Arial', 'size': '20', 'color': 'black', 'weight': 'normal',
                  'verticalalignment': 'bottom'}  # Bottom vertical alignment for more space
    axis_font = {'fontname': 'Arial', 'size': '20'}
    plt.figure()
    plt.plot(tra_plot_x, tra_plot_y, '--b', label='Refrence Trajectory', linewidth=4.5, alpha=0.9, mec='b')
    plt.plot(x_vec, y_vec, 'r', label='Trajectory', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(x_pred[1:], y_pred[1:], '--g', label='Prediction', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(x_meas, y_meas, 'oc', label='Measurement', markersize=2.0,  alpha=0.5, mec='b')
    plt.grid(True)
    plt.title('Trajectory', **title_font)
    plt.xlabel('X $(m)$', **axis_font)
    plt.ylabel('Y $(m)$', **axis_font)
    plt.xlim((0.5, 3.0))
    plt.ylim((-0.5, 3.0))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tick_params(labelsize=20)
    plt.legend()
    plt.figure()
    plt.plot(tra_plot_time, tra_plot_theta, '--b', label='Reference Theta', linewidth=4.5, alpha=0.9, mec='b')
    plt.plot(tra_plot_time, theta_vec, 'r', label='Theta', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(tra_plot_time, theta_pred, '--g', label='Theta', linewidth=2.5, alpha=0.9, mec='b')
    plt.plot(tra_plot_time, theta_meas, 'om', label='Measurement 1', markersize=2.0, alpha=0.5, mec='b')
    plt.plot(tra_plot_time, theta2_meas, 'oc', label='Measurement 2', markersize=2.0, alpha=0.5, mec='b')
    plt.grid(True)
    plt.title('$\Theta$ Reference', **title_font)
    plt.xlabel('Time $(secs)$', **axis_font)
    plt.ylabel('$\Theta\ (rad)$', **axis_font)
    plt.tick_params(labelsize=20)
    plt.legend()
    plt.show()

def listener():
    rospy.init_node('Controller', anonymous=True)
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
    rob0 = message_filters.Subscriber('Robot0/config', Vehicle)
    rob1 = message_filters.Subscriber('Robot0/pose', Odometry)
    ts = message_filters.ApproximateTimeSynchronizer([rob0, rob1], 2, 50)
    ts.registerCallback(callback)
    rospy.spin()
    rospy.on_shutdown(closedown)

if __name__ == '__main__':
    listener()
