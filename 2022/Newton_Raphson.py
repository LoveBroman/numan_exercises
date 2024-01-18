import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def newton_raphson(f, fp, x0, tol):
    x = x0
    n = 0
    while f(x) > tol and n < 400:
        x = x - f(x) / fp(x)
        n += 1

    return x, f'converged == {(n <= 400)}, n={n} '

def f(x):
    return x**7+9*x-11

def fp(x):
    return 7*x**6+9

#print(newton_raphson(f, fp, 9000000, 10**-10))