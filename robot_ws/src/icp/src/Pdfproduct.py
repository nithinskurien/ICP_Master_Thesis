import numpy as np
from numpy.linalg import inv

def product(mean1, mean2, var1, var2):
    """
    :param mean1: Mean of First PDF
    :param mean2: Mean of Second PDF
    :param var1:  Variance of First PDF
    :param var2: Variance of Second PDF
    :return: the mean and variance of the product

    """

    var = np.dot(np.dot(var1, var2), inv(var1 + var2))
    mean = np.dot(inv(inv(var1) + inv(var2)), np.dot(inv(var1), mean1) + np.dot(inv(var2), mean2))
    #Don't think we should use dot product here, try np.matmul instead

    return mean, var
'''
    var = var1*var2*inv(var1 + var2)
    mean = inv(inv(var1) + inv(var2)) * inv(var1)* mean1 + inv(var2)* mean2
'''

