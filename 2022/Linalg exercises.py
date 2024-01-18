import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def _is_symmetric(matrix):
    v = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return 0
    return 1

def _is_skewed(matrix):
    v = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                pass
            elif matrix[i][j] != - matrix[j][i]:
                return 0
    return -1

def symmetric(matrix):
    return _is_symmetric(matrix) + _is_skewed(matrix)

def v_to_matrix(u):
    A = np.zeros((len(u), len(u)))
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                A[i, j] = -2 * u[i]
            elif i-1 == j:
                A[i, j] = u[i]
            elif i == j - 1:
                A[i, j] = u[i + 1]
    return(A)

def norm(u):
    return ((u ** 2).sum()) ** 0.5, np.linalg.norm(u)


# vector = v_to_matrix(np.linspace(0, 2*np.pi, 500)) * np.ones(500)
# plt.figure(num=0, dpi=120)
# plt.plot(vector)
# plt.show()

def ort(u1, u2):
    return sum(u1 * u2) == 0

ort = ort(np.array([1, -1, 1]), np.array([2, 1, -1]))

print(ort)

#print(norm(np.array([1, 2, 3])))
#print(create_vector(np.array([1, 2, 3])))



arr = np.array([[1, -4, -3],
                [4, 5, -8],
                [3, 8, 9]])

#print(symmetric(arr))

# rot_m = np.array([[np.cos(1), np.sin(1)],[-np.sin(1), np.cos(1)]])
#
# u = np.array([1, 1])
# m = rot_m.dot(u)
# t = np.transpose(rot_m).dot(m)
# print(t)
# plt.figure(num=0, dpi=120)
# plt.plot(u, 'g+')
# plt.plot(m)
# plt.plot(t, 'r')
# plt.show()

x = np.full((19, 19), 1)

A = 4 * np.eye(20) + np.diag(np.diag(x), k=1) - np.diag(np.diag(x), k=-1)
# print(A)
# print(np.linalg.eig(A))
print(np.shape(A))