import numpy as np
import Distribution

#SOME COMMENTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1. Need #V*#F (4 if 2 vehicles and 2 features) feature measurements
class Measurement(object):

    def __init__(self, n_v, n_f, t_s, defined):
        self.T = 21
        self.var_veh = [np.matrix('0.01 0;0 0.01'), np.matrix('0.0001 0;0 0.0001')]
        var_f = 0.0001
        cross_var_f = 0
        self.fea_pos = [np.matrix('1; 1') for i in range(n_f)]
        self.var_fea = [[np.matrix([[var_f, cross_var_f], [cross_var_f, var_f]]) for i in range(n_v)] for j in range(n_f)]
        self.mean_veh = [None for i in range(n_v)]
        self.mean_veh_vel = [None for i in range(n_v)]
        self.meas_veh = [None for i in range(n_v)]
        self.mean_fea = [[None for i in range(n_v)] for j in range(n_f)]
        self.meas_fea = [[None for i in range(n_v)] for j in range(n_f)]

        if defined:
            r = 0.5
            delta_theta = r * 0.05
            max = int(2 * np.pi / delta_theta)
            quarter = int(2 * np.pi / delta_theta / 4)
            ang = np.linspace(delta_theta, int(2 * np.pi / delta_theta) * delta_theta, num=int(2 * np.pi / delta_theta))
            x_circle = r * np.cos(np.pi / 2 - ang)
            y_circle = r * np.sin(np.pi / 2 - ang)



            self.mean_veh[0] = np.concatenate((np.vstack((np.linspace(0, 0.5, 10), np.full((1, 10), 0.75)[0])),
                                               np.vstack((0.5 + x_circle[1:quarter], 0.25 + y_circle[1:quarter])),
                                               np.vstack((np.full((1, 10), 1.0)[0], np.linspace(0.25, -0.25, 10))),
                                               np.vstack((0.5 + x_circle[quarter+1:quarter*2],
                                                          -0.25 +y_circle[quarter+1:quarter*2])),
                                               np.vstack((np.linspace(0.5, 0, 10), np.full((1, 10), -0.75)[0]))), axis = 1)
            self.mean_veh[1] = np.concatenate((np.vstack((np.linspace(0, -0.5, 10), np.full((1, 10), -0.75)[0])),
                                   np.vstack((-0.5 + x_circle[quarter*2+1:quarter*3], -0.25 + y_circle[quarter*2+1:quarter*3])),
                                   np.vstack((np.full((1, 10), -1.0)[0], np.linspace(-0.25, 0.25, 10))),
                                   np.vstack((-0.5 + x_circle[quarter*3 + 1:quarter * 4],
                                              0.25 + y_circle[quarter*3 + 1:quarter * 4])),
                                   np.vstack((np.linspace(-0.5, 0, 10), np.full((1, 10), 0.75)[0]))),
                                  axis=1)

        else:
            # self.fea_pos = [np.matrix('2;2'), np.matrix('1;1'), np.matrix('0;1'), np.matrix('1;0'), np.matrix('0;0')]
            self.p_var_veh = [np.matrix('1 0; 0 1'), np.matrix('1 0; 0 1')]
            # can be velocity or position variance depending on what we want
            self.mean_veh_init = [np.matrix('1;0'), np.matrix('3;2')]
            self.mean_veh_vel_init = [np.matrix('0;0'), np.matrix('0;0')]

            for i in range(n_v):
                self.mean_veh_vel[i] = np.empty([2, self.T])
                self.mean_veh[i] = np.empty([2, self.T])
                self.mean_veh[i][:, 0] = np.transpose(self.mean_veh_init[i])
                self.mean_veh_vel[i][:, 0] = np.transpose(self.mean_veh_vel_init[i])
                for j in range(1, self.T):
                    self.mean_veh_vel[i][:, j] = self.mean_veh_vel[i][:, j - 1] + \
                                      np.random.multivariate_normal([0, 0], self.p_var_veh[i], 1)
                    self.mean_veh[i][:, j] = self.mean_veh[i][:, j-1] + self.mean_veh_vel[i][:, j - 1]*t_s

        for i in range(n_v):
            print 'legth' +str(len(self.mean_veh[i][0]))
            print np.shape(self.mean_veh[i])
            print np.shape(self.meas_veh[i])
            print np.shape(np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], len(self.mean_veh[i][0]))))
            self.meas_veh[i] = self.mean_veh[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], len(self.mean_veh[i][0])))

        for k in range(n_f):
            for l in range(n_v):
                self.mean_fea[k][l] = self.fea_pos[k] - self.mean_veh[l]
                self.meas_fea[k][l] = self.mean_fea[k][l] + \
                                      np.transpose(np.random.multivariate_normal([0, 0], self.var_fea[k][l], len(self.mean_veh[l][0])))

    def update_noise(self, var_vehicles, var_features): #REMEMBER IT IS A BIT HARD CODED

        for i in range(np.shape(self.mean_veh)[0]):
            self.var_veh[i] = var_vehicles[i]
            self.meas_veh[i] = self.mean_veh[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], len(self.mean_veh[i][0])))

        for k in range(np.shape(self.mean_fea)[0]):
            for l in range(np.shape(self.mean_fea)[1]):
                self.var_fea[k][l] = var_features[k][l]
                self.mean_fea[k][l] = self.fea_pos[k] - self.mean_veh[l]
                self.meas_fea[k][l] = self.mean_fea[k][l] + \
                                      np.transpose(np.random.multivariate_normal([0, 0], self.var_fea[k][l], len(self.mean_fea[k][l][0])))


    def vehicle(self, n, t):

        mu = self.meas_veh[n][:, t].reshape(2, 1)
        cov = self.var_veh[n]
        out = Distribution.Distribution(mu, cov)
        return out


    def feature(self, n, f, t):
        mu = self.meas_fea[f][n][:, t]
        cov = self.var_fea[f][n] # + np.matrix([[1000000, 0], [0, 1000000]])
        if mu[0] != mu[0]:
            return None
        else:
            out = Distribution.Distribution(mu, cov)
            return out

