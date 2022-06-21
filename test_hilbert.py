from numpy.linalg import cond

from matrix_Gilbert import generate_hilbert_matrix


def test_hilbert(k):

    # print("k = ", k)

    a = generate_hilbert_matrix(k)
    a = a.toarray()
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