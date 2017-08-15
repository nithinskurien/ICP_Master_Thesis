import Measurement as me
import Pdfproduct
import numpy as np
import Vehicle
import algorithm
import Distribution
import DataCollect
import matplotlib.pyplot as plt
import copy
import Kalman

def Print(meas, data):

    pos_est0 = data.get_veh_belief(0)[-1]
    pos_updt0 = data.get_updt_veh_belief(0)[-1]
    pos_pred0 = data.get_pred_veh_belief(0)[-1]
    pos_est1 = data.get_veh_belief(1)[-1]
    pos_updt1 = data.get_updt_veh_belief(1)[-1]
    pos_pred1 = data.get_pred_veh_belief(1)[-1]

    pos_est_param = ['r', 'Position estimate', 2.5, 0.9]
    meas_veh_param = ['ok', 'GNSS measurement', 0.5, 0.8]
    plt.figure(35)
    plt.subplot(211)

    plt.plot(np.array(meas.meas_veh[0][0]).flatten(), 'ok',
             label='GNSS measurement', linewidth=0.5, alpha=0.8)
    plt.plot(pos_est0[0], pos_est_param[0], label=pos_est_param[1], linewidth=pos_est_param[2], alpha=pos_est_param[3])
    plt.plot(pos_updt0[0], '--g', label='Initial belief', linewidth=2)
    plt.plot(pos_pred0[0], '--r', label='Initial belief', linewidth=2)

    # plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 1')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    plt.legend()

    plt.subplot(212)

    plt.plot(pos_est0[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas.meas_veh[0][1]).flatten(), 'ok',
             label='GNSS measurement')
    plt.plot(pos_updt0[1], '--g', label='Initial belief', linewidth=2)
    plt.plot(pos_pred0[1], '--r', label='Initial belief', linewidth=2)

    # plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')
    plt.legend()

    plt.figure(36)
    plt.subplot(211)
    plt.plot(pos_est1[0], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas.meas_veh[1][0]).flatten(), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8)
    plt.plot(pos_updt1[0], '--g', label='Initial belief', linewidth=2)
    plt.plot(pos_pred1[0], '--r', label='Initial belief', linewidth=2)

    # plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.title('The simulated values for vehicle 2')
    plt.xlabel('Time [s]')
    plt.ylabel('Position x [m]')
    plt.legend()

    plt.subplot(212)
    plt.plot(pos_est1[1], 'r', label='Position estimate', linewidth=2.5, alpha=0.9)
    plt.plot(np.array(meas.meas_veh[1][1]).flatten(), 'ok',
             label='GNSS measurement', linewidth=1.5, alpha=0.8)
    plt.plot(pos_updt1[1], '--g', label='Initial belief', linewidth=2)
    plt.plot(pos_pred1[1], '--r', label='Initial belief', linewidth=2)

    # plt.axis([0, 6, 0, 20])
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Position y [m]')
    plt.legend()

    plt.show()
    plt.pause(0.05)