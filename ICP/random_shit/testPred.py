import numpy as np
theta = 0.69
phi = 0.5
v = 1
ts = 0.1
x = 1.4
y = -0.20

# A = np.matrix([[1, 0, (-v*np.cos(theta) + v*np.cos(phi*ts + theta))/phi],
#       [0, 1, (-v*np.sin(theta) + v*np.sin(phi*ts + theta))/phi],
#       [0, 0, 1]])
A=np.matrix([[1, 0, -v*(-np.cos(phi*ts) + 1)*np.cos(theta)/phi - v*np.sin(theta)*np.sin(phi*ts)/phi],
             [0, 1, -v*(-np.cos(phi*ts) + 1)*np.sin(theta)/phi + v*np.sin(phi*ts)*np.cos(theta)/phi],
             [0, 0, 1]])
f1 = x + np.cos(theta)*(v/phi)*np.sin(phi*ts) - np.sin(theta)*(v/phi)*(1-np.cos(phi*ts))
f3 = y + np.sin(theta)*(v/phi)*np.sin(phi*ts) + np.cos(theta)*(v/phi)*(1-np.cos(phi*ts))

B =np.matrix([[(-np.sin(theta) + np.sin(phi*ts + theta))/phi,
   (ts*v*np.cos(phi*ts + theta) + x)/phi - (phi*x - v*np.sin(theta) + v*np.sin(phi*ts + theta))/phi**2],
   [(np.cos(theta) - np.cos(phi*ts + theta))/phi,
   (ts*v*np.sin(phi*ts + theta) + y)/phi - (phi*y + v*np.cos(theta) - v*np.cos(phi*ts + theta))/phi**2], [0, ts]])
X = np.matrix([[x],[y],[theta]])
U = np.matrix([[v],[phi]])

print f1,f3

print np.dot(A,X) + np.dot(B,U)