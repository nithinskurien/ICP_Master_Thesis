import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def pdf(mean, cov):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    p = cov[0, 1]/(np.sqrt(cov[0, 0])*np.sqrt(cov[1, 1]))
    print p
    X, Y = np.mgrid[mean[0, 0]-4*np.sqrt(cov[0, 0]):mean[0, 0]+4*np.sqrt(cov[0, 0]):(np.sqrt(cov[0, 0]))/5,
           mean[1, 0] - 4 * np.sqrt(cov[1, 1]):mean[1, 0] + 4 * np.sqrt(cov[1, 1]):(np.sqrt(cov[1, 1]))/5]
    const = 7/(44*np.sqrt(cov[0, 0])*np.sqrt(cov[1, 1])*np.sqrt(1-np.power(p, 2)))
    const2 = -0.5/(1-np.power(p, 2))

    print const
    Z = const * np.exp(const2 * ((np.power(X-mean[0, 0], 2)/cov[0, 0])
                  + (np.power(Y-mean[1, 0], 2)/cov[0, 0])-2*p*(X-mean[0, 0])
                 * (Y-mean[1, 0])/(np.sqrt(cov[0, 0])*np.sqrt(cov[1, 1]))))

    ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1, alpha=0.7, linewidth=0.17)
    plt.xlabel('$X\ (m)$')
    plt.ylabel('$Y\ (m)$')
    plt.title(r'$PDF\ \mu_x = %s,\ \mu_y = %s,\ \sigma_x^2 = %s,\ \sigma^2_{xy} = %s,\ \sigma_y^2 = %s$' %(mean[0, 0], mean[1, 0], cov[0, 0], cov[0, 1], cov[0, 0]))
    #plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    #plt.show()