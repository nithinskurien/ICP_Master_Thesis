#!/usr/bin/env python
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
import matplotlib.pyplot as plt
import Kalman
import LQR_Control as lqr

tra_mod = []
tra_plot_x = []
tra_plot_y = []
tra_plot_theta = []
tra_plot_time = []
x_vec = []
y_vec = []
theta_vec = []
count = 0
prev_input = np.matrix([[1], [1]])
t_previous = 0
tra_start = 0
lin_vel_max = 0
ang_vel_max = 0
tra_samp = 0
loop = 0

def callback(rob0):
    global prev_input, t_previous, count, tra_mod, lin_vel_max, ang_vel_max, tra_start, tra_samp,\
           x_vec, y_vec, theta_vec, tra_plot_time
    print "inside Callback"
    t_present = rob0.header.stamp.secs + rob0.header.stamp.nsecs*10**(-9)
    Quaternion1 = (rob0.pose.pose.orientation.x, rob0.pose.pose.orientation.y, rob0.pose.pose.orientation.z,
                       rob0.pose.pose.orientation.w)
    euler1 = tf.transformations.euler_from_quaternion(Quaternion1)
    euler_cor = euler0to360(euler1[2])
    t_sampling = t_present - t_previous

    if t_sampling > 2:  # re-route function activated if no readings received in 2 secs
        tra_mod = []
        tra_mod, tra_samp = traj.Trajectory().re_route(rob0.pose.pose.position.x, rob0.pose.pose.position.y, euler_cor, loop)
        tra_start = t_present
        prev_input = np.matrix([[1], [1]])
        print "Trajectory Planned"
    size = len(tra_mod[0])
    count = int((t_present - tra_start)/tra_samp)

    if count > int(size-1):
        rospy.signal_shutdown("Controller has been successfully terminated")

    if (np.fabs(tra_mod[0][count] - tra_mod[0][count+1]) + np.fabs(tra_mod[1][count] - tra_mod[1][count+1])) == 0.0:  #Only Roation LQR
        ang_vel = lqr.lqr_rotate(euler_check(euler1[2], tra_mod[2][count]), tra_mod[2][count], t_sampling)
        lin_vel = 0

    if (np.fabs(tra_mod[0][count] - tra_mod[0][count+1]) + np.fabs(tra_mod[1][count] - tra_mod[1][count+1])) != 0.0:  #Translation and Rotation LQR
        prev_input = lqr.lqr(rob0.pose.pose.position.x, rob0.pose.pose.position.y, euler_check(euler1[2], tra_mod[2][count]),
                         tra_mod[0][count], tra_mod[1][count], tra_mod[2][count], prev_input.item(0),
                         prev_input.item(1), t_sampling)
        lin_vel = prev_input[0]
        ang_vel = prev_input[1]

    if lin_vel > lin_vel_max:
        lin_vel_max = lin_vel

    if ang_vel > ang_vel_max:
        ang_vel_max = ang_vel

    print "Maximum Linear Velocity: " + str(round(lin_vel_max, 3)) + ", Maximum Angular Velocity: " + str(round(ang_vel_max, 3))
    print "Robot: ang: " + str(round(euler_cor, 3)) + ", x: " + str(round(rob0.pose.pose.position.x, 3)) + ", y: " + str(round(rob0.pose.pose.position.y, 3)) +\
          ", Trajectory Orientation: ang: " + str(round(tra_mod[2][count], 3)) + ", x: " + str(round(tra_mod[0][count], 3)) + ", y: " + str(round(tra_mod[1][count], 3))
    x_vec.append(rob0.pose.pose.position.x)
    y_vec.append(rob0.pose.pose.position.y)
    theta_vec.append(euler_cor)
    tra_plot_time.append(count * tra_samp)
    tra_plot_x.append(tra_mod[0][count])
    tra_plot_y.append(tra_mod[1][count])
    tra_plot_theta.append(tra_mod[2][count])


    twist = Twist()
    twist.linear.x = lin_vel
    twist.angular.z = ang_vel
    pub = rospy.Publisher("Robot0/cmd_vel", Twist, queue_size=10)
    pub.publish(twist)
    print "Trajectory count : " + str(count) + ", Sampling Time : " + str(round(t_sampling, 3))
    t_previous = t_present
    count += 1

def euler0to360(angle):

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    else:
        return angle

def euler_check(angle, angle2):

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    if abs(angle2 - angle) > np.pi:
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
    plt.plot(x_vec, y_vec, 'r', label='Trajectory', linewidth=2.5, alpha=0.8, mec='b')
    plt.grid(True)
    plt.title('Trajectory', **title_font)
    plt.xlabel('X $(m)$', **axis_font)
    plt.ylabel('Y $(m)$', **axis_font)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tick_params(labelsize=20)
    # plt.xlim((0.0, 3.0))
    # plt.ylim((-0.25, 2.5))
    plt.legend()
    plt.figure()
    plt.plot(tra_plot_time, tra_plot_theta, '--b', label='Reference $\Theta$', linewidth=4.5, alpha=0.9, mec='b')
    plt.plot(tra_plot_time, theta_vec, 'r', label='$\Theta$', linewidth=2.5, alpha=0.8, mec='b')
    plt.grid(True)
    plt.title('$\Theta$ Reference', **title_font)
    plt.xlabel('Time $(secs)$', **axis_font)
    plt.ylabel('$\Theta\ (rad)$', **axis_font)
    plt.tick_params(labelsize=20)
    plt.legend()
    plt.show()

def listener():
    global loop
    true_input = False
    while not true_input:
        try:
            loop = int(raw_input('Enter The no of Loops to Run:'))
            true_input = True
        except ValueError:
            print "Not a number"
    rospy.init_node('Controller', anonymous=True)
    rospy.Subscriber('Robot0/pose', Odometry, callback, queue_size=100)
    # spin() simply keeps python from exiting until this node is stopped
    print "inside listener"
    # rob0 = message_filters.Subscriber('Robot0/pose', Odometry)
    # rob1 = message_filters.Subscriber('Robot1/pose', Odometry)
    # ts = message_filters.ApproximateTimeSynchronizer([rob0, rob1], 2, 1)
    # ts.registerCallback(callback)
    rospy.spin()
    rospy.on_shutdown(closedown)

if __name__ == '__main__':
    listener()
