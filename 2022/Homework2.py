import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Interval:
    
    def __init__(self, mini, maxi=None):
        if maxi == None:
            self.mini = mini
            self.maxi = mini
        else:
            self.mini = mini
            self.maxi = maxi

    def __str__(self):
        return f'{[self.mini, self.maxi]}'



    def __add__(self, other):
        if type(other) == int or type(other) == float:
            mini = self.mini + other
            maxi = self.maxi + other
        else:
            mini = self.mini + other.mini
            maxi = self.maxi + other.maxi
        return Interval(mini, maxi)

    def __radd__(self, other):
        return self.__add__(other)


    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            if other >= 0:
                return Interval(self.mini * other, self.maxi * other)
            else:
                return Interval(self.maxi * other, self.mini * other)
        else:
            mini = min(self.mini * other.mini, self.maxi * other.mini, self.mini * other.maxi, self.maxi * other.maxi)
            maxi = max(self.mini * other.mini, self.maxi * other.mini, self.mini * other.maxi, self.maxi * other.maxi)
        return Interval(mini, maxi)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            mini = self.mini - other
            maxi = self.maxi - other
        else:
            mini = self.mini - other.maxi
            maxi = self.maxi - other.mini
        return Interval(mini, maxi)
    
    def __rsub__(self, other):
        return Interval(- self.__sub__(other).maxi, - self.__sub__(other).mini)
        #return Interval(other-self.mini,other-self.maxi)


    def __truediv__(self, other):
        if other.mini == 0 or other.maxi == 0:
            raise ZeroDivisionError()
        mini = min(self.mini / other.mini, self.maxi / other.mini, self.mini / other.maxi, self.maxi / other.maxi)
        maxi = max(self.mini / other.mini, self.maxi / other.mini, self.mini / other.maxi, self.maxi / other.maxi)
        return Interval(mini, maxi)

    def __contains__(self, item):
        return item >= self.mini and item <= self.maxi

    def __neg__(self):
        return Interval(- self.maxi, - self.mini)

    def __pow__(self, power, modulo=None):
        if power % 2 != 0:
            return Interval(self.mini ** power, self.maxi ** power)
        elif self.mini >= 0:
            return Interval(self.mini ** power, self.maxi ** power)
        elif self.maxi < 0:
            return Interval(self.maxi ** power, self.mini ** power)
        else:
            return Interval(0, max(self.mini ** power, self.maxi ** power))
                                                                         


#Uppgift 8

# print(Interval (2 , 3 ) + 1) # [3, 4]
# print(1 + Interval (2 , 3 )) # [3, 4]
# print(1.0 + Interval (2 , 3 )) # [3.0, 4.0]
# print(Interval (2 , 3 ) + 1.0) # [3.0, 4.0]# I1 = Interval(1, 4)
# print(1 - Interval (2 , 3 )) # [ -2, -1]# I2 = Interval(1000)
# print(Interval (2 , 3 ) -1) # [1, 2]# print(I2)
# print(1.0 - Interval (2 , 3 )) # [ -2.0, -1.0]# print(I1 + I2)
# print(Interval (2 , 3 ) - 1.0) # [1.0, 2.0]# print(I1 - I2)
# print(Interval (2 , 3 ) * 1) # [2, 3]# print(I1 * I2 )
# print(1 * Interval (2 , 3 )) # [2, 3]# print(I1 / I2)
# print(1.0 * Interval (2 , 3 )) # [2.0, 3.0]# print(1 in I1)
# Interval (2 , 3 ) * 1.0 # print(1 in I2)

#Uppgift 9
x = Interval (-2 , 2 ) # [ -2, 2]
x2 = Interval(0, 0.5)
print(x ** 2) # [0, 4]
print(x ** 3)
print(5 - 2*x2**2 + 3*x2**3)
print( (3 * x2**3) - (2 * x2**2) - (5 * x2) - 1)


#Uppgift 10

xl = np.linspace(0.,1,1000)
xu = np.linspace(0.,1,1000) + 0.5
il = list()
for i in range(len(xl)):
    il.append(Interval(xl[i], xu[i]))

y_list = list(map(lambda x: 3 * x**3 - 2 * x**2 - 5 * x - 1, il))


yl = [i.mini for i in y_list]
yu = [i.maxi for i in y_list]

plt.figure(num=0, dpi=120)
plt.xlabel(r'$x$')
plt.ylabel(r'$p(I)$')
plt.title('$p(I) = 3I^{3} - 2I^{2} - 5I - 1, I = Interval(x,x+0.5)$')
plt.plot(xl, yl, 'g')
plt.plot(xl, yu, 'b')
plt.show()

