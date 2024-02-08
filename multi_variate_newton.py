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

def jacobian(vars, fs, values):
    jac = np.zeros((fs, vars))
    for i, f in enumerate(fs):
        for j, var in enumerate(vars):
            df = partial_diff(f, var)
            jac[i, j] = df(**values)
    return jac

# def multi_variate_newton(fs, x0, n=100):
