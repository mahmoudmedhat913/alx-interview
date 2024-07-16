#!/usr/bin/python3
"""rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """rotate it 90 degree clockwise
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list[y]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """rotate 2d matrix"""
    rotate_2d_matrix(matrix)
    print(matrix)
