import numpy as np
import Distribution

#SOME COMMENTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1. Need #V*#F (4 if 2 vehicles and 2 features) feature measurements
class MeasurementMixer(object):

    def __init__(self, n_v, n_f, mean_v, mean_f):
        self.var_uwb_sensor = np.matrix([[6.18e-4, 1.75e-4], [1.75e-4, 4.43e-4]])
        self.var_feature_sensor = 300*np.matrix([[2.0e-6, 0.82e-6], [0.82e-6, 2.0e-6]])
        self.var_veh = [np.matrix('0.1 0.0; 0.0 0.1'), np.matrix('0.0 0.0; 0.0 0.0')]
        self.var_fea = [[np.matrix('0.0 0.0; 0.0 0.0'), np.matrix('0.0 0.0; 0.0 0.0')]]
        self.mean_veh = [None for i in range(n_v)]
        self.meas_veh = [None for i in range(n_v)]
        self.mean_fea = [[None for i in range(n_v)] for j in range(n_f)]
        self.meas_fea = [[None for i in range(n_v)] for j in range(n_f)]

        # for i in range(n_v):
        #     for j in range(n_f):
        #         if mean_f[j][i][0] == 0.0 and mean_f[j][i][1] == 0.0:
        #             mean_f[j][i][0] = None
        #             mean_f[j][i][1] = None

        for i in range(n_v):
            self.meas_veh[i] = mean_v[i] + \
                             np.transpose(np.random.multivariate_normal([0, 0], self.var_veh[i], 1))

        for k in range(n_f):
            for l in range(n_v):
                self.meas_fea[k][l] = mean_f[k][l] + \
                                      np.transpose(np.random.multivariate_normal([0, 0], self.var_fea[k][l], 1))

    def vehicle(self, n, i):

        mu = self.meas_veh[n][:, 0].reshape(2, 1)
        cov = self.var_veh[n] + self.var_uwb_sensor
        out = Distribution.Distribution(mu, cov)
        #print "mean Vehicle" + str(mu)
        return out


    def feature(self, n, f, i):

        mu = self.meas_fea[f][n][:, 0]
        cov = self.var_fea[f][n] + self.var_feature_sensor
        if mu[0] == 0.0 and mu[1] == 0.0:
            return None
            print 'Feat meas returns None'
        else:
            out = Distribution.Distribution(mu, cov)
            # print "mean Feature" + str(mu)
            return out

