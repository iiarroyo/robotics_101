#!/usr/bin/env python
from math import *
from socket import timeout
import matplotlib.pyplot as plt
import numpy as np
import time
import serial

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
centro = [13, 2]
Radio = 4
Tiempo = 17
initial_angles = [pi/2, pi/4]
Longitudes = [2, 2]
punto_i = np.array([centro[0]+Radio, centro[1]])
t_espera = 1
t_punto_i = 10
t_inicio = 2


def punto_d(t):
    L1 = Longitudes[0]
    L2 = Longitudes[1]
    q1 = initial_angles[0]
    q2 = initial_angles[1]
    if(t < t_espera):
        print("Esperando al controlador")
        punto = [(L1*cos(q1)+L2*cos(q1+q2)), (L1*sin(q1)+L2*sin(q1+q2))]
    elif(t < t_punto_i+t_espera):
        punto_aux = [(L1*cos(q1)+L2*cos(q1+q2)), (L1*sin(q1)+L2*sin(q1+q2))]
        punto = punto_aux + (t-t_espera)*(punto_i-punto_aux)/t_punto_i
    elif(t < t_punto_i+t_espera+t_inicio):
        punto = punto_i
    elif(t < t_punto_i+t_espera+t_inicio+Tiempo):
        t_aux = t_punto_i + t_espera + t_inicio
        t_punto = t - t_aux
        angulo = 2*pi*t_punto / Tiempo
        punto = centro + Radio * [cos(angulo), sin(angulo)]
    else:
        punto = punto_i
    return punto

def calcAngle(reqcos):
    res1 = atan2(sqrt(1-pow(reqcos,2)), reqcos)
    res2 = atan2(sqrt(1-pow(reqcos,2))*(-1), reqcos)
    return (res1, res2)

def cin(punto, longitudes):
    x = punto[0]
    y = punto[1]
    l1 = longitudes[0]
    l2 = longitudes[1]
    # ctheta2 = (x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2)
    # stheta2 = sqrt(1 - pow(ctheta2,2))
    # try:
    #     ctheta1 = (x * (l1 + l2 * ctheta2) + y * l2 *stheta2) / (x**2 + y**2)
    # except ZeroDivisionError:
    #     ctheta1 = (x * (l1 + l2 * ctheta2) + y * l2 *stheta2) / (0.001**2 + 0.001**2)
    # theta1a, theta1b = calcAngle(ctheta1)
    # theta2a, theta2b = calcAngle(ctheta2)
    theta2 = acos((pow(x, 2) + pow(y, 2) - pow(l1, 2) - pow(l2, 2)) / (2*l1*l2))
    theta1 = atan(y/x) - atan( (l2*sin(theta2)) / (l1+ (l2*cos(theta2))) )
    return (theta1, theta2)


if __name__ == "__main__":
    i = 0
    start = time.time()
    now = time.time()
    fin = 60
    t1s = []
    t2s = []
    while (now-start) < fin:
        now = time.time()
        p = punto_d(now-start)
        t1,t2 = cin(p, Longitudes)
        t1s.append(t1)
        t2s.append(t2)
        # time.sleep(0.5)
    plt.plot(t1s)
    plt.plot(t2s)
    plt.show()
