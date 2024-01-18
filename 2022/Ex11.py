import numpy as np
import matplotlib.pyplot as plt
import bisec
import Newton_Raphson as nr

def pol(x):
    return  x**3 - 2 * x**2 -5 * x - 1

def dpol(x):
    return 3 * x**2 -4 * x -5

def d2pol(x):
    return 6*x-4

def tang1(a,x):
    return x*dpol(a)-a*dpol(a)+pol(a)


print(bisec.bisec2(pol, [-1000, 1000], 10e-7))
print(bisec.bisec2(dpol, [1, 3], 10e-7))
print(nr.newton_raphson(dpol, d2pol, -2, 10e-9))
print(bisec.bisec2(d2pol, [-1000, 1000], 10e-7))
print(d2pol(2.1196329811805255))



X = np.linspace(-5, 5, 1000000)
plt.figure(num=0, dpi=120)
plt.plot(X, pol(X), 'r', linewidth=3)
plt.annotate('Inflection Point', [0.6666667177341878, pol(0.6666667177341878)], fontsize=5)
plt.annotate('Max Point', [-0.7862996478468912, pol(-0.7862996478468912)], fontsize=5)
plt.annotate('Min Point', [2.1196329811805255, pol(2.1196329811805255)], fontsize=5)



plt.plot(X, dpol(X), 'g')
plt.plot(X, tang1(0.6666667177341878, X), 'k:')
plt.plot(X, tang1(2.1196329811805255, X), 'k:')
plt.plot(X, tang1(-0.7862996478468912, X), 'k:')
plt.xticks([-0.8, 0.7, 2.1])


plt.show()

