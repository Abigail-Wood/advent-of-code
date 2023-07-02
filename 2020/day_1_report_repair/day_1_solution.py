#!/usr/bin/env python3

# "Find two values in a list of integers that sum to a specified integer value, and multiply those two integers together."
def process_once(l, target):
    for i in l:
        r = target - i
        if r in l:
            print(i * r)
            return

# "Find three values in a list of integers that sum to a specified integer value, and multiple those three integers together."
def process_twice(l, target):
    for i in l:
        r1 = target - i
        for j in filter(lambda x: x != i, l):
            r2 = r1 - j
            if r2 in filter(lambda x: x != i or j, l):
                print(i * j * r2)
                return

with open('/Users/awood/git_personal_repos/advent-of-code/./2020/day_1_report_repair/dummy_input.txt', 'r') as f:
    process_once([int(l.strip()) for l in list(f)], 2020)
    f.seek(0)
    process_twice([int(l.strip()) for l in list(f)], 2020)
