# LQR Controller For the robot to generate the input necessary for the robots motion

import numpy as np
import scipy.linalg

def lqr(x, y, theta, x_ref, y_ref, theta_ref, v, phi, ts):

    A = np.matrix([[1, 0, (-v * np.cos(theta) + v * np.cos(phi * ts + theta)) / phi],
                   [0, 1, (-v * np.sin(theta) + v * np.sin(phi * ts + theta)) / phi],
                   [0, 0, 1]])

    # A = np.matrix([[1, 0, 0],
    #                [0, 1, 0],
    #                [0, 0, 1]])

    B = np.matrix([[(-np.sin(theta) + np.sin(phi * ts + theta)) / phi, (ts * v * np.cos(phi * ts + theta) + x) / phi - (phi * x - v * np.sin(theta) + v * np.sin(phi * ts + theta)) / phi ** 2],
                   [(np.cos(theta) - np.cos(phi * ts + theta)) / phi, (ts * v * np.sin(phi * ts + theta) + y) / phi - (phi * y + v * np.cos(theta) - v * np.cos(phi * ts + theta)) / phi ** 2],
                   [0, ts]])

    Q = np.matrix([[40.0, 0, 0],   #Linear_Q
                   [0, 40.0, 0],
                   [0, 0, 30.0]])

    # Q = np.matrix([[375.0, 0, 0],
    #                [0, 375.0, 0],
    #                [0, 0, 180.0]])

    R = np.matrix([[50.0, 0],
                   [0, 50.0]])
    print "Angle Input to Controller: " + str(theta)
    """Solve the discrete time lqr controller.
    x[k+1] = A x[k] + B u[k]
    cost = sum x[k].T*Q*x[k] + u[k].T*R*u[k]
    """
    # ref Bertsekas, p.151
    # first, try to solve the ricatti equation
    X = np.matrix(scipy.linalg.solve_discrete_are(A, B, Q, R))

    # compute the LQR gain
    K = np.matrix(scipy.linalg.inv(B.T * X * B + R) * (B.T * X * A))

    eigVals, eigVecs = scipy.linalg.eig(A - B * K)
    # if (theta!=0.0):
    error = np.matrix([[x_ref-x], [y_ref-y], [theta_ref - theta]])
    input = np.dot(K, error)
    #print K
    #print K[0:2, 0:2]
    # if(theta==0.0):
    #     error = np.matrix([[x_ref - x], [y_ref - y]])
    #     input = np.dot(K[0:2, 0:2], error)
    # print "Full Model LQR"

    return input

def lqr_rotate(theta, theta_ref, ts):

    A = np.matrix([[1]])

    B = np.matrix([[ts]])

    Q = np.matrix([[45.0]])

    R = np.matrix([[100.0]])

    X = np.matrix(scipy.linalg.solve_discrete_are(A, B, Q, R))

    # compute the LQR gain
    K = np.matrix(scipy.linalg.inv(B.T * X * B + R) * (B.T * X * A))

    eigVals, eigVecs = scipy.linalg.eig(A - B * K)
    error = np.matrix([[theta_ref - theta]])
    input = np.dot(K, error)
    print "Rotate LQR"
    print input
    return input
