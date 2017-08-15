import numpy as np
import Distribution
import pickle

class DataCollect(object):

    def __init__(self, n_v, n_f):

        self.pred_veh_belief = [[] for i in range(n_v)]
        self.updt_veh_belief = [[] for i in range(n_v)]
        self.veh_belief = [[] for i in range(n_v)]
        self.veh_pos = [[] for i in range(n_v)]
        self.feat_belief = [[[]for j in range(n_f)] for i in range(n_v)]
        self.feat_pos = [[] for i in range(n_f)]


    def init(self, n_v, n_f, init_veh_distr, init_feat_distr):
        for i in range(n_v):
            self.veh_belief[i].append(init_veh_distr[i])
            self.updt_veh_belief[i].append(init_veh_distr[i])
            self.pred_veh_belief[i].append(init_veh_distr[i])
        # makes the 0th position to the initial distribution, later values of pos belief and updated pos belief from
        # i'th iteration follow in (i+1)'th position
            for j in range(n_f):
                self.feat_belief[i][j].append(init_feat_distr[j])

    def save_veh(self, veh_nr, new_veh_belief):
        self.veh_belief[veh_nr].append(new_veh_belief)

    def save_feat(self, veh_nr, feat_nr, new_feat_belief):
        self.feat_belief[veh_nr][feat_nr].append(new_feat_belief)

    def save_pred_veh(self, veh_nr, new_pred_veh_belief):
        self.pred_veh_belief[veh_nr].append(new_pred_veh_belief)

    def save_updt_veh(self, veh_nr, new_updt_veh_belief):
        self.updt_veh_belief[veh_nr].append(new_updt_veh_belief)

    def get_veh_belief(self, veh_nr):
        n = len(self.veh_belief[veh_nr])
        x = np.empty([4, n])
        for i in range(n):
            x[:, i] = np.transpose(self.veh_belief[veh_nr][i].get_mean())
        return x

    # def get_veh_belief(self, veh_nr):
    #     n = len(self.veh_belief[veh_nr])
    #     x = [None for g in range(n)]
    #     y = [None for f in range(n)]
    #     for i in range(n):
    #         x[i] = self.veh_belief[veh_nr][i].get_mean()[0, 0]
    #         y[i] = self.veh_belief[veh_nr][i].get_mean()[1, 0]
    #     return [x, y]

    def get_updt_veh_belief(self, veh_nr):
        n = len(self.updt_veh_belief[veh_nr])
        x = np.empty([4, n])
        for i in range(n):
            x[:, i] = np.transpose(self.updt_veh_belief[veh_nr][i].get_mean())
        return x

    # def get_updt_veh_belief(self, veh_nr):
    #     n = len(self.updt_veh_belief[veh_nr])
    #     x = [None for g in range(n)]
    #     y = [None for f in range(n)]
    #     for i in range(n):
    #         x[i] = self.updt_veh_belief[veh_nr][i].get_mean()[0, 0]
    #         y[i] = self.updt_veh_belief[veh_nr][i].get_mean()[1, 0]
    #     return [x, y]

    def get_pred_veh_belief(self, veh_nr):
        n = len(self.pred_veh_belief[veh_nr])
        x = np.empty([4, n])
        for i in range(n):
            x[:, i] = np.transpose(self.pred_veh_belief[veh_nr][i].get_mean())
        return x

    # def get_pred_veh_belief(self, veh_nr):
    #     n = len(self.pred_veh_belief[veh_nr])
    #     x = [None for g in range(n)]
    #     y = [None for f in range(n)]
    #     for i in range(n):
    #         x[i] = self.pred_veh_belief[veh_nr][i].get_mean()[0, 0]
    #         y[i] = self.pred_veh_belief[veh_nr][i].get_mean()[1, 0]
    #     return [x, y]

    def get_feat_belief(self, veh_nr, feat_nr):
        n = len(self.feat_belief[veh_nr][feat_nr])
        x = np.empty([2, n])
        for i in range(n):
            x[:, i] = np.transpose(self.feat_belief[veh_nr][feat_nr][i].get_mean())
        return x

    def save_data(self, name):
        with open('/home/tomek/TheTitans/ICP/Pickles/data' + name, 'wb') as output:
            pickle.dump(self, output)
