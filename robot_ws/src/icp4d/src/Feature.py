import Distribution

class Feature(object):

    def __init__(self, id, init_pos_distr):
        self.id = id
        self.init_pos_distr = init_pos_distr
        self.pos_belief = init_pos_distr #some initial belief of the position, which is a pdf!!!!!!!!!!!!!!!!!!!1
        self.pos_belief_iterative = Distribution.Distribution(None, None)
        self.m_gf_covinv = None
        self.m_gf_covinvmu = None
        self.m_fg = None
        self.consensus = Distribution.Distribution(None, None)
        # self.visible_veh = [None]

    def reset_belief(self):
        self.pos_belief = self.init_pos_distr

