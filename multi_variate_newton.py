import numpy as np
from functools import partial

def partial_diff(f, var, eps=10**-11):
    def fp(**kwargs):
        y = kwargs[var]
        k_copy = kwargs.copy()
        k_copy.pop(var)

        pf = partial(f, **{**k_copy, var: y + eps})
        mf = partial(f, **{**k_copy, var: y - eps })

        return (pf() - mf()) / (2 * eps)
    return fp

def f(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    z = kwargs["z"]
    return x + 4 * y**2 + 3*z*y

fp = partial_diff(f, "y")
print(fp(x=1, y=2, z=3))

def jacobian(numvars, *fs):
    jac = np.zeros((fs, numvars))
    for f in fs:
        for var in range(numvars):
            pass