import numpy as np

def bisec(f, inter, tol):
    if f(inter[0]) == 0:
        return inter[0]
    elif f(inter[1]) == 0:
        return inter[1]
    elif abs(f(inter[0]) - f(inter[1]))/2 < tol:
        return (inter[0] + inter[1])/2
    elif f(sum(inter)/2) * f(inter[0]) > 0:
        return bisec(f, [sum(inter)/2, inter[1]], tol)
    else:
        return bisec(f, [inter[0], sum(inter)/2], tol)

def bisec2(f, inter, tol):
    mid = (inter[0] + inter[1])/2
    diff = abs(f(inter[0]) - f(inter[1]))
    while diff > tol:
        mid = (inter[0] + inter[1]) / 2
        diff = abs(f(inter[0]) - f(inter[1]))

        if f(sum(inter)/2) * f(inter[0]) > 0:
            inter[0] = mid

        else:
            inter[1] = mid
    return mid




def f(input):
    return np.sin(input)*input

def naive_ackermann(m, n, calls):
    #global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1, calls)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1, calls), calls)



#print(f(range(0, 10)))



#print(bisec2(f, [1, 5], 10**-9))