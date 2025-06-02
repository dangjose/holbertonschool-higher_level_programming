#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda row: [num ** 2 for num in row], matrix))
