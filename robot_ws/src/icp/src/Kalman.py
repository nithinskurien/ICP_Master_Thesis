import numpy as np
from numpy.linalg import inv

def prediction(X_k, P_k, t):

    A = np.matrix('1 0;0 1')
    Q = np.matrix('.001 0;0 .001')
    X_k1 = np.dot(A, X_k)
    P_k1 = np.dot(np.dot(A, P_k), np.transpose(A)) + Q

    return X_k1, P_k1, Q

def update(X_k1, P_k1, Z_k, t):

    H = np.matrix('1 0;0 1')
    R = np.matrix('.01 0;0 .01')
    Y_k = Z_k - np.dot(H, X_k1)
    S_k = np.dot(np.dot(H, P_k1), np.transpose(H)) + R
    K_k = np.dot(np.dot(P_k1, np.transpose(H)), inv(S_k))
    X = X_k1 + np.dot(K_k, Y_k)
    P = P_k1 - np.dot(np.dot(K_k, H), P_k1)

    return X, P, R

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())
