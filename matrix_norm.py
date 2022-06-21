import numpy as np
from scipy.linalg import lu


def get_condition_number(array):
    x = max_matrix_norm(array)
    invert_matrix = plu_inverse(array)
    y = max_matrix_norm(invert_matrix)
    return x * y


def max_matrix_norm(array):
    norm = np.array([])
    for arr in array:
        sum = 0
        for i in arr:
            sum += i
        norm = np.append(norm, sum)

    max = norm[0]
    for i in range(len(norm)):
        if max < norm[i]:
            max = norm[i]

    return max


def forward_substitution(l_matrix, b):
    n = l_matrix.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / l_matrix[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(l_matrix[i, :i], y[:i])) / l_matrix[i, i]
    return y


def back_substitution(u_matrix, y):
    n = u_matrix.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / u_matrix[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(u_matrix[i, i:], x[i:])) / u_matrix[i, i]
    return x


def plu_inverse(a_matrix):
    n = a_matrix.shape[0]
    b = np.eye(n)
    a_matrix_inv = np.zeros((n, n))
    p, l_matrix, u_matrix = lu(a_matrix)
    for i in range(n):
        y = forward_substitution(l_matrix, np.dot(p, b[i, :]))
        a_matrix_inv[i, :] = back_substitution(u_matrix, y)
    return a_matrix_inv
