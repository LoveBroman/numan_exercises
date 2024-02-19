import numpy as np
def make_fun(fs, xs, fsize):
    A = np.zeros(fsize)
    for i in range(len(xs)):
        A[i] = fs(xs[i])
    return A



def least_squares(A, ys):

    return np.linalg.inv(A.T @ A) @ A.T @ ys

def gendata(m):
    return ((np.arange(m)) / m) * 2 * np.pi - np.pi



# xs = np.array([
#     [0, 1],
#     [0, 1],
#     [1, 0],
#     [1, 0],
#     [1, 2]])
#
# ys = np.array([3, 2, 3, 4, 6])
# fs = lambda x: np.insert(x, 0, 1)
#
# print(np.linalg.inv(xs.T @ xs) @ xs.T @ ys)
#
# A = make_fun(fs, xs,(xs.shape[0], xs.shape[1] + 1))
# t = least_squares(A, ys)
#
# print(t)

