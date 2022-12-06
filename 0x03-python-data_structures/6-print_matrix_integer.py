#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        l = len(row)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j < l - 1:
                print("{}".format(matrix[i][j]), end=" ")
            elif j == l - 1:
                print("{}".format(matrix[i][j]))
