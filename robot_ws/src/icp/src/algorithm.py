#
import Measurement as me
import Vehicle
import Distribution
import Feature
import time
import numpy as np
import Pdfproduct


def init_veh(n_v, nr_feat, init_pos_distr, var_init):
    veh = []
    for i in range(n_v):
        veh_temp = Vehicle.Vehicle(i, nr_feat, init_pos_distr[i], var_init[i])
        veh.append(veh_temp)
    return veh


def init_feat(n_f, nr_veh, init_pos_distr):
    feat = []
    for i in range(n_f):
        feat_temp = Feature.Feature(i, nr_veh, init_pos_distr[i])
        feat.append(feat_temp)
    return feat


def init_belief(v, gnss_meas_distr): #happens every time iteration in ICP
    pred_msg = v.pred_msg() #mean and covariance from the prediction
    meas_msg = gnss_meas_distr[v.id] #mean and covariance of the measurement
    new_belief = Distribution.Distribution.pdf_product(pred_msg, meas_msg)
    v.update_pred_pos_belief(new_belief)
    # Some save function?????????????


def m_gf_calc(n, f, v, feat_meas_distr):
    if n == 0:
        m_xg_prev = v.pred_pos_belief
    else:
        m_xg_prev = v.m_xg[f.id]
    f.m_gf[v.id] = Distribution.Distribution.pdf_sum(1, m_xg_prev, feat_meas_distr[f.id][v.id])


def m_gx_calc(n, f, v, feat_meas_distr):
    if n == 0:
        m_fg_prev = f.pos_belief # or pos belief iterative?????
    else:
        m_fg_prev = f.m_fg[v.id]
    v.m_gx[f.id] = Distribution.Distribution.pdf_sum(-1, feat_meas_distr[f.id][v.id], m_fg_prev)


def outgoing_g_calc(veh, feat, n, feat_meas_distr):
    for v in veh:
        for f in feat:
            m_gf_calc(n, f, v, feat_meas_distr)
            m_gx_calc(n, f, v, feat_meas_distr)


def consensus_fnc(feat, veh):
    for f in feat:
        consensus = Distribution.Distribution(None, None)
        for v in veh:
            if consensus.get_cov() is None:
                consensus = f.m_gf[v.id]
            else:
                consensus = Distribution.Distribution.pdf_product(consensus, f.m_gf[v.id])
    return consensus


def update_feat_belief(feat, consensus, data):
    for f in feat:
        pos_belief_prev = f.pos_belief
        f.pos_belief = Distribution.Distribution.pdf_product(pos_belief_prev, consensus)
        data.save_feat(f.id, f.pos_belief)

def update_veh_belief(veh, data):
    for v in veh:
        prod = Distribution.Distribution(None, None)
        for m in v.m_gx:
            if prod.get_cov() is None:
                prod = m
            else:
                prod = Distribution.Distribution.pdf_product(prod, m)

        v.pos_belief = Distribution.Distribution.pdf_product(prod, v.pred_pos_belief)
        data.save_veh(v.id, v.pos_belief)


'''Check here too if everything is ok!!!!!!!! check where the pos_belief is updated!!!!! if it does not fuck up with update_feature_belief() n == n_mp'''
def m_fg_calc(feat, veh):
    for f in feat:
        product = Distribution.Distribution(None, None)
        pos_belief_prev = f.pos_belief
        for v in veh:
            for v2 in veh:
                if product.get_mean() is None:
                    product = f.m_gf[v2.id]
                else:
                    if v.id != v2.id:
                        product = Distribution.Distribution.pdf_product(product, f.m_gf[v2.id])
            f.m_fg[v.id] = Distribution.Distribution.pdf_product(product, pos_belief_prev)


'''Check here too if everything is ok!!!!!!!! check where the prediction is updated!!!!!'''
def m_xg_calc(feat, veh):
    for v in veh:
        product = Distribution.Distribution(None, None)
        pos_belief_prev = v.pred_pos_belief
        for f in feat:
            for f2 in feat:
                if product.get_mean() is None:
                    product = v.m_gx[f2.id]
                else:
                    if f.id != f2.id:
                        product = Distribution.Distribution.pdf_product(product, v.m_gx[f2.id])
            v.m_xg[f.id] = Distribution.Distribution.pdf_product(product, pos_belief_prev)


def icp_time_step(veh, feat,  gnss_meas_distr, feat_meas_distr, n_mp, data):
    for v in veh:
        init_belief(v, gnss_meas_distr)
        data.save_pred_veh(v.id, v.pred_pos_belief)
    for n in range(n_mp):
        #print("n " + str(n))
        outgoing_g_calc(veh, feat, n, feat_meas_distr)
        consensus = consensus_fnc(feat, veh)
        m_fg_calc(feat, veh)
        m_xg_calc(feat, veh)

    update_feat_belief(feat, consensus, data)
    update_veh_belief(veh, data)



    '''
    print veh[0].pred_pos_belief.get_mean()
    print data.pred_veh_belief[0][t+1].get_mean()

    print veh[1].pred_pos_belief.get_mean()
    print data.pred_veh_belief[1][t + 1].get_mean()

    print veh[0].pos_belief.get_mean()
    print data.veh_belief[0][t + 1].get_mean()

    print veh[1].pos_belief.get_mean()
    print data.veh_belief[1][t + 1].get_mean()

    print feat[0].pos_belief.get_mean()
    print data.feat_belief[0][t + 1].get_mean()
    '''




def main_loop(veh, feat, meas, n_mp, T_s, data):
    """
    :param meas: an object of class Measurement
    :param veh: an array of object of class Vehicle
    :param feat: and array of objects of class feature
    :param N_mp: integer value specifying number of iterations in message passing algorithm
    :param T_s: Sample time, might be not needed... to calculate the real time in sim if T_s different from 1
    :return:
    """

    T = np.shape(meas.meas_veh[0])[1]
    gnss_meas_distr = [None for i in range(len(veh))]
    feat_meas_distr = [[None for i in range(len(veh))] for j in range(len(feat))]
    #print T
    for t in range(T):
        for v in veh:
            gnss_meas_distr[v.id] = meas.vehicle(v.id, t)
            for f in feat:
                feat_meas_distr[f.id][v.id] = meas.feature(v.id, f.id, t)


        #print("time " + str(t))
        icp_time_step(veh, feat, gnss_meas_distr, feat_meas_distr, n_mp, data)






