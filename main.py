from numpy.linalg import norm, cond

from jacobi import jacobi
import matrix_norm
from matrix_Gilbert import generate_hilbert_matrix
import numpy as np

from test_hilbert import test_hilbert

if __name__ == "__main__":
    a = np.array([[2, -1, 0],
                  [-1, 2, -1.],
                  [0, -1, 2.]])

    # a = np.array([[-4, -1, 0],
    #               [-1, -10, -1.],
    #               [0, -1, -2.]])

    # a = np.array([[2, -1, 0],
    #               [-1, 2, -1.],
    #               [0, -1, -2.]])

def formalize(a, k):
    a_

def test_first(a, k):

    print("k = ", k)

    a = formalize(a, k)
    # print("matrix")
    # print(a)
    # print()
    # print("jacobi")
    # print(len(jacobi(a)))

    # print("matrix")
    # print(a)

    # print("max_matrix_norm")
    # print(matrix_norm.max_matrix_norm(a))
    # print("matrix_norm")
    # print(norm(a, 'fro'))

    # 'fro' - норма Фробениуса ( корень из суммы квадратов элементов матрицы )

    # print("invert_matrix")
    # invert = matrix_norm.plu_inverse(a)
    # print(invert)

    # print("max_matrix_norm_invert")
    # print(matrix_norm.max_matrix_norm(invert))
    # print("matrix_norm_invert")
    # print(norm(invert, 'fro'))

    # print("get_condition_number")
    # print(matrix_norm.get_condition_number(a))
    print(cond(a, 'fro'))



for i in range(1, 11):
    test_hilbert(10 * i)


