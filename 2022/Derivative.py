import numpy as np
#1101001001101
def derivative(f, n, h):
    dd = (f(n+h) - f(n-h))/(2*h)
    def d():
        return dd
    return d

def func(x):
    return x**2+5*x+np.exp(x)

dx = derivative(func, 31, 10**-8)
print(dx())