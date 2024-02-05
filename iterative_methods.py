import numpy as np

def inner_seidel(A, b, x, D, L, U):
    for i, row in enumerate(A):
        x[i] = (b[i] - (L[i] + U[i]) @ x) / D[i]
    return x

def iter(A, b, x0, n, method='jacobi'):
    x = x0
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(A)
    for i in range(n):
        print(f"x{i} = {x.flatten()}")
        if method == 'jacobi':
            x = (b - (L + U) @ x) / D[:,None]
        elif method == 'seidel':
            inner_seidel(A, b, x, D, L, U)
    return x

arr = np.array(
    [[4, 1, 1],
       [1, 4, 1],
       [1,  1, 4]])

b = np.array([[1, 1, 1]], dtype=np.float64).T
x0 = np.array([[0,0,0]], dtype=np.float64).T
x = iter(arr, b, x0, 100)
print(x)
print(np.linalg.solve(arr, b))