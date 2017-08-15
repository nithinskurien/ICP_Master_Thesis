import numpy as np
import matplotlib.pyplot as plt

class Trajectory(object):
    def __init__(self, c_x, c_y, rad):
        self.vel = 0.1
        self.ang_vel = 0.1
        self.t_s = 0.05
        self.radius = rad
        self.center_x = c_x
        self.center_y = c_y
        # self.center_x = 0.0
        # self.center_y = 0.0
        self.x_vec = []
        self.y_vec = []
        self.theta_vec = []
        self.tra_mod = []

    def trajectory(self, loop):
        # true_input = False
        # while not true_input:
        #    try:
        #         loop = int(raw_input('Enter The no of Loops to Run:'))
        #         true_input = True
        #    except ValueError:
        #         print "Not a number"
        theta_min = np.arccos(1-((self.vel*self.t_s)**2/(2*self.radius**2)))
        x = []
        y = []
        print theta_min
        theta = []
        itera = int(2*np.pi/theta_min)
        j=0
        for i in range(loop*itera):
            if j%itera is 0:
                j=0
            x.append(self.radius*np.cos(j*theta_min-(np.pi/2))+self.center_x)
            y.append(self.radius*np.sin(j*theta_min-(np.pi/2))+self.center_y)
            theta.append(j*theta_min)
            j+=1
        tra = [x, y, theta]
        # plt.figure()
        # plt.plot(tra[0], tra[1])
        # plt.figure()
        # plt.plot(tra[2])
        # plt.show()
        return tra, itera

    def re_route(self, x, y, angle, loop):
        angle = self.euler0to360(angle)
        print "Re-Routing the Trajectory"
        tra, iter = self.trajectory(loop)
        dist_temp = np.sqrt((self.center_x - x) ** 2 + (self.center_y - y) ** 2)

        if dist_temp > self.radius:
            print "Outside Circle"
            dest = self.dest_tangent(tra, iter, x, y, dist_temp)
            self.rotate(x, y, angle, tra[2][dest])
            self.forward(x, y, tra[0][dest], tra[1][dest])

        if dist_temp <= self.radius:
            print "Inside Circle"
            dest = self.dest_leastdist(tra, iter, x, y)
            dest_angle = self.euler0to360(np.arctan2((tra[1][dest] - y), (tra[0][dest] - x)))
            self.rotate(x, y, angle, dest_angle)
            self.forward(x, y, tra[0][dest], tra[1][dest])
            self.rotate(tra[0][dest], tra[1][dest], self.euler0to360(np.arctan2((tra[1][dest] - y), (tra[0][dest] - x))), tra[2][dest])

        self.x_vec.extend(tra[0][dest:])
        self.y_vec.extend(tra[1][dest:])
        self.theta_vec.extend(tra[2][dest:])
        self.tra_mod = [self.x_vec, self.y_vec, self.theta_vec]
        #self.print_tra()

        return self.tra_mod, self.t_s

    def dest_tangent(self, tra, iter, x, y, dist_temp):
        dest = 0
        des_angle = np.arcsin(self.radius / dist_temp)
        dist_d = dist_temp * np.cos(des_angle)
        for i in range(iter):  # Finding the Merging Point
            dist_temp = np.sqrt((tra[0][i] - x) ** 2 + (tra[1][i] - y) ** 2)
            if np.fabs(dist_d - dist_temp) < (self.vel * self.t_s):  #Selecting the Tangent Point in the Direction of Motion on Trajectory
                if np.fabs(tra[2][i] - self.euler0to360(np.arctan2((tra[1][i]-y), (tra[0][i]-x)))) < .01:
                    angle_temp = tra[2][i]
                    dest = i
        print "Found Merging Point to Original Trajectory, Dest: " + str(dest) + " X: " + str(tra[0][dest]) + " Y :" + str(tra[1][dest])
        return dest

    def dest_leastdist(self, tra, iter, x, y):
        dest = 0
        dist = np.sqrt((tra[0][0] - x) ** 2 + (tra[1][0] - y) ** 2)
        for i in range(iter):
            dist_temp = np.sqrt((tra[0][i] - x) ** 2 + (tra[1][i] - y) ** 2)
            if dist_temp <= dist:
                dist = dist_temp
                dest = i
        print "Found Merging Point to Original Trajectory, Dest: " + str(dest) + " X: " + str(tra[0][dest]) + " Y :" + str(tra[1][dest])
        return dest

    def rotate(self, curr_x, curr_y, curr_angle, dest_angle):
        t_rev = int((dest_angle - curr_angle) / (self.ang_vel * self.t_s))
        for i in range(np.absolute(t_rev)):  # Rotating to match the orientation
            self.x_vec.append(curr_x)
            self.y_vec.append(curr_y)
            self.theta_vec.append(curr_angle + (i * t_rev/(np.abs(t_rev)) * self.ang_vel * self.t_s))
        # for i in range(t_rev):  #For Waiting after Rotation
        #     self.x_vec.append(curr_x)
        #     self.y_vec.append(curr_y)
        #     self.theta_vec.append(dest_angle)
        print "Angle to Turn: " + str(dest_angle) + ", Present Angle: " + str(curr_angle) + ", Steps to Turn: " + str(np.absolute(t_rev))

    def forward(self, curr_x, curr_y, dest_x, dest_y):
        dist_to_trav = np.sqrt((dest_x - curr_x) ** 2 + (dest_y - curr_y) ** 2)
        time_to_trav = dist_to_trav / self.vel
        angle_to_trav = self.euler0to360(np.arctan2((dest_y - curr_y), (dest_x - curr_x)))
        print "Distance to Travel: " + str(dist_to_trav) + ", Time to Travel: " + str(time_to_trav) + ", Angle: " + str(angle_to_trav)

        for i in range(int(time_to_trav / self.t_s)):  # Moving to the Desired Point
            self.x_vec.append(curr_x + i * self.vel * self.t_s * np.cos(angle_to_trav))
            self.y_vec.append(curr_y + i * self.vel * self.t_s * np.sin(angle_to_trav))
            self.theta_vec.append(angle_to_trav)

    def euler0to360(self, angle):

        if angle < 0:
            angle = angle + 2 * np.pi
        if angle > 2 * np.pi:
            angle = angle - 2 * np.pi2
        else:
            return angle

    def print_tra(self):

        plt.figure()
        plt.plot(self.tra_mod[0], self.tra_mod[1], 'b', label='Trajectory', linewidth=2.5, alpha=0.9, mec='b')
        plt.grid(True)
        plt.title('Trajectory Reference')
        plt.xlabel('$X\ (m) $')
        plt.ylabel('$Y\ (m)$')
        plt.legend()
        plt.figure()
        plt.plot(self.tra_mod[2], 'r', label='Theta', linewidth=2.5, alpha=0.9, mec='b')
        plt.grid(True)
        plt.title('Theta Reference')
        plt.xlabel('$Iterations$')
        plt.ylabel('$Theta (rad)$')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    Trajectory().re_route(0.0, 0.0, 0.0)