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


# def init_feat(n_f, nr_veh, init_pos_distr):
#     feat = []
#     for i in range(n_f):
#         feat_temp = Feature.Feature(i, nr_veh, init_pos_distr[i])
#         feat.append(feat_temp)
#     return feat


def init_belief(v, gnss_meas_distr, data, T_s): #happens every time iteration in ICP
    v.update_time_step(T_s)
    pred_msg = v.pred_msg() #mean and covariance from the prediction
    meas_msg = gnss_meas_distr[v.id]
    data.save_pred_veh(v.id, pred_msg)

    h_gnss = np.matrix('1 0 0 0; 0 1 0 0')

    rho_gnss = meas_msg.get_mean()
    r_gnss = meas_msg.get_cov()
    x_pred = pred_msg.get_mean()
    p_pred = pred_msg.get_cov()

    k = np.dot(p_pred, np.dot(np.transpose(h_gnss), np.linalg.inv(r_gnss + np.dot(np.dot(h_gnss, p_pred), np.transpose(h_gnss)))))
    x_update = x_pred + np.dot(k, (rho_gnss - np.dot(h_gnss, x_pred)))
    p_update = p_pred - np.dot(np.dot(k, h_gnss), p_pred)

    # x_update[0] = meas_msg.get_mean()[0]
    # x_update[1] = meas_msg.get_mean()[1]
     #mean and covariance of the measurement
    new_belief = Distribution.Distribution(x_update, p_update)
    # print 'update'
    # print new_belief.get_mean()
    # print new_belief.get_cov()
    v.update_updt_pos_belief(new_belief)
    data.save_updt_veh(v.id, v.updt_pos_belief)


def m_gf_calc(n, v, feat_meas_distr):
    for f_id in v.visible_feat:
        h_1 = np.matrix('1 0; 0 1')
        h_2 = np.matrix('-1 0 0 0; 0 -1 0 0')

        if n == 0:
            m_xg_prev = v.updt_pos_belief
        else:
            m_xg_prev = v.m_xg[f_id]

        meas_mu = feat_meas_distr[f_id][v.id].get_mean()
        meas_cov = feat_meas_distr[f_id][v.id].get_cov()
        m_xg_mu = m_xg_prev.get_mean()
        m_xg_cov = m_xg_prev.get_cov()

        v.feat[f_id].m_gf_covinv =   np.transpose(h_1)*np.linalg.inv(meas_cov + h_2*m_xg_cov*np.transpose(h_2))*h_1
        v.feat[f_id].m_gf_covinvmu = np.transpose(h_1)*np.linalg.inv(meas_cov + h_2*m_xg_cov*np.transpose(h_2))*(meas_mu-h_2*m_xg_mu)
        # print h_2*m_xg_cov*np.transpose(h_2)
        # print 'G to F'
        # print str(v.id) + ' ' + str(f_id)
        # print np.linalg.inv(h_1)*(meas_mu-h_2*m_xg_mu)
        # print np.linalg.inv(np.transpose(h_1)*np.linalg.inv(meas_cov + h_2*m_xg_cov*np.transpose(h_2))*h_1)

    # if n == 0:
    #     m_xg_prev = v.pred_pos_belief
    # else:
    #     m_xg_prev = v.m_xg[f.id]
    #
    # f.m_gf[v.id] = Distribution.Distribution.pdf_sum(1, m_xg_prev, feat_meas_distr[f.id][v.id])

def m_gx_calc(n, v, feat_meas_distr):
    for f_id in v.visible_feat:
        h_1 = np.matrix('1 0; 0 1')
        h_2 = np.matrix('-1 0 0 0; 0 -1 0 0')

        m_fg = v.feat[f_id].m_fg

        meas_mu = feat_meas_distr[f_id][v.id].get_mean()
        meas_cov = feat_meas_distr[f_id][v.id].get_cov()
        m_fg_mu = m_fg.get_mean()
        m_fg_cov = m_fg.get_cov()

        v.m_gx_covinv[f_id] =   np.transpose(h_2)*np.linalg.inv(meas_cov + h_1*m_fg_cov*np.transpose(h_1))*h_2
        v.m_gx_covinvmu[f_id] = np.transpose(h_2)*np.linalg.inv(meas_cov + h_1*m_fg_cov*np.transpose(h_1))*(meas_mu-h_1*m_fg_mu)
        # print 'G to X !!!!!!!!!!!!!!!!!!!!!!!'
        # print str(v.id) + ' ' + str(f_id)
        # print np.transpose(h_2)*np.linalg.inv(h_2*np.transpose(h_2))*(meas_mu-h_1*m_fg_mu)
        # print np.transpose(h_2)*np.linalg.inv(meas_cov + h_1*m_fg_cov*np.transpose(h_1))*h_2

    # if n == 0:
    #     m_fg_prev = f.pos_belief # or pos belief iterative?????
    # else:
    #     m_fg_prev = f.m_fg[v.id]
    # v.m_gx[f.id] = Distribution.Distribution.pdf_sum(-1, feat_meas_distr[f.id][v.id], m_fg_prev)




def consensus_fnc(veh):
    temp_covinv = [None for i in range(len(veh[0].feat))]
    temp_covinvmu = [None for i in range(len(veh[0].feat))]
    for v in veh:
        for f_id in v.visible_feat:
            if temp_covinv[f_id] is None:
                temp_covinv[f_id] = v.feat[f_id].m_gf_covinv
                temp_covinvmu[f_id] = v.feat[f_id].m_gf_covinvmu
            else:
                temp_covinv[f_id] = temp_covinv[f_id] + v.feat[f_id].m_gf_covinv
                temp_covinvmu[f_id] = temp_covinvmu[f_id] + v.feat[f_id].m_gf_covinvmu
    for v in veh:
        for f_id2 in v.visible_feat:
            consensus_cov = np.linalg.inv(temp_covinv[f_id2])
            consensus_mu = np.dot(consensus_cov, temp_covinvmu[f_id2])
            # print consensus_cov
            # print consensus_mu
            v.feat[f_id2].consensus = Distribution.Distribution(consensus_mu, consensus_cov)
            # print 'Consensus'
            # print consensus_mu
            # print consensus_cov




def update_feat_belief(veh, data):
    Q = np.matrix([[0.01, 0], [0, 0.01]])
    for v in veh:
        for f_id in v.visible_feat:
            pos_belief_prev = v.feat[f_id].pos_belief
            pos_belief_new = Distribution.Distribution(pos_belief_prev.get_mean(), pos_belief_prev.get_cov() + Q)
            v.feat[f_id].pos_belief = Distribution.Distribution.pdf_product(pos_belief_new, v.feat[f_id].consensus)
            # print 'Feat Belief'
            # print v.feat[f_id].pos_belief.get_mean()
            # print v.feat[f_id].pos_belief.get_cov()
        for f2 in v.feat:
            data.save_feat(v.id, f2.id, v.feat[f2.id].pos_belief)


def update_veh_belief(veh, data):
    for v in veh:
        temp_covinv = None
        temp_covinvmu = None

        for f_id in v.visible_feat:
            if temp_covinv is None:
                temp_covinv = v.m_gx_covinv[f_id]
                temp_covinvmu = v.m_gx_covinvmu[f_id]
            else:
                temp_covinv = temp_covinv + v.m_gx_covinv[f_id]
                temp_covinvmu = temp_covinvmu + v.m_gx_covinvmu[f_id]

        belief_cov = v.updt_pos_belief.get_cov()
        belief_mu = v.updt_pos_belief.get_mean()
        if temp_covinvmu is None and temp_covinv is None:
            temp_cov = belief_cov
            temp_mu = belief_mu
        else:
            temp_cov = np.linalg.inv(temp_covinv + np.linalg.inv(belief_cov))
            temp_mu = np.dot(temp_cov, (temp_covinvmu + np.dot(np.linalg.inv(belief_cov), belief_mu)))
        # print 'vehicle belief covariance'
        # print temp_mu
        # print temp_cov
        v.pos_belief = Distribution.Distribution(temp_mu, temp_cov)
        data.save_veh(v.id, v.pos_belief)
    # for v in veh:
    #     v.pos_belief = v.updt_pos_belief
    #     data.save_veh(v.id, v.pos_belief)

'''Check here too if everything is ok!!!!!!!! check where the pos_belief is updated!!!!! if it does not fuck up with update_feature_belief() n == n_mp'''
def m_fg_calc(veh):

    # for v in veh:
    #     temp_covinv = [None for i in range(len(veh[0].feat))]
    #     temp_covinvmu = [None for i in range(len(veh[0].feat))]
    #     for v2 in veh:
    #         if v.id != v2.id:
    #             for f_id2 in v2.visible_feat:
    #                 if temp_covinv[f_id2] is None:
    #                     temp_covinv[f_id2] = v2.feat[f_id2].m_gf_covinv
    #                     temp_covinvmu[f_id2] = v2.feat[f_id2].m_gf_covinvmu
    #                 else:
    #                     temp_covinv[f_id2] += v2.feat[f_id2].m_gf_covinv
    #                     temp_covinvmu[f_id2] += v2.feat[f_id2].m_gf_covinvmu
    #     for f_id in v.visible_feat:
    #         pos_belief_prev = v.feat[f_id].pos_belief
    #         belief_cov = pos_belief_prev.get_cov()
    #         belief_mu = pos_belief_prev.get_mean()
    #         if temp_covinv[f_id] is None and temp_covinvmu[f_id] is None:
    #             temp_cov = belief_cov
    #             temp_mu = belief_mu
    #         else:
    #             temp_cov = np.linalg.inv(temp_covinv[f_id] + np.linalg.inv(belief_cov))
    #             temp_mu = np.dot(temp_cov, (temp_covinvmu[f_id] + np.dot(np.linalg.inv(belief_cov),belief_mu)))
    #         v.feat[f_id].m_fg = Distribution.Distribution(temp_mu, temp_cov)


    # MAKE THE CONSENSUS BASED CALCULATIONS INSTEAD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    for v in veh:
        for f_id in v.visible_feat:
            pos_belief_prev = v.feat[f_id].pos_belief
            belief_cov = pos_belief_prev.get_cov()
            belief_mu = pos_belief_prev.get_mean()
            temp_cov = np.linalg.inv(np.linalg.inv(v.feat[f_id].consensus.get_cov()) + np.linalg.inv(belief_cov) - v.feat[f_id].m_gf_covinv)
            # print 'consensus' + str(v.feat[f_id].consensus.get_mean())
            # print 'consensusCov' + str(v.feat[f_id].consensus.get_cov())

            # print belief_cov
            # print v.feat[f_id].m_gf_covinvmu
            temp_mu = temp_cov * (np.linalg.inv(v.feat[f_id].consensus.get_cov())*v.feat[f_id].consensus.get_mean() + np.linalg.inv(belief_cov)*belief_mu - v.feat[f_id].m_gf_covinvmu)
            v.feat[f_id].m_fg = Distribution.Distribution(temp_mu, temp_cov)
            # print 'F to G'
            # print str(v.id) + ' ' + str(f_id)
            # print temp_mu
            # print temp_cov


'''Check here too if everything is ok!!!!!!!! check where the prediction is updated!!!!!'''
def m_xg_calc(veh):
    # for v in veh:
    #     temp_covinv = None
    #     temp_covinvmu = None
    #     pos_belief_prev = v.updt_pos_belief
    #     for f_id in v.visible_feat:
    #         for f_id2 in v.visible_feat:
    #             if f_id != f_id2:
    #                 if temp_covinv is None:
    #                     temp_covinv = v.m_gx_covinv[f_id2]
    #                     temp_covinvmu = v.m_gx_covinvmu[f_id2]
    #                 else:
    #                     temp_covinv += v.m_gx_covinv[f_id2]
    #                     temp_covinvmu += v.m_gx_covinvmu[f_id2]
    #
    #         belief_cov = pos_belief_prev.get_cov()
    #         belief_mu = pos_belief_prev.get_mean()
    #
    #         if temp_covinv is None and temp_covinvmu is None:
    #             temp_cov = belief_cov
    #             temp_mu = belief_mu
    #         else:
    #             temp_cov = np.linalg.inv(temp_covinv + np.linalg.inv(belief_cov))
    #             temp_mu = temp_cov*(temp_covinvmu + np.linalg.inv(belief_cov)*belief_mu)
    #
    #         v.m_xg[f_id] = Distribution.Distribution(temp_mu, temp_cov)

    for v in veh:
        pos_belief_prev = v.updt_pos_belief
        for f_id in v.visible_feat:
            temp_covinv = None
            temp_covinvmu = None
            for f_id2 in v.visible_feat:
                if f_id != f_id2:
                    if temp_covinv is None:
                        temp_covinv = v.m_gx_covinv[f_id2]
                        temp_covinvmu = v.m_gx_covinvmu[f_id2]
                    else:
                        temp_covinv = temp_covinv + v.m_gx_covinv[f_id2]
                        temp_covinvmu = temp_covinvmu + v.m_gx_covinvmu[f_id2]

            belief_cov = pos_belief_prev.get_cov()
            belief_mu = pos_belief_prev.get_mean()

            if temp_covinv is None and temp_covinvmu is None:
                temp_cov = belief_cov
                temp_mu = belief_mu
            else:
                temp_cov = np.linalg.inv(temp_covinv + np.linalg.inv(belief_cov))
                temp_mu = np.dot(temp_cov, (temp_covinvmu + np.dot(np.linalg.inv(belief_cov), belief_mu)))

            v.m_xg[f_id] = Distribution.Distribution(temp_mu, temp_cov)
            # print 'X to G'
            # print str(v.id) + ' ' + str(f_id)
            # print temp_mu
            # print temp_cov


def icp_time_step(veh, gnss_meas_distr, feat_meas_distr, n_mp, data, T_s):
    for v in veh:
        init_belief(v, gnss_meas_distr, data, T_s)
    for n in range(n_mp):
        #print("n " + str(n))
        for v in veh:
            m_gf_calc(n, v, feat_meas_distr)
        consensus_fnc(veh)
        m_fg_calc(veh)
        for v in veh:
            m_gx_calc(n, v, feat_meas_distr)
        m_xg_calc(veh)
    update_feat_belief(veh, data)
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




def main_loop(veh, meas, n_mp, T_s, data):
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
    feat_meas_distr = [[None for i in range(len(veh))] for j in range(len(veh[0].feat))]


    for t in range(1, T):
        print t
        for v in veh:
            v.visible_feat = []
            gnss_meas_distr[v.id] = meas.vehicle(v.id, t)
            for f in v.feat:
                if meas.feature(v.id, f.id,  t) is None:
                    v.reset_feature(f.id)
                else:
                    feat_meas_distr[f.id][v.id] = meas.feature(v.id, f.id,  t)
                    v.visible_feat.append(f.id)
        icp_time_step(veh, gnss_meas_distr, feat_meas_distr, n_mp, data, T_s)






