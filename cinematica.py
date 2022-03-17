from math import *
import matplotlib.pyplot as plt
"""
function punto = fcn(centro, Radio, t, Tiempo, initial_angles, Longitudes)

punto_i = [centro(1)+Radio; centro(2)];
t_espera = 1;  t_punto_i = 10; t_inicio = 2;

L1 = Longitudes(1);
L2 = Longitudes(2);
q1 = initial_angles(1);
q2 = initial_angles(2);

if(t<t_espera)
    disp("Esperando al controlador")
    punto = [L1*cos(q1)+L2*cos(q1+q2) ; L1*sin(q1)+L2*sin(q1+q2)];
elseif(t<t_punto_i+t_espera)
    punto_aux = [L1*cos(q1)+L2*cos(q1+q2) ; L1*sin(q1)+L2*sin(q1+q2)];
    punto = punto_aux + (t-t_espera)*(punto_i-punto_aux)/t_punto_i;
elseif(t<t_punto_i+t_espera+t_inicio)
    punto = punto_i;
elseif(t<t_punto_i+t_espera+t_inicio+Tiempo)
    t_aux = t_punto_i + t_espera + t_inicio;
    t_punto = t - t_aux;
    angulo = 2*pi*t_punto / Tiempo;
    punto = centro + Radio* [cos(angulo) ; sin(angulo)];
else
    punto = punto_i;
end
"""
def punto_d(centro, radio, t, tiempo, initial_angles, Longitudes):
    # punto = [0, 0]
    punto_i = [[centro[1]+Radio], [centro[2]]]
    t_espera = 1
    t_punto_i = 10
    t_inicio = 2

    L1 = Longitudes[1]
    L2 = Longitudes[2]
    q1 = initial_angles[1]
    q2 = initial_angles[2]
    for i in range(8000):
        if(t<t_espera):
            disp("Esperando al controlador")
            punto = [[L1*cos(q1)+L2*cos(q1+q2) ],[L1*sin(q1)+L2*sin(q1+q2)]]
        elif(t<t_punto_i+t_espera):
            punto_aux = [[L1*cos(q1)+L2*cos(q1+q2)],[L1*sin(q1)+L2*sin(q1+q2)]]
            punto = punto_aux + (t-t_espera)*(punto_i-punto_aux)/t_punto_i
        elif(t<t_punto_i+t_espera+t_inicio):
            punto = punto_i
        elif(t<t_punto_i+t_espera+t_inicio+Tiempo):
            t_aux = t_punto_i + t_espera + t_inicio
            t_punto = t - t_aux
            angulo = 2*pi*t_punto / Tiempo
            punto = centro + Radio* [[cos(angulo)],[sin(angulo)]]
        else:
            punto = punto_i
        plt.plot(punto)
        plt.show()
"""
function [theta1, theta2] = fcn(punto, longitudes)
    x = punto(1);
    y = punto(2);
    L1 = longitudes(1);
    L2 = longitudes(2);
    theta2 = acos( (x^2 + y^2 - L1^2 - L2^2) / (2*L1*L2) );
    theta1 = atan(y/x) - atan( (L2*sin(theta2)) / (L1+ (L2*cos(theta2))) );
"""
def cin(punto, logitudes):
    x = punto[1]
    y = punto[2]
    L1 = longitudes[1]
    L2 = longitudes[2]
    theta2 = acos((x^2 + y^2 - L1^2 - L2^2) / (2*L1*L2))
    theta1 = atan(y/x) - atan( (L2*sin(theta2)) / (L1+ (L2*cos(theta2))));


if __name__ == "__main__":
    centro = [0, 0]
    radio = 1
    t = 1
    tiempo = 20
    initial_angles = [0, 0]
    longitudes = [2, 2]
    punto_d(centro, radio, t, tiempo, initial_angles, Longitudes)
    

