import numpy as np
import matplotlib.pyplot as plt
r = 0.5
delta_theta = r * 0.05
max = int(2 * np.pi/delta_theta)
quarter = int(2 * np.pi/delta_theta/4)

ang = np.linspace(delta_theta, int(2 * np.pi / delta_theta) * delta_theta, num=int(2 * np.pi / delta_theta))
x_circle = r * np.cos(np.pi / 2 - ang)
y_circle = r * np.sin(np.pi / 2 - ang)
print quarter
print max
print np.vstack((x_circle[quarter+1:quarter*2], y_circle[quarter+1:quarter*2]))
mean_veh = np.concatenate((np.vstack((np.linspace(0, -0.5, 10), np.full((1, 10), -0.75)[0])),
                                   np.vstack((-0.5 + x_circle[quarter*2+1:quarter*3], -0.25 + y_circle[quarter*2+1:quarter*3])),
                                   np.vstack((np.full((1, 10), -1.0)[0], np.linspace(-0.25, 0.25, 10))),
                                   np.vstack((-0.5 + x_circle[quarter*3 + 1:quarter * 4],
                                              0.25 + y_circle[quarter*3 + 1:quarter * 4])),
                                   np.vstack((np.linspace(-0.5, 0, 10), np.full((1, 10), 0.75)[0]))),
                                  axis=1)
plt.plot(mean_veh[0], mean_veh[1])
plt.show()
