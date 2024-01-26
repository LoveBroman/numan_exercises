import unittest
import numpy as np
from LU_decomposition import *

class TestLU(unittest.TestCase):
    np.random.seed(0)

    def test_back_sub(self):
        n = 70
        A = np.triu(np.random.rand(n, n))
        b = np.random.rand(n)
        x = back_sub(A, b)
        x1 = np.linalg.solve(A, b)
        self.assertTrue(np.allclose(x, x1))

    def test_forward_sub(self):
        n = 50
        A = np.tril(np.random.rand(n,n))
        b = np.random.rand(n)
        x = forward_sub(A, b)
        x1 = np.linalg.solve(A, b)
        self.assertTrue(np.allclose(x, x1))

    def test_solve_standard(self):
        A1 = np.array([[3, -0.5, 0.6],
                       [4.7, 2, 2.3],
                       [.1, -5, 9.1]])

        b1 = np.array([4.57, 8.14, 46.76])
        A2 = np.array([[1, 1, 1],
                       [1, -1, 2],
                       [3, 1, 4]])
        b2 = np.array([1, 1, 1])

        x1 = solve(A1, b1)
        x1t = np.linalg.solve(A1, b1)
        self.assertTrue(np.allclose(x1, x1t))
        x2 = solve(A2, b2)
        x2t = np.linalg.solve(A2, b2)
        print(x2)
        print(x2t)
        #self.assertTrue(np.allclose(x2, x2t))
        #x2 Does not work because of singular matrix

    def test_solve(self):
        n = 500
        A = np.random.rand(n,n)
        b = np.random.rand(n)
        x = solve(A, b)
        x1 = np.linalg.solve(A, b)
        self.assertTrue(np.allclose(x, x1))





