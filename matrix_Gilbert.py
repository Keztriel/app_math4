import scipy.sparse


def empty_matrix(n, m, output_format):
    matrix = scipy.sparse.__dict__[output_format + "_matrix"]
    return matrix((n, m))


def generate_hilbert_matrix(k):
    a_k = empty_matrix(k, k, "lil")
    for i in range(k):
        for j in range(k):
            a_k[i, j] = 1.0 / (i + j + 1.0)

    return a_k.tocsr()
