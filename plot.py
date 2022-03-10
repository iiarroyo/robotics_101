from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def two_dof_plot2(q1, q2, l1, l2):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # l1 = 2 # length of first arm
    # l2 = 2 # length of second arm
    # theta1 = radians(q1)
    # theta2 = radians(q2)
    # x1 = l1*cos(theta1)
    # y1 = l1*sin(theta1)
    # x2 = l1 * cos(theta1) + l2 * cos(theta1 + theta2)
    # y2 = l1 * sin(theta1) + l2 * sin(theta1 + theta2)
    # points = np.matrix([[0, 0], [x1, y1], [x2, y2]])
    # print(x2, y2)
    # plt.plot(points[:,0], points[:,1])
    %matplotlib qt
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    ax.view_init(30, 0)
    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    #     plt.draw()
    #     plt.pause(.001)
R = 0
P = 1

c1 = 2
c2 = 2
c3 = 2
c4 = 2
q1 = 0  # degrees
q2 = 0  # distance
l1 = 2
l2 = 2

sigma = [R, P]
a = [c3, 0]
alpha = [90, 0]
d = [c1, c2 + c4 + 1]  # q2 = 10
theta = [90, 90]  # theta1 = 90
# T =  GENFK(sigma, a, alpha, d, theta, q)
# print(T)

theta1 = 90 + q1
theta2 = 90
two_dof_plot2(theta1, theta2, c3, l2+q2)