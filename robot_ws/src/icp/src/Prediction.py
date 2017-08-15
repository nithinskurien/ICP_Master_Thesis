import numpy as np



"""
This class is the Model For Prediction for the next state
"""


class Prediction(object):

    def __init__(self):
        self.mu = None
        self.var = .001
        self.t_s = None
        self.A = np.matrix('1 0; 0 1')
        self.B = np.matrix('1 0; 0 1')
        self.Q = np.matrix([[self.var, 0], [0, self.var]])
        self.c = None
        self.p_Mu = None
        self.p_C = None

    def predict(self, mu, c, t_s):
        self.mu = mu
        self.t_s = t_s
        self.c = c
        self.p_Mu = np.dot(self.A, self.mu)
        self.p_C = self.Q + np.dot(np.dot(self.A, self.c), self.A.transpose())

        return self.p_Mu, self.p_C

