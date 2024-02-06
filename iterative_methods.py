import numpy as np

def inner_seidel(A, b, x, D, L, U):
    x_new = x
    for i, row in enumerate(A):
        x_new[i] = (b[i] - (L[i] + U[i]) @ x_new) / D[i]
    return x_new

# def SOR(A, b, x, D, L, U, w):
#     LDI = np.linalg.inv(D + w * L)
#     for i, row in enumerate(A):
#         x[i] = LDI[i] * (((1 - w) * D[i] - U[i]).T @ x) + w * LDI[i] @ b
#     return x

def iter(A, b, x0, n, method='jacobi', w=1, tol=1e-6):
    x = x0
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(A)
    for i in range(n):
        print(f"x{i} = {x.flatten()}")
        if method == 'jacobi':
            x_new = (b - (L + U) @ x) / D[:, None]
        elif method == 'seidel':
            x_new = inner_seidel(A, b, x, D, L, U)
        elif method == 'SOR':
            LDI = np.linalg.inv(D + w * L)
            #x_new = LDI @ (((1 - w) * D - w *U) @ x) + w * LDI @ b
            x_new = np.linalg.solve(D + w * L, (1 - w) * D @ x + w * b - w * U @ x)
        if np.linalg.norm(x_new - x, np.inf) / np.linalg.norm(x_new, np.inf) < tol:
            return x_new
        x = x_new
    return x

arr = np.array([[3, -1, 0, 0, 0, .5],
                [-1, 3, -1, 0, .5,0],
                [0, -1, 3, -1, 0, 0],
                [0, 0, -1, 3, -1, 0],
                [0, .5, 0, -1, 3, -1],
                [.5, 0, 0, 0, -1, 3]])

b = np.array([[5/2, 3/2, 1, 1, 3/2, 5/2]], dtype=np.float64).T
x0 = np.array([[1, 1, 1, 1, 1, 1]], dtype=np.float64).T
x = iter(arr, b, x0, 6, "SOR", 1.1)
print(x)
print(np.linalg.solve(arr, b))