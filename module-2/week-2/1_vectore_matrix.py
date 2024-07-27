import numpy as np


# To compute vector length
def compute_vector_length(vector):
    return np.linalg.norm(vector)


# To compute dot product
def compute_dot_product(v1, v2):
    return np.dot(v1, v2)


#
def matrix_multi_vector(m, v):
    return np.dot(m, v)


#
def matrix_multi_matrix(m1, m2):
    return np.dot(m1, m2)


#
def inverse_matrix(m):
    return np.linalg.inv(m)
