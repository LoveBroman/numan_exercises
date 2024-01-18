from numpy import *
from matplotlib.pyplot import *

class Interval:
    def __init__(self,a, b=None):
        if b is None:
            b = a
        self.a = a
        self.b = b
        self.interval = [a, b]
        #print([a, b]) # This line is commented out as not every computation need this displayed. If many intervals are computed it may cloud the console.
    
    def __add__(self, other):
        if type(other) != Interval:
            return Interval(self.a+other,self.b+other)
        else:
            return Interval(self.a+other.a,self.b+other.b)
        
    def __radd__(self,other):
        return Interval(self.a+other,self.b+other)
     
    def __sub__(self, other):
        if type(other) != Interval:
            return Interval(self.a-other,self.b-other)
        else:
            return Interval(self.a-other.b,self.b-other.a)
        
    def __rsub__(self,other):
        return Interval(other-self.a,other-self.b)
                        
    def __mul__(self, other):
        if type(other) != Interval:
            return Interval(self.a*other,self.b*other)
        else:
            comb = [self.a*other.a,self.a*other.b,self.b*other.a,self.b*other.b]
            return Interval(min(comb),max(comb))
        
    def __rmul__(self, other):
        if type(other) != Interval:
            return Interval(self.a*other,self.b*other)

    def __truediv__(self, other):
        if self.a == 0:
            raise Exception(f"a = 0, can't divide by {self.a}!")
        elif other.b == 0:
            raise Exception(f"d = 0, can't divide by {other.b}!")
        elif self.a/other.a >= (2^63 - 1) or self.a/other.b >= (2^63 - 1) or self.b/other.a >= (2^63 - 1) or self.b/other.b >= (2^63 - 1):
            raise Exception("Interval is infinately large, it does not have a finite limit")
        elif type(other) != Interval:
            return Interval(self.a/other,self.b/other)
        else:
            comb = [self.a/other.a,self.a/other.b,self.b/other.a,self.b/other.b]
            return Interval(min(comb),max(comb))
    
    def __contains__(self,x):
        if x >= self.a and x <= self.b:
            return f"{x} is in the interval {self.interval}"
        else:
            return f"{x} is not in the interval {self.interval}"
    
    def __neg__(self):
        return Interval(-self.a,-self.b)
    
    def __pow__(self,other):
        if (other % 2) == 0:
            if self.a >= 0:
                return Interval(self.a**other,self.b**other)
            elif self.b < 0:
                return Interval(self.b**other,self.a**other)
            else:
                return Interval(0,max(self.a**other,self.b**other))
        else:
            return Interval(self.a**other,self.b**other)


# Creating all of the lists, including the final one, for task 10
xl = linspace(0.,1,1000)
xu = linspace(0.,1,1000) +.5

L = []
for i in range(len(xl)):
    L.append(Interval(xl[i],xu[i]))
    
PL = []
for n in range(len(L)):
    PL.append(3*L[n]**3-2*L[n]**2-5*L[n]-1)
    
yl = []
yu = []
for k in range(len(PL)):
    yl.append(PL[k].a)
    yu.append(PL[k].b)

# Plotting the result for task 10
plot(xl,yl,'b', linewidth=.75)
plot(xl,yu, 'g', linewidth=.75)
xlim(0,1)
ylim(-10,4)
xlabel(r'$x$')
ylabel(r'$p(I)$')
title(r'$p(I) = 3I^{3} - 2I^{2} - 5I - 1, I = Interval(x,x+0.5)$')
show()


    
    
    
    
    
    
    