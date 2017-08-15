import numpy as np
import Distribution

#SOME COMMENTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1. Need #V*#F (4 if 2 vehicles and 2 features) feature measurements
class Measurement(object):

    def __init__(self, n_v, n_f):
        self.T = 200
        self.var_veh = [np.matrix('1 0;0 1'), np.matrix('9 0;0 9')]
        self.var_fea = [[np.matrix('0.5 0;0 0.5'), np.matrix('0.5 0;0 0.5')]]

        self.fea_pos = [np.matrix('2;2')]

        self.p_var_veh = [np.matrix('2 0;0 2'), np.matrix('2 0;0 2')]
        self.mean_veh_init = [np.matrix('1;0'), np.matrix('3;2')]

        self.mean_veh = [None for i in range(n_v)]
        self.meas_veh = [None for i in range(n_v)]
        self.mean_fea = [[None for i in range(n_v)] for j in range(n_f)]
        self.meas_fea = [[None for i in range(n_v)] for j in range(n_f)]

        for i in range(n_v):
            self.mean_veh[i] = np.empty([2, self.T])
            self.mean_veh[i][:, 0] = np.transpose(self.mean_veh_init[i])
            for j in range(1, self.T):
                self.mean_veh[i][:, j] = self.mean_veh[i][:, j - 1] + \
                                  np.random.multivariate_normal([0, 0], self.p_var_veh[i], 1)
            self.meas_veh[i] = self.mean_veh[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], self.T))

        for k in range(n_f):
            for l in range(n_v):
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
        out = Distribution.Distribution(-mu, cov)
        return out

