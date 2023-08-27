#!/usr/bin/env python3

import numpy as np

def calculate_scenic(row, column, tree_height, row_index, col_index):
    # Start at tree; stop if you reach an edge
    # or at the first tree that is the same height or taller than the tree under consideration (inclusive)
    # scenic score is found by multiplying together its viewing distance in each of the four directions.
    scenic = []

    # Up
    count = 0
    for j in range(row_index - 1, -1, -1):
        count += 1
        if tree_height <= column[j]:
            break
    scenic.append(count)

    # Left
    count = 0
    for i in range(col_index - 1, -1, -1):
        count += 1
        if tree_height <= row[i]:
            break
    scenic.append(count)

    # Down
    count = 0
    for j in range(row_index + 1, len(column)):
        count += 1
        if tree_height <= column[j]:
            break
    scenic.append(count)

    # Right
    count = 0
    for i in range(col_index + 1, len(row)):
        count += 1
        if tree_height <= row[i]:
            break
    scenic.append(count)
    
    return np.prod(scenic)

with open('input.txt', 'r') as f:
    # Initialise the best scenic score 
    max_scenic = 0
    # Initialise a grid of numbers.
    a2D = np.array([list(x.strip()) for x in list(f)])
    # That only leaves the interior trees to consider.
    for i in range(1, a2D.shape[0] - 1):
        for j in range(1, a2D.shape[1] -1 ):
            # pulls out each relevant tree coordinate to be evaluated.
            tree_height = a2D[i,j]
            scenic = calculate_scenic(a2D[i, :], a2D[:, j], tree_height, i, j)
            if scenic > max_scenic:
                max_scenic = scenic

# How many trees are visible from outside the grid?
print(max_scenic)
