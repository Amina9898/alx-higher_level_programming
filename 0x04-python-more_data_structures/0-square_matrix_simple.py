#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        res_row = []
        for i in row:
            res_row.append(i**2)
        result.append(res_row)
    return result
