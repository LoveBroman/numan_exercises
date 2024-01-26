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
        print(x)
        print(x1)
        self.assertTrue(np.allclose(x, x1))


