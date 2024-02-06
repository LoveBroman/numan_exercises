import numpy as np


# A helper function that given a specific index and a matrix gives a
# The scalar product of all the elemnts to the right

def back_scalar(U, x, i):
    return U[i, i + 1:] @ x[i + 1:]


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

def gauss_elim(A, b):
    assert A.shape[0] == A.shape[1] == len(b)
    U = A.copy()
    c = b.copy()

    for i, row in enumerate(U):
        for j, rowj in list(enumerate(U))[i + 1:]:
            fac = U[j, i] / U[i, i]
            U[j] = U[j] - fac * U[i]
            c[j] = c[j] - fac * c[i]
    return U, c

def LU_factorize(A):
    assert A.shape[0] == A.shape[1]
    U = A.copy()
    L = np.eye(A.shape[0])

    for i, row in enumerate(U):
        for j, rowj in list(enumerate(U))[i + 1:]:
            fac = U[j, i] / U[i, i]
            U[j] = U[j] - fac * U[i]
            L[j, i] = fac
    return L, U

def solve(A, b):
    U, c = gauss_elim(A, b)
    return back_sub(U, c)

def LU_solve(A, b):
    L, U = LU_factorize(A)
    y = forward_sub(L, b)
    x = back_sub(U, y)
    return x

def swap(arr, i, j):
    temp = arr[i].copy()
    arr[i] = arr[j]
    arr[j] = temp

def pivot(A, P, i):
    maxrow = A[i:, i].argmax() + i
    swap(A, i, maxrow)
    swap(P, i, maxrow)

def PALU_factorize(A):
    assert A.shape[0] == A.shape[1]
    P = np.eye(len(A))
    pivot(A, P, 0)
    for i, row in enumerate(A):
        for j, rowj in list(enumerate(A))[i + 1:]:
            fac = A[j, i] / A[i, i]
            A[j, i + 1:] -= fac * A[i, i + 1:]
            A[j, i] = fac
        if i < len(A) -1:
            pivot(A, P, i + 1)
    return A, P


A = np.array([[3, 1, 2],
             [6, 1, 3],
             [6, 0, 1]], dtype="float64")

b = np.array([1, 2, 3])

LU, P = PALU_factorize(A)
L = np.tril(LU, -1) + np.eye(len(A))
U = np.triu(LU)
print("P = \n", P)
print("L = \n",L)
print("U = \n", U)
print(P.T @ L @ U)


