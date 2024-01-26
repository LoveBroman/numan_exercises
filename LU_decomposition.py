import numpy as np

#A helper function that given a specific index and a matrix gives a
#The scalar product of all the elemnts to the right
def back_scalar(U, x, i):
    return U[i, i + 1:] @ x[i+1:]


def back_sub(U, b):
    x = np.zeros(len(U))
    for i, row in reversed(list(enumerate(U))):
        if i == len(U) - 1:
            x[i] = b[i] / U[i, i]
        else:
            x[i] = (b[i] - back_scalar(U, x, i))/ U[i, i]
    return x


U = np.array([[1, 1],
              [0, 1]])
b = np.array([0, 1])
x = back_sub(U, b)



print(x)