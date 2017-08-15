import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#read the pickle
name = '2_3_1_16_1000000000'
nameM = '2_3_1_16_1000000000'
N_mp = 2
with open('/home/tomek/TheTitans/ICP/Pickles/measurement'+nameM+'.pickle', 'rb') as input:
    meas = pickle.load(input)

with open('/home/tomek/TheTitans/ICP/Pickles/dataICP' + name + '_' + str(N_mp) + '.pickle', 'rb') as input:
    dataICP = pickle.load(input)

with open('/home/tomek/TheTitans/ICP/Pickles/dataKalman' + name + '.pickle', 'rb') as input:
    dataKalman = pickle.load(input)

fontprop = FontProperties()
fontprop.set_size('small')

pos_est0Kalman = dataKalman.get_veh_belief(0)
pos_updt0Kalman = dataKalman.get_updt_veh_belief(0)
pos_pred0Kalman = dataKalman.get_pred_veh_belief(0)
pos_est1Kalman = dataKalman.get_veh_belief(1)
pos_updt1Kalman = dataKalman.get_updt_veh_belief(1)
pos_pred1Kalman = dataKalman.get_pred_veh_belief(1)

pos_est0ICP = dataICP.get_veh_belief(0)
pos_updt0ICP = dataICP.get_updt_veh_belief(0)
pos_pred0ICP = dataICP.get_pred_veh_belief(0)
pos_est1ICP = dataICP.get_veh_belief(1)
pos_updt1ICP = dataICP.get_updt_veh_belief(1)
pos_pred1ICP = dataICP.get_pred_veh_belief(1)


veh1fig = plt.figure(35)
plt.plot(np.concatenate(([None], np.array(meas.mean_veh[0][0]).flatten()), axis=0),
         np.concatenate(([None], np.array(meas.mean_veh[0][1]).flatten()), axis=0), 'b',
         label='Actual trajectory', linewidth=2.5, alpha=0.7)
plt.plot(np.concatenate(([None], np.array(meas.meas_veh[0][0]).flatten()), axis=0),
         np.concatenate(([None], np.array(meas.meas_veh[0][1]).flatten()), axis = 0), 'ok',
         label='GNSS measurement', linewidth=0.5, alpha=0.8)
plt.plot(pos_est0Kalman[0], pos_est0Kalman[1], 'r', label='Position estimate Kalman', linewidth=2.5, alpha=0.9)
plt.plot(pos_est0ICP[0], pos_est0ICP[1], 'm', label='Position estimate ICP', linewidth=2.5, alpha=0.9)
# plt.plot(pos_updt0ICP[0], pos_updt0ICP[1], '--g', label='GNSS update ICP', linewidth=2)
# plt.plot(pos_pred0Kalman[0], pos_pred0Kalman[1], '--r', label='Predicted state', linewidth=2)

plt.grid(True)
plt.title('The simulated values for vehicle 1')
plt.xlabel('Position in x [m]')
plt.ylabel('Position in y [m]')
plt.legend(ncol= 2, prop=fontprop)
axes = plt.gca()
axes.set_ylim(axes.get_ylim()[0], axes.get_ylim()[0] + (axes.get_ylim()[1] - axes.get_ylim()[0])*1.15)

veh2fig = plt.figure(36)
plt.plot(np.concatenate(([None], np.array(meas.mean_veh[1][0]).flatten()), axis = 0),
         np.concatenate(([None], np.array(meas.mean_veh[1][1]).flatten()), axis = 0), 'b',
         label='Actual trajectory', linewidth=2.5, alpha=0.7)
plt.plot(np.concatenate(([None], np.array(meas.meas_veh[1][0]).flatten()), axis = 0),
         np.concatenate(([None], np.array(meas.meas_veh[1][1]).flatten()), axis = 0),'ok',
         label='GNSS measurement', linewidth=1.5, alpha=0.8, fillstyle=None)
plt.plot(pos_est1Kalman[0], pos_est1Kalman[1], 'r', label='Position estimate Kalman', linewidth=2.5, alpha=0.9)
plt.plot(pos_est1ICP[0], pos_est1ICP[1], 'm', label='Position estimate ICP', linewidth=2.5, alpha=0.9)
# plt.plot(pos_updt1ICP[0], pos_updt1ICP[1], '--g', label='GNSS update ICP', linewidth=2)
# plt.plot(pos_pred1Kalman[0], pos_pred1Kalman[1], '--r', label='Predicted state Kalman', linewidth=2)

plt.grid(True)
plt.title('The simulated values for vehicle 2')
plt.xlabel('Position in x [m]')
plt.ylabel('Position in y [m]')

plt.legend(ncol=2, prop=fontprop)
axes2 = plt.gca()
axes2.set_ylim([axes2.get_ylim()[0], axes2.get_ylim()[0] + (axes2.get_ylim()[1] - axes2.get_ylim()[0])*1.15])
plt.show()

veh1fig.savefig('/home/tomek/Desktop/ICP/Figures/trajectory2_veh1_' +name+ '_' + str(N_mp) + '.eps')
veh2fig.savefig('/home/tomek/Desktop/ICP/Figures/trajectory2_veh2_' +name+ '_' + str(N_mp) + '.eps')

