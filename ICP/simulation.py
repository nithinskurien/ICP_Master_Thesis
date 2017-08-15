import Measurement as me
import Pdfproduct
import numpy as np
import Vehicle
import algorithm
import Distribution
import DataCollect
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import copy
import Kalman


if __name__ == '__main__':

    t_s = 0.5
    n_v = 2
    n_f = 4
    p1 = np.matrix('0; 0.75; 0; 0')
    p2 = np.matrix('0; -0.75; 0; 0')

    cov1 = np.matrix('0.0025 0 0 0; '
                     '0 0.0025 0 0; '
                     '0 0 0.0025 0; '
                     '0 0 0 0.0025')
    cov2 = np.matrix('0.0025 0 0 0; '
                     '0 0.0025 0 0; '
                     '0 0 0.0025 0; '
                     '0 0 0 0.0025')
    # p1 = np.matrix('1; 0; 0; 0')
    #
    # p2 = np.matrix('3; 2; 0; 0')
    # cov1 = np.matrix('25 0 0 0; '
    #                  '0 25 0 0; '
    #                  '0 0 25 0; '
    #                  '0 0 0 25')
    # cov2 = np.matrix('25 0 0 0; '
    #                  '0 25 0 0; '
    #                  '0 0 25 0; '
    #                  '0 0 0 25')

    init_veh_distr1mean = np.reshape(np.random.multivariate_normal(np.array(p1).flatten(), cov1, 1), [4, 1])
    init_veh_distr2mean = np.reshape(np.random.multivariate_normal(np.array(p2).flatten(), cov2, 1), [4, 1])

    init_veh_distr = [Distribution.Distribution(init_veh_distr1mean, cov1),
                        Distribution.Distribution(init_veh_distr2mean, cov2)]

    p3 = np.matrix('1; 1')
    cov3 = np.matrix('100 0; 0 100')

    p4 = np.matrix('1; 1')
    cov4 = np.matrix('5 0; 0 5')

    p5 = np.matrix('2; 2')
    cov5 = np.matrix('5 0; 0 5')

    p6 = np.matrix('0.5; 0.5')
    cov6 = np.matrix('5 0; 0 5')

    p7 = np.matrix('0.5; 0.5')
    cov7 = np.matrix('5 0; 0 5')

    init_feat_distr = [Distribution.Distribution(np.reshape(np.random.multivariate_normal(np.array(p3).flatten(), cov3, 1), [2, 1]),
                                                 cov3) for i in range(n_f)]

    q = 0.00001
    # q = 1
    var_init = [q, q]

    v = algorithm.init_veh(n_v, n_f, init_veh_distr, init_feat_distr, var_init)
    meas = me.Measurement(n_v, n_f, t_s, True)

    data = DataCollect.DataCollect(n_v, n_f)
    data.init(n_v, n_f, init_veh_distr, init_feat_distr[:n_f])
    v = algorithm.init_veh(n_v, n_f, init_veh_distr, init_feat_distr[:n_f], var_init)
    # meas.meas_fea[0][1][:, 10:25] = None

    algorithm.main_loop(v, meas, 1, t_s, data)

    fontprop = FontProperties()
    fontprop.set_size('small')
    #
    # plt.figure(1, figsize=(9, 5))
    # err1 = plt.subplot(211)
    # plt.plot(error[0][0, :], label='Square error in x')
    # plt.plot(error[0][1, :], label='Square error in y')
    # plt.plot(error_mean_distance[0], label='Mean distance error')
    # plt.title('The RMSE for vehicle 1')
    # plt.xlabel('Time')
    # plt.ylabel('RMSE [m]')
    # plt.subplots_adjust(hspace=0.36)
    # err1.legend(ncol=3, prop=fontprop)
    # err1.set_ylim([err1.get_ylim()[0], err1.get_ylim()[0] + (err1.get_ylim()[1] - err1.get_ylim()[0])*1.15])
    # err2 = plt.subplot(212)
    # plt.plot(error[1][0, :], label='Square error in x')
    # plt.plot(error[1][1, :], label='Square error in y')
    # plt.plot(error_mean_distance[1], label='Mean distance error')
    # plt.title('The RMSE for vehicle 2')
    # plt.xlabel('Time')
    # plt.ylabel('RMSE [m]')
    # plt.subplots_adjust(hspace=0.36)
    # err2.legend(ncol=3, prop=fontprop)
    # err2.set_ylim([err2.get_ylim()[0], err2.get_ylim()[0] + (err2.get_ylim()[1] - err2.get_ylim()[0])*1.15])
    #
    #
    #
    pos_est0 = data.get_veh_belief(0)
    pos_updt0 = data.get_updt_veh_belief(0)
    pos_pred0 = data.get_pred_veh_belief(0)
    pos_est1 = data.get_veh_belief(1)
    pos_updt1 = data.get_updt_veh_belief(1)
    pos_pred1 = data.get_pred_veh_belief(1)

    #
    #
    pos_est_param = ['r', 'Position estimate', 2.5, 0.9]
    meas_veh_param = ['ok', 'GNSS measurement', 0.5, 0.8]
    plt.figure(35)
    # veh1plot = plt.subplot(211)

    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[0][0]).flatten()), axis = 0), np.concatenate(([None], np.array(meas.meas_veh[0][1]).flatten()), axis = 0), 'ok',
             label='GNSS measurement', linewidth=0.5, alpha=0.8)
    plt.plot(pos_est0[0], pos_est0[1], pos_est_param[0], label=pos_est_param[1], linewidth=pos_est_param[2], alpha=pos_est_param[3])
    plt.plot(pos_updt0[0], pos_updt0[1], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred0[0], pos_pred0[1], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[0][0]).flatten()), axis=0), np.concatenate(([None], np.array(meas.mean_veh[0][1]).flatten()), axis=0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)

    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 1')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    # veh1plot.legend(ncol= 3, prop=fontprop)
    # veh1plot.set_ylim(veh1plot.get_ylim()[0], veh1plot.get_ylim()[0] + (veh1plot.get_ylim()[1] - veh1plot.get_ylim()[0])*1.4)
    # plt.subplots_adjust(hspace=0.36)

    # plt.subplot(212)
    #
    # plt.plot(pos_est0[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    # plt.plot(np.concatenate(([None], np.array(meas.meas_veh[0][1]).flatten()), axis=0), 'ok',
    #          label='GNSS measurement', fillstyle='full')
    # plt.plot(pos_updt0[1], '--g', label='GNSS update', linewidth=2)
    # plt.plot(pos_pred0[1], '--r', label='Predicted state', linewidth=2)
    # plt.plot(np.concatenate(([None], np.array(meas.mean_veh[0][1]).flatten()), axis=0), 'b',
    #          label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #
    # # plt.axis([0, 6, 0, 20])
    #
    # plt.grid(True)
    # plt.xlabel('Time [s]')
    # plt.ylabel('Position y [m]')

    plt.figure(36)
    # veh2plot = plt.subplot(211)
    plt.plot(pos_est1[0], pos_est1[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[1][0]).flatten()), axis = 0), np.concatenate(([None], np.array(meas.meas_veh[1][1]).flatten()), axis = 0), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8, fillstyle=None)
    plt.plot(pos_updt1[0], pos_updt1[1], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred1[0], pos_pred1[1], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[1][0]).flatten()), axis = 0), np.concatenate(([None], np.array(meas.mean_veh[1][1]).flatten()), axis = 0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 2')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')

    # veh2plot.legend(ncol=3, prop=fontprop)
    # veh2plot.set_ylim([veh2plot.get_ylim()[0], veh2plot.get_ylim()[0] + (veh2plot.get_ylim()[1] - veh2plot.get_ylim()[0])*1.4])
    #
    # plt.subplot(212)
    # plt.plot(pos_est1[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    # plt.plot(np.concatenate(([None], np.array(meas.meas_veh[1][1]).flatten()), axis = 0), 'ok',
    #          label='GNSS measurement', linewidth=1.5, alpha=0.8)
    # plt.plot(pos_updt1[1], '--g', label='GNSS update', linewidth=2)
    # plt.plot(pos_pred1[1], '--r', label='Predicted state', linewidth=2)
    # plt.plot(np.concatenate(([None], np.array(meas.mean_veh[1][1]).flatten()), axis = 0), 'b',
    #          label='Actual trajectory', linewidth=2.5, alpha=0.7)
    # #plt.axis([0, 6, 0, 20])
    # plt.grid(True)
    # plt.xlabel('Time [s]')
    # plt.ylabel('Position y [m]')
    # plt.subplots_adjust(hspace =

    plt.figure(37)
    plt.subplot
    plt.plot(data.get_feat_belief(0, 0)[0], 'r', label = 'x')
    plt.plot(data.get_feat_belief(0, 0)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(0, 1)[0], 'r',label = 'x')
    # plt.plot(data.get_feat_belief(0, 1)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(0, 2)[0], 'r',label = 'x')
    # plt.plot(data.get_feat_belief(0, 2)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(0, 3)[0], 'r', label = 'x')
    # plt.plot(data.get_feat_belief(0, 3)[1], 'b',label = 'y')

    # plt.plot(data.get_feat_belief(0, 1)[0], data.get_feat_belief(0, 1)[1])
    # plt.plot(data.get_feat_belief(0, 2)[0], data.get_feat_belief(0, 2)[1])
    plt.plot(data.get_feat_belief(1, 0)[0], 'r',label = 'x')
    plt.plot(data.get_feat_belief(1, 0)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(1, 1)[0], 'r',label = 'x')
    # plt.plot(data.get_feat_belief(1, 1)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(1, 2)[0], 'r',label = 'x')
    # plt.plot(data.get_feat_belief(1, 2)[1], 'b',label = 'y')
    # plt.plot(data.get_feat_belief(1, 3)[0], 'r',label = 'x')
    # plt.plot(data.get_feat_belief(1, 3)[1], 'b',label = 'y')

    # plt.plot(data.get_feat_belief(1, 1)[0] + 0.01, data.get_feat_belief(1, 1)[1])
    # plt.plot(data.get_feat_belief(1, 2)[0] + 0.01, data.get_feat_belief(1, 2)[1])

    plt.legend()
    plt.show()
