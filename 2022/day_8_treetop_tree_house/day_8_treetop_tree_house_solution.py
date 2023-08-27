#!/usr/bin/env python3

import numpy as np

# Count the number of trees that are visible from outside the grid when looking directly along a row or column.
# Each tree is represented by a single digit whose value is height, from 0-9 (smallest -> tallest).
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
# How many trees are visible from outside the grid?

# Could speed up by checking shortest of row/column to tree first.
def check_axes(row, column, tree_height, row_index, col_index):
    # Check row up to tree.
    for i in range(col_index):
        if tree_height <= row[i]:
            break
        if i == col_index - 1:
            return 1
    # Check row from tree to end.
    for i in range(col_index + 1, len(row)):
        if tree_height <= row[i]:
            break
        if i == (len(row) - 1):
            return 1
    # Check column from top to tree.
    for j in range(row_index):
        if tree_height <= column[j]:
            break
        if j == row_index - 1:
            return 1
    # Check column from tree to bottom.
    for j in range(row_index + 1, len(column)):
        if tree_height <= column[j]:
            break
        if j == (len(row) - 1):
            return 1
    return 0

with open('input.txt', 'r') as f:
    # Initialise a grid of numbers.
    a2D = np.array([list(x.strip()) for x in list(f)])
    # All of the trees around the edge of the grid are visible. Initialise visible with 2*col + 2*row. 4 removes overlap of corners.
    visible = 2 * (len(a2D[0]) + len(a2D[:, 0])) - 4
    # That only leaves the interior trees to consider.
    for i in range(1, a2D.shape[0] - 1):
        for j in range(1, a2D.shape[1] -1 ):
            # pulls out each relevant tree coordinate to be evaluated.
            tree_height = a2D[i,j]
            visible += check_axes(a2D[i, :], a2D[:, j], tree_height, i, j)

# How many trees are visible from outside the grid?
print(visible)
