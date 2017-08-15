import numpy as np
from numpy.linalg import inv


class Distribution(object):

    def __init__(self, mu, cov):
        #self.mu = np.matrix(2, 1)
        #self.cov = np.matrix(2, 2)
        self.mu = mu
        self.cov = cov


    def get_mean(self):
        return self.mu

    def get_cov(self):
        return self.cov

    @staticmethod
    def pdf_product(a, b):
        """
        maybe get it to handle list of distributions as input!!!

        :param a:
        :param b:
        :return:
        """
        cov1 = a.get_cov()
        cov2 = b.get_cov()
        mean1 = a.get_mean()
        mean2 = b.get_mean()
        cov = np.dot(np.dot(cov1, cov2), inv(cov1 + cov2))
        mean = np.dot(inv(inv(cov1) + inv(cov2)), np.dot(inv(cov1), mean1) + np.dot(inv(cov2), mean2))
        c = Distribution(mean, cov)
        return c

    @staticmethod
    def pdf_sum(k, a, b):
        cov1 = a.get_cov()
        cov2 = b.get_cov()
        mean1 = k*a.get_mean()
        mean2 = b.get_mean()
        mean = mean1 + mean2
        cov = cov1 + cov2
        c = Distribution(mean, cov)
        return c
