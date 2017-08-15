#
import Measurement as me
import Vehicle
import Distribution
import Feature
import time
import numpy as np
import Pdfproduct


def init_veh(n_v, nr_feat, init_pos_distr, init_feat_distr, var_init):
    veh = []
    for i in range(n_v):
        veh_temp = Vehicle.Vehicle(i, nr_feat, init_pos_distr[i], init_feat_distr, var_init[i])
        veh.append(veh_temp)
    return veh


def init_feat(n_f, nr_veh, init_pos_distr):
    feat = []
    for i in range(n_f):
        feat_temp = Feature.Feature(i, nr_veh, init_pos_distr[i])
        feat.append(feat_temp)
    return feat


def init_belief(v, gnss_meas_distr, data): #happens every time iteration in ICP
    pred_msg = v.pred_msg() #mean and covariance from the prediction
    meas_msg = gnss_meas_distr[v.id]
    data.save_pred_veh(v.id, pred_msg)

    h_gnss = np.matrix('1 0 0 0; 0 1 0 0')

    rho_gnss = meas_msg.get_mean()
    r_gnss = meas_msg.get_cov()
    x_pred = pred_msg.get_mean()
    p_pred = pred_msg.get_cov()

    k = p_pred*np.transpose(h_gnss)*np.linalg.inv(r_gnss + h_gnss*p_pred*np.transpose(h_gnss))
    x_update = x_pred + k*(rho_gnss - h_gnss*x_pred)
    p_update = p_pred - k*h_gnss*p_pred
     #mean and covariance of the measurement
    new_belief = Distribution.Distribution(x_update, p_update)
    v.update_updt_pos_belief(new_belief)
    data.save_updt_veh(v.id, v.updt_pos_belief)
    # Some save function?????????????


def update_veh_belief(veh, data):
    for v in veh:
        v.update_pos_belief(v.updt_pos_belief)
        data.save_veh(v.id, v.pos_belief)


def time_step(veh, gnss_meas_distr, data):
    for v in veh:
        init_belief(v, gnss_meas_distr, data)
    update_veh_belief(veh, data)


def main_loop(veh, meas, T_s, data):
    """
    :param meas: an object of class Measurement
    :param veh: an array of object of class Vehicle
    :param T_s: Sample time, might be not needed... to calculate the real time in sim if T_s different from 1
    :return:
    """

    T = np.shape(meas.meas_veh[0])[1]
    gnss_meas_distr = [None for i in range(len(veh))]

    print T
    for t in range(1, T):
        for v in veh:
            gnss_meas_distr[v.id] = meas.vehicle(v.id, t)
        print("time " + str(t))
        time_step(veh, gnss_meas_distr, data)






