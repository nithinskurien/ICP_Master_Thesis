import Measurement as me
import Pdfproduct
import numpy as np
import Vehicle
import algorithm
import Distribution
import DataCollect
import matplotlib.pyplot as plt
import Kalman


if __name__ == '__main__':


    data = DataCollect.DataCollect(2, 1)
    count = 0
    T_s = 0.1
    n_v = 2
    p1 = np.matrix('1.01; 0.1')
    p2 = np.matrix('2.9; 1.9')
    cov1 = np.matrix('0.5 0; 0 0.5')
    cov2 = np.matrix('0.5 0; 0 0.5')
    init_veh_distr = [Distribution.Distribution(p1, cov1), Distribution.Distribution(p2, cov2)]

    p3 = np.matrix('0.5; 0.5')
    cov3 = np.matrix('5 0; 0 5')
    init_feat_distr = [Distribution.Distribution(p3, cov3)]

    data.init(2, 1, init_veh_distr, init_feat_distr)

    var_pos1 = 2
    var_pos2 = 2
    var_init = [[var_pos1, var_pos1], [var_pos2, var_pos2]]

    while count < 1000:
         meas = me.Measurement(2, 1)
         v = algorithm.init_veh(2, 1, init_veh_distr, var_init)
         f = algorithm.init_feat(1, 2, init_feat_distr)
         algorithm.main_loop(v, f, meas, 7, 1, data)
         ++count

    x_pos_est0, y_pos_est0 = data.get_veh_belief(0)
    x_pos_pred0, y_pos_pred0 = data.get_pred_veh_belief(0)
    x_pos_est1, y_pos_est1 = data.get_veh_belief(1)
    x_pos_pred1, y_pos_pred1 = data.get_pred_veh_belief(1)

    error0 = [Kalman.rmse(data.get_veh_belief(0)[0][1:], meas.mean_veh[0][0]), Kalman.rmse(data.get_veh_belief(0)[1][1:], meas.mean_veh[0][1])]
    errorP0 = [np.sqrt(v[0].pos_belief.get_cov()[0, 0]), np.sqrt(v[0].pos_belief.get_cov()[1, 1])]
    print error0
    print errorP0
    error0 = [Kalman.rmse(data.get_veh_belief(1)[0][1:], meas.mean_veh[1][0]), Kalman.rmse(data.get_veh_belief(1)[1][1:], meas.mean_veh[1][1])]
    errorP0 = [np.sqrt(v[1].pos_belief.get_cov()[0, 0]), np.sqrt(v[1].pos_belief.get_cov()[1, 1])]
    print error0
    print errorP0

    pos_est_param = ['r', 'Position estimate', 2.5, 0.9]
    meas_veh_param = ['ok', 'GNSS measurement', 0.5, 0.8]
    plt.figure(35)
    plt.subplot(211)
    plt.plot(x_pos_est0, pos_est_param[0], label=pos_est_param[1], linewidth=pos_est_param[2], alpha=pos_est_param[3])
    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[0][0]).flatten()), axis = 0), 'ok',
             label='GNSS measurement', linewidth=0.5, alpha=0.8)
    plt.plot(x_pos_pred0, '--g', label='Initial belief', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[0][0]).flatten()), axis = 0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 1')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    plt.legend()



    plt.subplot(212)
    plt.plot(y_pos_est0, 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[0][1]).flatten()), axis=0), 'ok',
             label='GNSS measurement', fillstyle='full')
    plt.plot(y_pos_pred0, '--g', label='Initial belief', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[0][1]).flatten()), axis=0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    # plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')
    plt.legend()

    plt.figure(36)
    plt.subplot(211)
    plt.plot(x_pos_est1, 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[1][0]).flatten()), axis = 0), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8, fillstyle=None)
    plt.plot(x_pos_pred1, '--g', label='Initial belief', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[1][0]).flatten()), axis = 0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 2')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    plt.legend()

    plt.subplot(212)
    plt.plot(y_pos_est1, 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.concatenate(([None], np.array(meas.meas_veh[1][1]).flatten()), axis = 0), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8)
    plt.plot(y_pos_pred1, '--g', label='Initial belief', linewidth=2)
    plt.plot(np.concatenate(([None], np.array(meas.mean_veh[1][1]).flatten()), axis = 0), 'b',
             label='Actual trajectory', linewidth=2.5, alpha=0.7)
    #plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')
    plt.legend()


    plt.show()

    # #v is now a list of objects of class vehicles, f list of objects of Feature and meas contains all the needed measurements
    # #following just checks if this shit works
    # print v[0].pos_belief.get_cov()
    # print v[0].pos_belief.get_mean()
    # print v[0].id
    # print v[1].pos_belief.get_cov()
    # print v[1].pos_belief.get_mean()
    # print f[0].pos_belief.get_mean()
    # print f[0].pos_belief.get_cov()

