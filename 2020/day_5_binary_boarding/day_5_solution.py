#!/usr/bin/env python3

conversion_dict = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}
def calculate_seat_ids(row_column_list):
    seat_ids = []
    for (r, c) in row_column_list:
        for k, v in conversion_dict.items():
            r = r.replace(k, v)
            c = c.replace(k, v)
        r = int(r, 2)
        c = int(c, 2)
        seat_id = r * 8 + c
        seat_ids.append(seat_id)
    return seat_ids

def find_missing_seat_id(seat_ids):
    for i in range(min(seat_ids), max(seat_ids)):
        if i in seat_ids:
            continue
        else:
            return i

with open("/Users/awood/git_personal_repos/advent-of-code/2020/day_5_binary_boarding/input.txt", 'r') as f:
    seat_ids = calculate_seat_ids([(x[:7], x[7:]) for x in list(f)])
    print(f"Part One answer: {max(seat_ids)}")
    print(f"Part Two answer: {find_missing_seat_id(seat_ids)}")
    