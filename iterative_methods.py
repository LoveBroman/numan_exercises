import numpy as np


def inner_seidel(A, b, x, D, L, U):
    x_new = x.copy()
    for i, row in enumerate(A):
        x_new[i] = (b[i] - (L[i] + U[i]) @ x_new) / D[i, i]
    return x_new

# def SOR(A, b, x, D, L, U, w):
#     LDI = np.linalg.inv(D + w * L)
#     for i, row in enumerate(A):
#         x[i] = LDI[i] * (((1 - w) * D[i] - U[i]).T @ x) + w * LDI[i] @ b
#     return x

def iterate(A, b, x0, n=100, method='jacobi', w=1, tol=1e-14, showlen=None):
    x = x0
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diagflat(np.diag(A))
    for i in range(n):
        #print(f"x{i} = {x.flatten()}")
        if method == 'jacobi':
            # x_new = (b - (L + U) @ x) / D[:, None]
            x_new = (b - (L + U) @ x) @ np.linalg.inv(D)

        elif method == 'seidel':
            x_new = inner_seidel(A, b, x, D, L, U)
        elif method == 'SOR':
            LDI = np.linalg.inv(D + w * L)
            #x_new = LDI @ (((1 - w) * D - w *U) @ x) + w * LDI @ b
            x_new = np.linalg.solve(D + w * L, (1 - w) * D @ x + w * b - w * U @ x)
        if showlen is not None:
            print(f"length of x after {i} iterations:  {((x_new ** 2).sum()) ** .5}")

        # if np.linalg.norm(x_new - x, np.inf) / np.linalg.norm(x_new, np.inf) < tol:
        #     return x_new
        x = x_new
    return x

#ex3
# arr = np.array([[3, -1, 0, 0, 0, .5],
#                 [-1, 3, -1, 0, .5,0],
#                 [0, -1, 3, -1, 0, 0],
#                 [0, 0, -1, 3, -1, 0],
#                 [0, .5, 0, -1, 3, -1],
#                 [.5, 0, 0, 0, -1, 3]])
#
# b = np.array([[5/2, 3/2, 1, 1, 3/2, 5/2]], dtype=np.float64).T
# x0 = np.array([[1, 1, 1, 1, 1, 1]], dtype=np.float64).T

#Assignment3 q2 ans: 0.2348997169840506
# arr = np.array([[15, -5, 1, 1.1],
#                 [0, 5, 2, -1],
#                 [2, -1, 9, -1],
#                 [1, 1.1, -1, -6]])
# b = np.ones(4)
# x0 = np.array([2, 1, 1, 1])
#
# x = iter(arr, b, x0, roots=np.array([ 0.11716446, 0.1386601,   0.08537596, -0.13594756]))
# print(x)
# print(np.linalg.solve(arr, b))

# arr = np.array([[15, -5, 1, 1.1],
#                 [0, 5, 2, -1],
#                 [2, -1, 9, -1],
#                 [1, 1.1, -1, -6]], dtype="float64")
# b = np.ones(4, dtype="float64")
# x0 = np.array([2, 1, 1, 1], dtype="float64")
#
# x = iterate(arr, b, x0, method="seidel", showlen=True)
# print(x)
# print(np.linalg.solve(arr, b))
a = np.array([[3, -1],
              [-1, 2]])
x0 = np.array([1, 0])
b = np.array([5, 4])
print(iterate(a, b, x0, n=1))

A = np.array([[1, -1, 1, -1],
              [1, 1, 1, 1],
              [1, 2, 4, 8],
              [1, 3, 9, 27]])

b= np.array([3, 1, 3, 7])
print(np.linalg.det(A))
print("solu ", np.linalg.solve(A, b))

