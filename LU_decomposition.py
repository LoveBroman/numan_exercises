import numpy as np

#A helper function that given a specific index and a matrix gives a
#The scalar product of all the elemnts to the right
def back_scalar(U, x, i):
    return U[i, i + 1:] @ x[i+1:]


def back_sub(U, b):
    assert U.shape[0] == U.shape[1] == len(b)
    x = np.zeros(len(U))
    for i, row in reversed(list(enumerate(U))):
        if i == len(U) - 1:
            x[i] = b[i] / U[i, i]
        else:
            x[i] = (b[i] - back_scalar(U, x, i)) / U[i, i]
    return x

def forward_scalar(L, x, i):
    return L[i, :i] @ x[:i]

def forward_sub(L, b):
    assert L.shape[0] == L.shape[1] == len(b)
    x = np.zeros(len(L))
    for i, row in enumerate(L):
        if i == 0:
            x[i] = b[i] / L[i, i]
        else:
            x[i] = (b[i] - forward_scalar(L, x, i)) / L[i, i]
    return x


U = np.array([[1, 2],
              [0, 1]])
b = np.array([6, 5])
x = back_sub(U, b)
x2 = np.linalg.solve(U, b)


print(x)
print(x2)