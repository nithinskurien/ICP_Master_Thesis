import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#read the pickle

name = '2_1_16_16_1000001'
name2 = '2_2_16_16_1'
name3 = '2_3_16_16_1'
name4 = '2_4_16_16_1000001'
name5 = '2_5_16_16_1'

N_mp = 2
runs = 100

with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' + name + '_' + str(runs) + '_' + str(N_mp) + '.pickle', 'rb') as input:
    errorICP1 = pickle.load(input)
with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' + name2 + '_' + str(runs) + '_' + str(N_mp) + '.pickle',
          'rb') as input:
    errorICP2 = pickle.load(input)
with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' + name3 + '_' + str(runs) + '_' + str(N_mp) + '.pickle',
          'rb') as input:
    errorICP3 = pickle.load(input)
with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' + name4 + '_' + str(runs) + '_' + str(N_mp) + '.pickle', 'rb') as input:
    errorICP4 = pickle.load(input)

with open('/home/tomek/TheTitans/ICP/Pickles/errorKalman' + name + '_' + str(runs) + '.pickle', 'rb') as input:
    errorKalman = pickle.load(input)
# with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' + name5 + '_' + str(runs) +  '_' + str(N_mp) + '.pickle', 'rb') as input:
#     errorICP5 = pickle.load(input)


fontprop = FontProperties()
fontprop.set_size('small')

print np.shape(errorKalman[0])
print np.shape([range(0, 21)])
print np.shape(errorICP1[0])


errorPlot = plt.figure(1)
err1 = plt.subplot(211)
plt.plot(np.array(range(0, 21)), errorKalman[0], label='Error for Kalman filter')
plt.plot(np.array(range(0, 21)), errorICP1[0], label='Error for ICP (1 feature)')
plt.plot(np.array(range(0, 21)), errorICP2[0], label='Error for ICP (2 features)')
plt.plot(np.array(range(0, 21)), errorICP3[0], label='Error for ICP (3 features)')
plt.plot(np.array(range(0, 21)), errorICP4[0], label='Error for ICP (4 features)')
# plt.plot(np.array(range(0, 21)), errorICP5[0], label='Error for ICP (5 features)')
plt.grid(True)
plt.title('The mean errors for vehicle 1')
plt.xlabel('Time')
plt.ylabel('Error [m]')
plt.subplots_adjust(hspace=0.36)
err1.legend(ncol=2, prop=fontprop)
err1.set_ylim([err1.get_ylim()[0], err1.get_ylim()[0] + (err1.get_ylim()[1] - err1.get_ylim()[0])*1.0])
err2 = plt.subplot(212)
plt.plot(np.array(range(0, 21)), errorKalman[1], label='Error for Kalman filter')
plt.plot(np.array(range(0, 21)), errorICP1[1], label='Error for ICP (1 feature)')
plt.plot(np.array(range(0, 21)), errorICP2[1], label='Error for ICP (2 features)')
plt.plot(np.array(range(0, 21)), errorICP3[1], label='Error for ICP (3 features)')
plt.plot(np.array(range(0, 21)), errorICP4[1], label='Error for ICP (4 features)')
# plt.plot(np.array(range(0, 21)), errorICP5[1], label='Error for ICP (5 features)')
plt.grid(True)
plt.title('The mean errors for vehicle 2')
plt.xlabel('Time')
plt.ylabel('Error [m]')
plt.subplots_adjust(hspace=0.36)
err2.legend(ncol=2, prop=fontprop)
err2.set_ylim([err2.get_ylim()[0], err2.get_ylim()[0] + (err2.get_ylim()[1] - err2.get_ylim()[0])*1.0])
plt.show()
errorPlot.savefig('/home/tomek/TheTitans/ICP/Figures/errorComp_' + name + '_' + str(runs) + '_' + str(N_mp) + '.eps')