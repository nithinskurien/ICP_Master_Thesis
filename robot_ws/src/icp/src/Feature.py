import Distribution

class Feature(object):

    def __init__(self, id, nr_veh, init_pos_distr):
        self.id = id
        self.pos_belief = init_pos_distr #some initial belief of the position, which is a pdf!!!!!!!!!!!!!!!!!!!1
        self.pos_belief_iterative = Distribution.Distribution(None, None)
        self.m_gf = [None for i in range(nr_veh)]
        self.m_fg = [None for j in range(nr_veh)]

