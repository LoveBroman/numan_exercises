import numpy as np
import time
import matplotlib.pyplot as plt


def crazu_plus(a, b):
    if (type(a) != float and type(a) != int) or (type(b) != float and type(b) != int):
        raise ValueError('Inputen ska vara numerisk')
    return float(str(a - b) + str(a + b))

print(crazu_plus(10, 6))

def track_time(n):
    t = np.empty(n)
    for i in range(n):
        t1 = time.time()
        crazu_plus(7**i, 3**i)
        np.append(t, t1 - time.time())
    return t


