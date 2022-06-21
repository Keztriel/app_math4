import random

import numpy as np
from numpy.linalg import solve, det, cond, norm

import matrix_norm

a = np.array([[2, -1, 0],
              [-1, 2, -1.],
              [0, -1, 2.]])

def get_random_A(n):
    a = np.matrix([[random.randrange(-4, 0) for i in range(n)] for j in range(n)])
    if det(a) == 0: print("bad matrix")
    return a

def formalize(A, k, _i = 1):
    a = np.copy(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i != j:
                if (i < _i):
                    a[i,j] = -1 * sum(a[i, :])
                elif (i > _i):
                    a[i,j] = -1 * sum(a[i, :]) + 10 ** k
    return a


a = get_random_A(4)
print(a)
c = []
x_ = [];
for k in range (10):
    # print(k)
    A = formalize(a, k)
    # print(A)
    F = [1, 2, 12, 5]
    x = solve(A, F)
    c += [cond(A, 'fro')]
    x_ += [x]

for i in c: print(i)
for i in x_: print(i)