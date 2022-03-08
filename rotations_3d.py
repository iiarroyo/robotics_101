import math as math
import numpy as np
from numpy.linalg import inv

atd = np.matrix([[1, 0, 0, -1],
                 [0, 1, 0, 1],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

ctd = np.matrix([[0, 1, 0, 0],
                 [1, 0, 0, 0],
                 [0, 0, -1, -2],
                 [0, 0, 0, 1]])

btc = np.matrix([[1, 0, 0, 4],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

res = atd*inv(ctd)*inv(btc)
# res = inv(btc)
print(res)