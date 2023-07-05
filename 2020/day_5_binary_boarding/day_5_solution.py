#!/usr/bin/env python3

def calculate_seat_ids(row_column_list):
    seat_ids = []
    for (r, c) in row_column_list:
        row = int(r.replace('F', '0').replace('B', '1'), 2)
        col = int(c.replace('R', '1').replace('L', '0'), 2)
        seat_ids.append(row * 8 + col)
    return seat_ids

def find_missing_seat_id(seat_ids):
    for i in range(min(seat_ids), max(seat_ids) + 1):
        if i in seat_ids:
            continue
        else:
            return i

with open("/Users/awood/git_personal_repos/advent-of-code/2020/day_5_binary_boarding/input.txt", 'r') as f:
    seat_ids = calculate_seat_ids([(x[:7], x[7:]) for x in list(f)])
    print(f"Part One answer: {max(seat_ids)}")
    print(f"Part Two answer: {find_missing_seat_id(seat_ids)}")
    