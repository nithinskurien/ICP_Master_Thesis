import numpy as np
import Distribution
import Measurement
"""
This class is the Model For Prediction for the next state
"""


class Vehicle(object):

    def __init__(self, id, nr_feat, init_pos_distr, var_init):
        """
        :param id: integer describing vehicle number
        :param pos_init: Initial position for example from a measurement.
        :param pos_cov_init: Initial covariance of the position estimate
        :param var_init: Process noise!!!
        :return:

        """
        self.id = id
        self.pos_belief = init_pos_distr
        self.var = var_init
        self.t_s = None
        self.A = np.matrix('1 0; 0 1')
        self.B = np.matrix('1 0; 0 1')
        self.Q = np.matrix([[self.var[0], 0],
                            [0, self.var[1]]])
        self.pred_pos_belief = None
        self.m_xg = [None for i in range(nr_feat)]
        self.m_gx = [None for i in range(nr_feat)]

    def predict(self, mu, c, t_s):
     #   self.mu = mu
        self.t_s = t_s
     #   self.c = c
        self.p_Mu = np.dot(self.A, self.mu)
        self.p_C = self.Q + np.dot(np.dot(self.A, self.c), self.A.transpose())
        return self.p_Mu, self.p_C

    def pred_msg(self):
        p_Mu = np.dot(self.A, self.pos_belief.get_mean())
        p_C = self.Q + np.dot(np.dot(self.A, self.pos_belief.get_cov()), self.A.transpose())
        msg = Distribution.Distribution(p_Mu, p_C)
        return msg

    def update_pos_belief(self, a):
        self.pos_belief = a

    def update_pred_pos_belief(self, a):
        self.pred_pos_belief = a

    #def measurement(self,t):

