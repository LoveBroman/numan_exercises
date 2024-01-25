import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def deriv(f):
    return lambda x: (f(x + 10**-11) - f(x))/10**-11

def newton_raphson(f, fp, x0, tol):
    x = x0
    n = 0
    while f(x) > tol and n < 400:
        x = x - f(x) / fp(x)
        n += 1

    return x, f'converged == {(n <= 400)}, n={n} '

def newton_raphson2(f, x0, tol, plotall=False):
    x = x0
    n = 0
    fp = deriv(f)
    print("f", f(x))
    while abs(f(x)) > tol and n < 400 and fp(x) != 0:
        x = x - (f(x) / fp(x))
        if n <=3 or plotall:
            print(x, f(x))
        n += 1

    return x, f'converged == {(n < 400)}, n={n} '

def secant(f, a, b):
    return (f(a) - f(b))/(a - b)

def secant_metod(f, a, b, tol, plotall=False):
    n = 0
    while abs(f(b)) > tol and n < 400:
        a, b = a - f(a)/secant(f,a, b), a
        if n <=3 or plotall:
            print(a, f(a))
        n += 1
    return a, f'converged == {(n < 400)}, n={n} '



def f(x):
    return x ** 7 + 9 *x-11

def fp(x):
    return 7 * x ** 6 + 9

# print(newton_raphson(f, fp, 9000000, 10**-10))
# print(newton_raphson2(f,9000000, 10**-10))

#e1
# print(newton_raphson2(lambda x: x**3 + x**2 - 1, 1,10**-10))
# print(newton_raphson2(lambda x: x**2 + 1/(x + 1) -3*x, 1, 10**-10))
# print(newton_raphson2(lambda x: 5*x - 10, 1, 10**-10))

#e3
# print(newton_raphson2(lambda x: x ** 3 -6*x**2 + 4*x +12, 5, 10**-10))
# print(newton_raphson2(lambda x: np.exp(np.sin(x)**3) + x**6 -2*x**4 -x**3 -1, 5, 10**-10))
# print(newton_raphson2(lambda x: 4**2*x/np.sin(x), 5, 10**-10,True))

#e4
# print(secant_metod(lambda x: np.exp(x) + np.sin(x) - 4, 5, 3, 10**-10,True))
print(secant_metod(lambda x: x**3 - 6*x**2 + 4*x + 12, 5, 3, 10**-10,True))
print(secant_metod(lambda x: np.exp(np.sin(x)**3) + x**6 -2*x**4 - x**3 - 1, 5, 3, 10**-10,True))

