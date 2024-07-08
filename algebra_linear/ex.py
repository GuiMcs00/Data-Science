import math
from functools import reduce
import numpy as np

vectores = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = [1, 2, 3]
w = [4, 5, 6]
vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return[v_i - w_i
           for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_reduce(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

# print((scalar_multiply(vector_reduce(vectors), vector_reduce(vectors))))

def reduce_scalar_multiply(vectors):
    return reduce(scalar_multiply, vectors)

# print(reduce_scalar_multiply(vectors)) # Pesquisar sobre!
# Desafio 1: construir uma função que itera sobre o vectors multiplicando os elementos na posição correspondente.
# resutado esperado é: [28, 80, 162]

# Desafio 1 superado

def vector_mult(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = [r_i * v_i for r_i, v_i in zip(result, vector)]
    return result


def vector_mean(vectors):
    """computar o vetor cujo o i-ésimo elemento seja a média dos
    i-ésimos elementos dos vetores inclusos"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    return sum(v_i * w_i
           for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


# Matrizes

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_j[j] for A_j in A]

# print(get_row(vectors, 0))
# print(get_column(vectors, 2))


def make_matrix(num_rows, num_columns, entry_fn):
    return [[entry_fn(i,j)
             for j in range(num_columns)]
            for i in range(num_rows)]
