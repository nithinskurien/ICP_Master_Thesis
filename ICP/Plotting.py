import numpy as np
import Measurement as me
import Pdf
import Kalman
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


meas = me.Measurement()
X_int = np.matrix('1;1')
P_int = np.matrix('0 0;0 0')
X_f = np.matrix('1;1')
P_f = np.matrix('0 0;0 0')
P_fx = []
P_fy = []
X_r = np.matrix('1;1')
for i in range(100):
    X_k1, P_k1, Q = Kalman.prediction(X_int, P_int, i)
    Z_k = np.transpose(meas.vehicle(1, i))
    X, P, R = Kalman.update(X_k1, P_k1, Z_k, i)
    X_f = np.concatenate((X_f, X), 1)
    P_f = np.concatenate((P_f, P), 1)
    P_fx = np.append(P_fx, P.item(0, 0))
    P_fy = np.append(P_fy, P.item(1, 1))
    X_r = np.concatenate((X_r, np.matrix('1;1')), 1)
    X_int = X
    P_int = P
F_x = np.array(X_f[0][:]).flatten()
F_y = np.array(X_f[1][:]).flatten()
Z_x = np.array(meas.vehicle_w(1)[0]).flatten()
Z_y = np.array(meas.vehicle_w(1)[1]).flatten()
X_rx = np.array(X_r[0][:]).flatten()
X_ry = np.array(X_r[1][:]).flatten()


rmse_x = Kalman.rmse(F_x, X_rx)
rmse_y = Kalman.rmse(F_y, X_ry)

print rmse_x
print rmse_y

plt.figure(1)
plt.subplot(211)
plt.plot(F_x,'b', label='Kalman Filtered Output', linewidth=2.5, alpha=0.9, mec='b')
plt.plot(Z_x,'g', label='Measurement', linewidth=2.5, alpha=0.9)
plt.plot(Z_x,'g', label='Measurement', linewidth=2.5, alpha=0.9)
plt.grid(True)
plt.title(r'$ X-Position,\ \ Q = %s,\ R = %s$' %(Q.item(0, 0), R.item(0, 0)))
plt.xlabel('$Time$')
plt.ylabel('$X\ (m)$')
plt.legend()


plt.subplot(212)
plt.plot(F_y,'b', label='Kalman Filtered Output', linewidth=2.5, alpha=0.9, mec='b')
plt.plot(Z_y,'g', label='Measurement', linewidth=2.5, alpha=0.9)
plt.grid(True)
plt.title(r'$ Y-Position,\ \ Q = %s,\ R = %s$' %(Q.item(1, 1), R.item(1, 1)))
plt.xlabel('$Time$')
plt.ylabel('$Y\ (m)$')
plt.legend()

plt.figure(2)
ax = plt.subplot(211)
plt.plot(P_fx,'b', label='Covariance of Estimate X', linewidth=2.5, alpha=0.9, mec='b')
plt.grid(True)
plt.title(r'$ X-Position,\ \ Q = %s,\ R = %s$' %(Q.item(1, 1), R.item(1, 1)))
ax.text(0.95, 0.1, 'X-Position, RMSE = %s' %rmse_x, transform=ax.transAxes, ha='right', fontsize=16)
plt.xlabel('$Time$')
plt.ylabel('$Variance\ (m^2)$')
plt.legend()

ax = plt.subplot(212)
plt.plot(P_fy,'b', label='Covariance of Estimate Y', linewidth=2.5, alpha=0.9, mec='b')
plt.grid(True)
plt.title(r'$ Y-Position,\ \ Q = %s,\ R = %s$' %(Q.item(1, 1), R.item(1, 1)))
ax.text(0.95, 0.1, 'Y-Position, RMSE = %s' %rmse_y, transform=ax.transAxes, ha='right', fontsize=16)
plt.xlabel('$Time$')
plt.ylabel('$Variance\ (m^2)$')
plt.legend()

plt.figure(3)
plt.plot(F_x, F_y, 'bo', label='Kalman Estimates', linewidth=2.5, alpha=0.9, mec='b')
plt.plot(Z_x, Z_y, 'go', label='Measurement', linewidth=2.5, alpha=0.9, mec='b')
plt.grid(True)
plt.xlabel('$X\ (m)$')
plt.ylabel('$Y\ (m)$')
plt.legend()

Pdf.pdf(X_int, P_int)
plt.show()
