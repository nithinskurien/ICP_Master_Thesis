import numpy as np
import Distribution
import pickle

class DataCollect(object):

    def __init__(self, n_v, n_f):
        self.pred_veh_belief = [[] for i in range(n_v)]
        self.veh_belief = [[] for i in range(n_v)]
        self.veh_pos = [[] for i in range(n_v)]
        self.feat_belief = [[] for i in range(n_f)]
        self.feat_pos = [[] for i in range(n_f)]
        #self.

    def init(self, n_v, n_f, init_veh_distr, init_feat_distr):
        for i in range(n_v):
            self.veh_belief[i].append(init_veh_distr[i])
            self.pred_veh_belief[i].append(init_veh_distr[i])
        '''makes the 0th position to the initial distribution, later values of
         pos belief and pred pos belief from i'th iteration follow in (i+1)'th position'''
        for j in range(n_f):
            self.feat_belief[j].append(init_feat_distr[j])

    def save_veh(self, veh_nr, new_veh_belief):
        self.veh_belief[veh_nr].append(new_veh_belief)

    def save_feat(self, feat_nr, new_feat_belief):
        self.feat_belief[feat_nr].append(new_feat_belief)

    def save_pred_veh(self, veh_nr, new_veh_pred_belief):
        self.pred_veh_belief[veh_nr].append(new_veh_pred_belief)

    def get_veh_belief(self, veh_nr):
        n = len(self.veh_belief[veh_nr])
        x= [None for g in range(n)]
        y = [None for f in range(n)]
        for i in range(n):
            x[i] = self.veh_belief[veh_nr][i].get_mean()[0, 0]
            y[i] = self.veh_belief[veh_nr][i].get_mean()[1, 0]
        return [x, y]

    def get_pred_veh_belief(self, veh_nr):
        n = len(self.pred_veh_belief[veh_nr])
        x= [None for g in range(n)]
        y = [None for f in range(n)]
        for i in range(n):
            x[i] = self.pred_veh_belief[veh_nr][i].get_mean()[0, 0]
            y[i] = self.pred_veh_belief[veh_nr][i].get_mean()[1, 0]
        return [x, y]

    def get_feat_belief(self, veh_nr):
        n = len(self.feat_belief[veh_nr])
        x= [None for g in range(n)]
        y = [None for f in range(n)]
        for i in range(n):
            x[i] = self.feat_belief[veh_nr][i].get_mean()[0, 0]
            y[i] = self.feat_belief[veh_nr][i].get_mean()[1, 0]
        return [x, y]

    def save_data(self):
        with open('my_dataset.pickle', 'wb') as output:
            pickle.dump(self, output)
