import Measurement as me
import Distribution
import algorithm
import pickle
import matplotlib.pyplot as plt
import numpy as np



n_v = 2
n_f = 3

# THIS (ONCE)------------------------------------
# meas = me.Measurement(n_v, n_f, 1)

# OR THIS-------------------------------------

name = '2_3_16_16_1.pickle'
with open('/home/tomek/Desktop/ICP/Pickles/measurement' + name, 'rb') as input:
    meas = pickle.load(input)
var_veh1 = 0.000001
var_veh2 = 16
var_features = 0.000001
cov1 = [np.matrix([[var_veh1, 0], [0, var_veh1]]), np.matrix([[var_veh2, 0], [0, var_veh2]])]
cov2 = [[np.matrix([[var_features, 0], [0, var_features]]), np.matrix([[var_features, 0], [0, var_features]])],
        [np.matrix([[var_features, 0], [0, var_features]]), np.matrix([[var_features, 0], [0, var_features]])],
        [np.matrix([[var_features, 0], [0, var_features]]), np.matrix([[var_features, 0], [0, var_features]])]]
meas.update_noise(cov1, cov2) #remember this function is a little hard coded (all features same variance etc.)
# ----------------------------------------------------

plt.figure(2)
plt.plot(np.array(meas.mean_veh[0][0]).flatten(), np.array(meas.mean_veh[0][1]).flatten(), 'b',
         label='GNSS measurement')

plt.plot(np.array(meas.mean_veh[1][0]).flatten(), np.array(meas.mean_veh[1][1]).flatten(), 'b',
         label='GNSS measurement', fillstyle='full')




plt.show()
# BE CAREFUL to not destroy the nice measurements!!!!
with open('/home/tomek/Desktop/ICP/Pickles/measurement' + str(n_v) + '_' + str(n_f) + '_' + str(meas.vehicle(0, 0).get_cov()[0,0]) + '_' +
            str(meas.vehicle(1, 0).get_cov()[0, 0]) + '_' + str(meas.feature(0, 0, 0).get_cov()[0,0]) + '.pickle', 'wb') as output:
    pickle.dump(meas, output)
