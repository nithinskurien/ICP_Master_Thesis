import numpy as np
import Distribution

#SOME COMMENTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1. Need #V*#F (4 if 2 vehicles and 2 features) feature measurements
class Measurement(object):

    def __init__(self, n_v, n_f, t_s):
        self.T = 21
        self.var_veh = [np.matrix('0.0004 0;0 0.0004'), np.matrix('0.1 0;0 0.1')]
        var_f = 2.0e-6
        cross_var_f = 82.0e-8
        self.var_fea = [[np.matrix([[var_f, cross_var_f], [cross_var_f, var_f]]) for i in range(n_v)] for j in range(n_f)]

        # self.fea_pos = [np.matrix('2;2'), np.matrix('1;1'), np.matrix('0;1'), np.matrix('1;0'), np.matrix('0;0')]
        self.fea_pos = [np.matrix('1; 1') for i in range(n_f)]
        self.p_var_veh = [np.matrix('0.01 0; 0 0.01'), np.matrix('0.01 0; 0 0.01')]
        # can be velocity or position variance depending on what we want
        self.mean_veh_init = [np.matrix('1;0'), np.matrix('3;2')]
        self.mean_veh_vel_init = [np.matrix('0;0'), np.matrix('0;0')]

        self.mean_veh = [None for i in range(n_v)]
        self.mean_veh_vel = [None for i in range(n_v)]
        self.meas_veh = [None for i in range(n_v)]
        self.mean_fea = [[None for i in range(n_v)] for j in range(n_f)]
        self.meas_fea = [[None for i in range(n_v)] for j in range(n_f)]

        for i in range(n_v):
            self.mean_veh_vel[i] = np.empty([2, self.T])
            self.mean_veh[i] = np.empty([2, self.T])
            self.mean_veh[i][:, 0] = np.transpose(self.mean_veh_init[i])
            self.mean_veh_vel[i][:, 0] = np.transpose(self.mean_veh_vel_init[i])
            for j in range(1, self.T):
                self.mean_veh_vel[i][:, j] = self.mean_veh_vel[i][:, j - 1] + \
                                  np.random.multivariate_normal([0, 0], self.p_var_veh[i], 1)
                self.mean_veh[i][:, j] = self.mean_veh[i][:, j-1] + self.mean_veh_vel[i][:, j - 1]*t_s
            self.meas_veh[i] = self.mean_veh[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], self.T))

        for k in range(n_f):
            for l in range(n_v):
                self.mean_fea[k][l] = self.fea_pos[k] - self.mean_veh[l]
                self.meas_fea[k][l] = self.mean_fea[k][l] + \
                                      np.transpose(np.random.multivariate_normal([0, 0], self.var_fea[k][l], self.T))

    def update_noise(self, var_vehicles, var_features): #REMEMBER IT IS A BIT HARD CODED

        for i in range(np.shape(self.mean_veh)[0]):
            self.var_veh[i] = var_vehicles[i]
            self.meas_veh[i] = self.mean_veh[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], self.T))

        for k in range(np.shape(self.mean_fea)[0]):
            for l in range(np.shape(self.mean_fea)[1]):
                self.var_fea[k][l] = var_features[k][l]
                self.mean_fea[k][l] = self.mean_veh[l] - self.fea_pos[k]
                self.meas_fea[k][l] = self.mean_fea[k][l] + \
                                      np.transpose(np.random.multivariate_normal([0, 0], self.var_fea[k][l], self.T))


    def vehicle(self, n, t):

        mu = self.meas_veh[n][:, t].reshape(2, 1)
        cov = self.var_veh[n]
        out = Distribution.Distribution(mu, cov)
        return out


    def feature(self, n, f, t):
        mu = self.meas_fea[f][n][:, t]
        cov = self.var_fea[f][n]
        if mu[0] != mu[0]:
            return None
        else:
            out = Distribution.Distribution(mu, cov)
            return out

