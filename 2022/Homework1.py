import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def approx_ln(x, n):
    a = (x+1)/2
    g = x**0.5
    for i in range(n):
        a = (a+g)/2
        g = (a*g)**0.5
    return (x-1)/a

def d_func(a, k, n):
    if k == 0:
        return a[n]
    else:
        return (d_func(a, k - 1, n)-4**(-k)*d_func(a, k - 1, n - 1))/(1-4**(-k))

def fast_approx_ln(x, n):
    a = [(x + 1) / 2]
    g = x ** 0.5
    for i in range(n):
        a.append((a[i] + g) / 2)
        g = (a[i + 1] * g) ** 0.5
    d = d_func(a, n, n)
    return (x - 1)/d



def difference(x, n):
    result = list()
    for i in range(n):
        result.append(abs(approx_ln(x, i) - np.log(x)))
    return result

def plot_error(x, n):
    x_values = np.linspace(10**-6, x, 10**6)
    plt.figure(num=0, dpi=120)
    plt.yscale("log")
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    for i in range(n):
        plt.plot(x_values, abs(fast_approx_ln(x_values, i) - np.log(x_values)), f'{colors[i]}')
    plt.title('Error behaviour of the accelerated carlson method for the log')
    plt.legend(['1 iteration', '2 iterations', '3 iterations', '4 iterations','5 iterations','6 iterations', '7 iterations'])
    plt.savefig('differ_ln_vs_approx.pdf')
    plt.show()

print(fast_approx_ln(7, 4) - np.log(7))


#Jämförelse mellan approximationen av logaritm och numpys imbyggda
# Comparison between approx_ln and np.log

x_values = np.linspace(10**-6, 1000, 10**6)
plt.figure(num=0, dpi=120)
plt.plot(x_values, approx_ln(x_values, 1000), 'g+')
plt.plot(x_values, np.log(x_values), 'r-')
plt.show()
plt.savefig('ln_vs_approx.pdf')


# skillnaden plottad
# Difference plotted

# x_values = np.linspace(10**-6, 1000, 10**6)
# plt.figure(num=0, dpi=120)
# plt.plot(x_values, abs(approx_ln(x_values, 1000) - np.log(x_values)), 'g')
#plt.show()

# skillnaden plottad med x konstant och n som variabel
# Difference plotted with x as constant and n as variable

#x_values = list(range(1000))
#differences = difference(1.41, 1000)

#plt.plot(x_values, differences, 'g')
#plt.savefig('differ_func_of_n.pdf')
#plt.show()


# Skillnad mellan fast approx och numpys imbyggda
# Task 5

plot_error(20, n=5)
