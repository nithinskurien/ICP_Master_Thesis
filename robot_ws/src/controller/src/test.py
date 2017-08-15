import numpy as np
import matplotlib.pyplot as plt
tra = []
vel = 0.1
t_s = 0.1
radius = 1
theta = np.arccos(1-((vel/t_s)**2/(2*radius**2)))

print int(360/theta)
for i in range(int(360/theta)-1):
    x = radius*np.cos(i*np.pi/180)
    y = radius*np.sin(i*np.pi/180)
    tra.append([x, y])
plt.figure()
print tra
# plt.plot(tra[:][0])
plt.show()