# Script to generate linearised equation form for the Jacobian

import sympy as sp
import numpy as np
import scipy.linalg


@staticmethod
def calculate_matrices():
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    xd = sp.Symbol('xd')
    yd = sp.Symbol('yd')
    theta = sp.Symbol('theta')
    thetad = sp.Symbol('thetad')
    v = sp.Symbol('v')
    phi = sp.Symbol('phi')
    ts = sp.Symbol('ts')

    # The first state equation describing x in k
    f1 = sp.simplify(x + sp.cos(theta)*(v/phi)*sp.sin(phi*ts) - sp.sin(theta)*(v/phi)*(1-sp.cos(phi*ts)))
    f2 = v*sp.cos(theta)
    f3 = sp.simplify(y + sp.sin(theta)*(v/phi)*sp.sin(phi*ts) + sp.cos(theta)*(v/phi)*(1-sp.cos(phi*ts)))
    f4 = v*sp.sin(theta)
    f5 = theta + phi*ts
    f6 = phi
    A = [[None for i in range(6)] for j in range(6)]
    B = [[None for i in range(2)] for j in range(6)]
    f = [f1, f2, f3, f4, f5, f6]
    xvec = [x, xd, y, yd, theta, thetad]
    uvec = [v, phi]
    # A matrix calculations
    for i in range(len(f)):
        for j in range(len(xvec)):
            A[i][j] = sp.diff(sp.simplify(f[i]), xvec[j])
    print A

    for i in range(len(f)):
        for j in range(len(uvec)):
            B[i][j] = sp.diff(sp.simplify(f[i]), uvec[j])

    print B
    return A, B


#@staticmethod
#def calculate_LQR_gain():
x = 1
y = 2
theta = 30
v = yd/np.sin(theta)
phi = 0.5
ts = 0.1

A = np.matrix([[1, 0, (-v*np.cos(theta) + v*np.cos(phi*ts + theta))/phi],
      [0, 1, (-v*np.sin(theta) + v*np.sin(phi*ts + theta))/phi],
      [0, 0, 1]])

B =np.matrix([[(-np.sin(theta) + np.sin(phi*ts + theta))/phi, (ts*v*np.cos(phi*ts + theta) + x)/phi - (phi*x - v*np.sin(theta) + v*np.sin(phi*ts + theta))/phi**2],
     [(np.cos(theta) - np.cos(phi*ts + theta))/phi, (ts*v*np.sin(phi*ts + theta) + y)/phi - (phi*y + v*np.cos(theta) - v*np.cos(phi*ts + theta))/phi**2],
     [0, ts]])
Q = np.matrix([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]])
R = np.matrix([[1, 0],
               [0, 1]])
print A
print B



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
print K
print X
# return K, X, eigVals




