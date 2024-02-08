import numpy as np
from functools import partial

def partial_diff(f, var, eps=10**-11):
    def fp(**kwargs):
        y = kwargs[var]
        k_copy = kwargs.copy()
        k_copy.pop(var)

        pf = partial(f, **{**k_copy, var: y + eps})
        mf = partial(f, **{**k_copy, var: y - eps})

        return (pf() - mf()) / (2 * eps)
    return fp

def jacobian(fs, vars, values):
    jac = np.zeros((len(fs), len(vars)))
    for i, f in enumerate(fs):
        for j, var in enumerate(vars):
            df = partial_diff(f, var)
            jac[i, j] = df(**values)
    return jac

def multi_apply(fs, values):
    arr = np.zeros_like(fs)
    for i, f in enumerate(fs):
        arr[i] = f(**values)
    return arr

def err(r, x):
    return sum((r-x) ** 2)

def multi_variate_newton(fs, vars, x0, n=100, roots=None):
    x = x0
    for i in range(n):
        x_dict = dict(zip(vars, x))
        Da = jacobian(fs, vars, x_dict)
        inv_a = np.linalg.inv(Da)
        xnew = x - inv_a @ multi_apply(fs, x_dict)
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
    return x1 **2 -2*x1 + x2 **2 - x3 + 1

def f2(**kwargs):
    x1 = kwargs["x1"]
    x2 = kwargs["x2"]
    x3 = kwargs["x3"]
    return x1 *x2 **2 - x1 -3*x2 + x2*x3 +2

def f3(**kwargs):
    x1 = kwargs["x1"]
    x2 = kwargs["x2"]
    x3 = kwargs["x3"]
    return x1*x3**2 - 3 * x3 + x2*x3**2 + x1*x2


fs = [f1, f2, f3]
vars = ["x1", "x2", "x3"]

x100 = multi_variate_newton(fs, vars, np.arange(3) +1, roots=np.ones(3))
print(x100)