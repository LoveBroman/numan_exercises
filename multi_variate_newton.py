import numpy as np
from functools import partial
import matplotlib.pyplot as plt

def partial_diff(f, var, eps=10**-11):
    def fp(**kwargs):
        y = kwargs[var]
        k_copy = kwargs.copy()
        k_copy.pop(var)

        pf = f(**{**k_copy, var: y + eps})
        mf = f(**{**k_copy, var: y - eps})

        return (pf - mf) / (2 * eps)
    return fp

def jacobian(fs, vars, values):
    jac = np.zeros((len(fs), len(vars)))
    for i, f in enumerate(fs):
        for j, var in enumerate(vars):
            df = partial_diff(f, var)
            jac[i, j] = df(**values)
    return jac

def multi_apply(fs, values):
    arr = np.zeros_like(fs, dtype="float64")
    for i, f in enumerate(fs):
        arr[i] = f(**values)
    return arr

def err(r, x):
    return (sum((r-x) ** 2)) ** .5

def multi_variate_newton(fs, vars, x0, n=100, roots=None):
    x = x0
    for i in range(n):
        x_dict = dict(zip(vars, x))
        Da = jacobian(fs, vars, x_dict)
        #Da = exact_jacobian(x_dict)
        inv_a = np.linalg.inv(Da)
        xnew = x - inv_a @ multi_apply(fs, x_dict)
        if roots is not None:
            ek = err(x, roots)
            ekp = err(xnew, roots)
            print(f"Error after {i} iteration", ekp / (ek +1e-13))
        x = xnew
    x = dict(zip(vars, x))
    return x


def exact_jacobian(x_dict):
    x1 = x_dict["x1"]
    x2 = x_dict["x2"]
    x3 = x_dict["x3"]
    n = len(x_dict)
    jac = np.zeros((n, n), dtype="float64")
    jac[0,:] = [2*(x1-2), 2*x2, -1]
    jac[1,:] = [x2 ** 2 -1, 2*x1*x2 + x3 - 3, x2]
    jac[2,:] = [x3**2 + x2, x3**2 + x1, 2*x3 * (x1 + x2) -3]
    return jac

#avoids inverses
def multi_variate_newton2(fs, vars, x0, n=100, roots=None):
    x = x0
    for i in range(n):
        x_dict = dict(zip(vars, x))
        Da = exact_jacobian(x_dict)
        dx = np.linalg.solve(Da,- multi_apply(fs, x_dict))
        xnew = x + dx
        if roots is not None:
            ek = err(x, roots)
            ekp = err(xnew, roots)
            print(f"Error after {i} iteration", ekp / ek)
        x = xnew
    x = dict(zip(vars, x))
    return x

def f1(**kwargs):
    x1 = kwargs["x1"]
    x2 = kwargs["x2"]
    x3 = kwargs["x3"]
    return x1**2 - 2*x1 + x2**2 - x3 + 1

def f2(**kwargs):
    x1 = kwargs["x1"]
    x2 = kwargs["x2"]
    x3 = kwargs["x3"]
    return x1 * x2**2 - x1 -3*x2 + x2*x3 +2

def f3(**kwargs):
    x1 = kwargs["x1"]
    x2 = kwargs["x2"]
    x3 = kwargs["x3"]
    return x1*x3**2 - 3*x3 + x2*x3**2 + x1*x2

# def plot_jacobian(f):
#
#     rows, cols = Da.shape
#     fig, axs = plt.subplots(rows, cols, figsize=(15, 15))
#     for i, row in Da:
#         for


fs = [f1, f2, f3]
vars = ["x1", "x2", "x3"]

x100 = multi_variate_newton(fs, vars, np.array([1, 2, 3]), roots=np.ones(3, dtype="float64"))
y100 = multi_variate_newton2(fs, vars, np.array([1, 2, 3]), roots=np.ones(3, dtype="float64"))

print(x100)
print(y100)