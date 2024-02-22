import numpy as np
from LU_decomposition import back_sub


def make_fun(fs, xs, fsize):
    A = np.zeros(fsize)
    for i in range(len(xs)):
        A[i] = fs(xs[i])
    return A


def least_squares(A, ys):
    return np.linalg.inv(A.T @ A) @ A.T @ ys


def gendata(m):
    return ((np.arange(m)) / m) * 2 * np.pi - np.pi


def gram_schmidt(A, gety=False):
    Q = np.zeros_like(A, dtype="float64")
    Y = np.zeros_like(A, dtype="float64")
    for i in range(A.shape[1]):
        Y[:, i] = A[:, i].copy()
        for j in range(0, i):
            Y[:, i] = Y[:, i] - Q[:, j] * np.dot(Q[:, j], A[:, i])
        Q[:, i] = Y[:, i] / np.linalg.norm(Y[:, i])
    if not gety:
        return Q
    else:
        return Q, Y

def QR(A, gety=False):
    if not gety:
        Q = gram_schmidt(A)
        R = Q.T @ A
        return Q, R
    else:
        Q, Y = gram_schmidt(A, True)
        R = Q.T @ A
        return Q, R, Y
def QR_leastSquares(A, y):
    Q, R = QR(A)
    return back_sub(R, Q.T @ y)



