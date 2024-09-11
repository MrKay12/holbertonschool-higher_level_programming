#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    matrix2 = []

    for row in matrix:
        row2 = [element ** 2 for element in row]
        matrix2.append(row2)

        return matrix2
