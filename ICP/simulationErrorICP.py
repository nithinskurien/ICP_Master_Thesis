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
import pickle


if __name__ == '__main__':
    N_mp = 2
    # T_s = 0.1
    n_v = 2
    n_f = 4
    p1 = np.matrix('1; 0; 0; 0')
    p2 = np.matrix('3; 2; 0; 0')

    # cov1 = np.matrix('4 0 0 0; '
    #                  '0 4 0 0; '
    #                  '0 0 2 0; '
    #                  '0 0 0 2')
    # cov2 = np.matrix('16 0 0 0; '
    #                  '0 16 0 0; '
    #                  '0 0 2 0; '
    #                  '0 0 0 2')

    cov1 = np.matrix('16 0 0 0; '
                     '0 16 0 0; '
                     '0 0 4 0; '
                     '0 0 0 4')
    cov2 = np.matrix('16 0 0 0; '
                     '0 16 0 0; '
                     '0 0 4 0; '
                     '0 0 0 4')




    p3 = np.matrix('1.0; 1.0')
    cov3 = np.matrix('10000 0; 0 10000')

    p4 = np.matrix('0.5; 0.5')
    cov4 = np.matrix('5 0; 0 5')

    p5 = np.matrix('0.5; 0.5')
    cov5 = np.matrix('5 0; 0 5')

    p6 = np.matrix('0.5; 0.5')
    cov6 = np.matrix('5 0; 0 5')

    p7 = np.matrix('0.5; 0.5')
    cov7 = np.matrix('5 0; 0 5')

    # init_feat_distr = [Distribution.Distribution(p3, cov3), Distribution.Distribution(p4, cov4),
    #                    Distribution.Distribution(p5, cov5), Distribution.Distribution(p6, cov6),
    #                    Distribution.Distribution(p7, cov7)]

    q = 1

    var_init = [q, q]
    runs = 100
    dataICP = [None for i in range(runs)]
    meas = [None for i in range(runs)]
    error_square = [[None for i in range(runs)] for j in range(n_v)]
    error_distance = [[None for i in range(runs)] for j in range(n_v)]
    error = [None for i in range(n_v)]
    error_mean_norm = [None for i in range(n_v)]

    for run in range(runs):
        print 'RUUUUUN FOREST RUUUUN' + str(run)
        init_veh_distr1mean = np.reshape(np.random.multivariate_normal(np.array(p1).flatten(), cov1, 1), [4, 1])
        init_veh_distr2mean = np.reshape(np.random.multivariate_normal(np.array(p2).flatten(), cov2, 1), [4, 1])

        init_veh_distr = [Distribution.Distribution(init_veh_distr1mean, cov1),
                          Distribution.Distribution(init_veh_distr2mean, cov2)]
        init_feat_distr = []
        for f in range(n_f):
            init_feat_distr_mean = np.reshape(np.random.multivariate_normal(np.array(p3).flatten(), cov3, 1), [2, 1])
            init_feat_distr.append(Distribution.Distribution(init_feat_distr_mean, cov3))

        meas[run] = me.Measurement(n_v, n_f, 1, False)
        dataICP[run] = DataCollect.DataCollect(n_v, n_f)
        dataICP[run].init(n_v, n_f, init_veh_distr, init_feat_distr[:n_f])
        v = algorithm.init_veh(n_v, n_f, init_veh_distr, init_feat_distr[:n_f], var_init)
        algorithm.main_loop(v, meas[run], N_mp, 1, dataICP[run])
        for k in range(n_v):
            error_square[k][run] = np.power(dataICP[run].get_veh_belief(k)[:2, :] - meas[run].mean_veh[k], 2)
            error_distance[k][run] = np.sum(error_square[k][run], axis = 0)
    for l in range(n_v):
        error[l] = np.sqrt(np.mean(error_square[l], axis = 0))
        error_mean_norm[l] = np.sqrt(np.mean(error_distance[l], axis = 0))

    with open('/home/tomek/TheTitans/ICP/Pickles/errorICP' +
              str(n_v) + '_' + str(n_f) + '_' + str(meas[0].vehicle(0, 0).get_cov()[0, 0]) + '_' +
              str(meas[0].vehicle(1, 0).get_cov()[0, 0]) + '_' + str(meas[0].feature(0, 0, 0).get_cov()[0, 0]) +
              '_' + str(runs) + '_' + str(N_mp) + '.pickle', 'wb') as output:
        pickle.dump(error_mean_norm, output)

    print error
    print error_mean_norm
    fontprop = FontProperties()
    fontprop.set_size('small')

    plt.figure(1, figsize=(9, 5))
    err1 = plt.subplot(211)
    plt.plot(error[0][0, :], label='Square error in x')
    plt.plot(error[0][1, :], label='Square error in y')
    plt.plot(error_mean_norm[0], label='Mean distance error')
    plt.title('The RMSE for vehicle 1')
    plt.xlabel('Time')
    plt.ylabel('RMSE [m]')
    plt.subplots_adjust(hspace=0.36)
    err1.legend(ncol=2, prop=fontprop)
    err1.set_ylim([err1.get_ylim()[0], err1.get_ylim()[0] + (err1.get_ylim()[1] - err1.get_ylim()[0])*1.2])
    err2 = plt.subplot(212)
    plt.plot(error[1][0, :], label='Square error in x')
    plt.plot(error[1][1, :], label='Square error in y')
    plt.plot(error_mean_norm[1], label='Mean distance error')
    plt.title('The RMSE for vehicle 2')
    plt.xlabel('Time')
    plt.ylabel('RMSE [m]')
    plt.subplots_adjust(hspace=0.36)
    err2.legend(ncol=2, prop=fontprop)
    err2.set_ylim([err2.get_ylim()[0], err2.get_ylim()[0] + (err2.get_ylim()[1] - err2.get_ylim()[0])*1.2])



    pos_est0 = dataICP[0].get_veh_belief(0)
    pos_updt0 = dataICP[0].get_updt_veh_belief(0)
    pos_pred0 = dataICP[0].get_pred_veh_belief(0)
    pos_est1 = dataICP[0].get_veh_belief(1)
    pos_updt1 = dataICP[0].get_updt_veh_belief(1)
    pos_pred1 = dataICP[0].get_pred_veh_belief(1)
    #
    # # plt.figure(2)
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[0][1]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_fea[2][0][1]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[0][0]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_fea[2][0][0]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # #
    # #
    # # plt.figure(3)
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[1][1]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].meas_fea[2][1][1]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[1][0]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].meas_fea[2][1][0]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # #
    # # plt.figure(4)
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[0][1]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].meas_fea[2][0][1]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[0][0]).flatten()), axis=0), 'b',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].meas_fea[2][0][0]).flatten()), axis=0), 'k',
    # #          label='GNSS measurement', fillstyle='full')
    # # plt.plot(np.concatenate(([None], np.array(meas[0].mean_veh[0][1]).flatten()), axis=0), 'b',
    # #          label='Actual trajectory', linewidth=2.5, alpha=0.7)
    # # plt.show()
    #
    #
    # # error0 = [Kalman.rmse(data[0].get_veh_belief(0)[0][1:], meas[0].mean_veh[0][0]), Kalman.rmse(data[0].get_veh_belief(0)[1][1:], meas[0].mean_veh[0][1])]
    # # errorP0 = [np.sqrt(v[0].pos_belief.get_cov()[0, 0]), np.sqrt(v[0].pos_belief.get_cov()[1, 1])]
    # # print error0
    # # print errorP0
    # # error0 = [Kalman.rmse(data[0].get_veh_belief(1)[0][1:], meas[0].mean_veh[1][0]), Kalman.rmse(data[0].get_veh_belief(1)[1][1:], meas[0].mean_veh[1][1])]
    # # errorP0 = [np.sqrt(v[1].pos_belief.get_cov()[0, 0]), np.sqrt(v[1].pos_belief.get_cov()[1, 1])]
    # # print error0
    # # print errorP0
    #
    pos_est_param = ['r', 'Position estimate', 2.5, 0.9]
    meas_veh_param = ['ok', 'GNSS measurement', 0.5, 0.8]
    plt.figure(35,figsize=(9, 5))
    veh1plot = plt.subplot(211)

    plt.plot( np.array(meas[0].meas_veh[0][0]).flatten(), 'ok',
             label='GNSS measurement', linewidth=0.5, alpha=0.8)
    plt.plot(pos_est0[0], pos_est_param[0], label=pos_est_param[1], linewidth=pos_est_param[2], alpha=pos_est_param[3])
    plt.plot(pos_updt0[0], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred0[0], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.array(meas[0].mean_veh[0][0]).flatten(), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)

    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 1')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    veh1plot.legend(ncol= 3, prop=fontprop)
    veh1plot.set_ylim(veh1plot.get_ylim()[0], veh1plot.get_ylim()[0] + (veh1plot.get_ylim()[1] - veh1plot.get_ylim()[0])*1.4)
    plt.subplots_adjust(hspace=0.36)

    plt.subplot(212)

    plt.plot(pos_est0[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas[0].meas_veh[0][1]).flatten(), 'ok',
             label='GNSS measurement', fillstyle='full')
    plt.plot(pos_updt0[1], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred0[1], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.array(meas[0].mean_veh[0][1]).flatten(), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)

    # plt.axis([0, 6, 0, 20])

    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')

    plt.figure(36,figsize=(9, 5))
    veh2plot = plt.subplot(211)
    plt.plot(pos_est1[0], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas[0].meas_veh[1][0]).flatten(), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8, fillstyle=None)
    plt.plot(pos_updt1[0], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred1[0], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.array(meas[0].mean_veh[1][0]).flatten(), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 2')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')

    veh2plot.legend(ncol=3, prop=fontprop)
    veh2plot.set_ylim([veh2plot.get_ylim()[0], veh2plot.get_ylim()[0] + (veh2plot.get_ylim()[1] - veh2plot.get_ylim()[0])*1.4])

    plt.subplot(212)
    plt.plot(pos_est1[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas[0].meas_veh[1][1]).flatten(), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8)
    plt.plot(pos_updt1[1], '--g', label='GNSS update', linewidth=2)
    plt.plot(pos_pred1[1], '--r', label='Predicted state', linewidth=2)
    plt.plot(np.array(meas[0].mean_veh[1][1]).flatten(), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')
    plt.subplots_adjust(hspace = 0.36)


    plt.show()
    # #
    # # # #v is now a list of objects of class vehicles, f list of objects of Feature and meas contains all the needed measurements
    # # # #following just checks if this shit works
    # # # print v[0].pos_belief.get_cov()
    # # # print v[0].pos_belief.get_mean()
    # # # print v[0].id
    # # # print v[1].pos_belief.get_cov()
    # # # print v[1].pos_belief.get_mean()
    # # # print f[0].pos_belief.get_mean()
    # # # print f[0].pos_belief.get_cov()
    # #
