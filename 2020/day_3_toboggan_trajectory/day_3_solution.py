#!/usr/bin/env python3

def process(data, row_length, x_start, x_move, y_move):
    trees = 0 
    x = x_start
    for row_index in range(y_move, len(data), y_move):
        x += x_move
        if x >= row_length:
            x = x - row_length
        if (data[row_index][x]) == '#':
            trees += 1
    return trees

with open('/Users/awood/git_personal_repos/advent-of-code/2020/day_3_toboggan_trajectory/dummy_input.txt', 'r') as f:
    data = [list(l.strip()) for l in list(f)]

    part_1_answer = process(data, len(data[0]), 0, 3, 1)
    print(f"Part 1 answer: {part_1_answer}")

    part_2_result = part_1_answer
    part_2_result = part_2_result * process(data, len(data[0]), 0, 1, 1)
    part_2_result = part_2_result * process(data, len(data[0]), 0, 5, 1)
    part_2_result = part_2_result * process(data, len(data[0]), 0, 7, 1)
    part_2_result = part_2_result * process(data, len(data[0]), 0, 1, 2)
    print(f"Part 2 answer: {part_2_result}")