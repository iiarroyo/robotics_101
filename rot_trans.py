"""
Actividad:
    Programming Assignment Rotations and Translations 
Video:
    https://youtu.be/cMWbo0xkxno
Alumno: 
    Israel Ivan Arroyo Parada
Matricula:
    A01706190
Profesor: 
    Jesus Arturo Escobedo
"""
import math as math
import numpy as np
from os import linesep as endl

def my_rotx(theta):
    """
    Write a function called my_rotx(theta) that takes as input the angle
    theta in radians and computes the fundamental rotation matrix around
    the x-axis.(It should give as result a 3x3 matrix).
    :input: degrees
    """
    rad = math.radians(theta) 
    res = np.matrix([[1,         0,                         0],
                     [0,    math.cos(rad), -math.sin(rad)],
                     [0,    math.sin(rad), math.cos(rad)]])
    return res


def my_roty(theta):
    """
    Write a function called my_roty(theta) that takes as input the angle
    theta in radians and computes the fundamental rotation matrix around
    the y-axis. (It should give as result a 3x3 matrix).
    :input: degrees
    """
    rad = math.radians(theta) 
    res = np.matrix([[math.cos(rad),   0,       math.sin(rad)],
                     [0,                 1,       0           ],
                     [-math.sin(rad),  0,       math.cos(rad)]])
    return res


def my_rotz(theta):
    """
    Write a function called my_rotz(theta) that takes as input the angle
    theta in radians and computes the fundamental rotation matrix around
    the z-axis. (It should give as result a 3x3 matrix).
    :input: degrees
    """
    rad = math.radians(theta) 
    res = np.matrix([[math.cos(rad), -math.sin(rad), 0],
                     [math.sin(rad), math.cos(rad),  0],
                     [0,               0,                1]])
    return res
 

def my_transl(x,y,z):
    """
    Write a function my_transl(x,y,z) that takes as input the translations
    around the x, y, and z axis and gives you the corresponding homogeneous
    transformation matrix. (It should give as result a 4x4 matrix). 
    """
    # id_matrix can be swaped for any rot matrix in the future
    id_matrix = np.matrix([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
    t_b = np.matrix([[x],
                     [y],
                     [z]])
    btm_row = np.matrix([[0, 0, 0, 1]])
    htm = np.hstack([id_matrix,t_b])  # adds t_b col
    htm = np.vstack([htm,btm_row])  # adds btm_row
    return htm


def main():
    # print("my_rotx(pi/4)")
    # print("  {0}{1}".format(my_rotx(rad), endl))

    # print("my_roty(-pi/4)")  # (notice the minus sign)
    # print("  {0}{1}".format(my_roty(rad), endl))
    # print("my_rotz(pi/2)") 
    # print("  {0}{1}".format(my_rotz(rad), endl))

    # print("my_transl(2,3,4)")
    # print("  {0}{1}".format(my_transl(2,3,4), endl))
    roty=my_roty(35)
    rotx = my_rotx(90)
    rotz=my_rotz(90)
    print(rotx*rotz)

if __name__ == '__main__':
    main()

 