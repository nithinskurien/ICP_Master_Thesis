# Kalman Filter for the Robot
import numpy as np
from numpy.linalg import inv

def prediction(X_k, P_k, v, phi, ts):    # Kalman Position Prediction step according to the linearised model

    x = X_k.item(0)
    y = X_k.item(1)
    theta = euler0to360(X_k.item(2))
    A = np.matrix([[1, 0, 0], # (-v * np.cos(theta) + v * np.cos(phi * ts + theta)) / phi],
                   [0, 1, 0], # (-v * np.sin(theta) + v * np.sin(phi * ts + theta)) / phi],
                   [0, 0, 1]])

    B = np.matrix([[(-np.sin(theta) + np.sin(phi*ts + theta))/phi,
        (ts*v*np.cos(phi*ts + theta) + x)/phi - (phi*x - v*np.sin(theta) + v*np.sin(phi*ts + theta))/phi**2],
        [(np.cos(theta) - np.cos(phi*ts + theta))/phi,
        (ts*v*np.sin(phi*ts + theta) + y)/phi - (phi*y + v*np.cos(theta) - v*np.cos(phi*ts + theta))/phi**2], [0, ts]])

    Q = np.matrix([[8.0e-7, 0, 0],
                   [0, 8.0e-7, 0],
                   [0, 0, 1.0e-7]])

    input = np.matrix([[v], [phi]])

    X_k1 = np.dot(A, X_k) + np.dot(B, input)
    # print "Prediction :"
    # print X_k1
    P_k1 = np.dot(np.dot(A, P_k), np.transpose(A)) + Q

    return X_k1, P_k1

# def prediction_linear_velocity(X_k, P_k, v, phi, ts):
#
#     A = np.matrix([[1, 0, 0], # (-v * np.cos(theta) + v * np.cos(phi * ts + theta)) / phi],
#                    [0, 1, 0], # (-v * np.sin(theta) + v * np.sin(phi * ts + theta)) / phi],
#                    [0, 0, 1]])


def update(X_k1, P_k1, Z_k):    # Kalman Position measurement update step

    H = np.matrix('1 0 0; 0 1 0')
    R = np.matrix([[6.18e-4, 1.75e-4], [1.75e-4, 4.43e-4]])
    Y_k = Z_k - np.dot(H, X_k1)
    S_k = np.dot(np.dot(H, P_k1), np.transpose(H)) + R
    K_k = np.dot(np.dot(P_k1, np.transpose(H)), inv(S_k))
    X = X_k1 + np.dot(K_k, Y_k)
    P = P_k1 - np.dot(np.dot(K_k, H), P_k1)
    return X, P

def update_theta(X_k1, P_k1, Z_k, var_theta):    # Kalman Angle measurement update step
    H = np.matrix('0 0 1')
    R = np.matrix([[var_theta]])
    Y_k = Z_k - np.dot(H, X_k1)
    S_k = np.dot(np.dot(H, P_k1), np.transpose(H)) + R
    K_k = np.dot(np.dot(P_k1, np.transpose(H)), inv(S_k))
    X = X_k1 + np.dot(K_k, Y_k)
    P = P_k1 - np.dot(np.dot(K_k, H), P_k1)
    return X, P

def euler0to360(angle):   # Changing angle range from -pi to pi to 0 to 2Pi

    if angle < 0:
        angle = angle + 2 * np.pi
    if angle > 2 * np.pi:
        angle = angle - 2 * np.pi
    else:
        return angle

