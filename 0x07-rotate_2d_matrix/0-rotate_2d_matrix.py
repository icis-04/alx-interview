#!/usr/bin/python3
""" script to rotate a matrix 2 """


def rotate_2d_matrix(matrix):
    """ function for rotating a square matrix"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    N = len(matrix)

    for i in range(N//2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
