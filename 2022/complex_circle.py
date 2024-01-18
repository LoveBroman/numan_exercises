import cmath
import math
import numpy as np
import matplotlib.pyplot as plt

def f(theta, r):
    return [r*np.cos(theta), r*np.sin(theta)]

fig = plt.figure(num = 0, dpi=120)
#axes = fig.add_axes([-0.5, -0.5, .8, .8])


#Plottar axeln med konstant radie men med olika vinklar
xlist = np.linspace(0, 8*np.pi, 4000)
#ylist = f(xlist, 0.5)
#print(ylist[0:1000])

#plt.plot(ylist[0], ylist[1], 'r')

#plt.show()


#Ökande radie
xlist2 = np.linspace(0, 10, 4000)

ylist2 = f(xlist, xlist2)
plt.plot(ylist2[0], ylist2[1], 'r')
plt.show()



