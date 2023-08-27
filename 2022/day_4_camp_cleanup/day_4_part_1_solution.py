#!/usr/bin/env python3

def extract_ranges(s):
    # data structure desired is tuples of ranges e.g. (range(1, 3), range(2, 4))
    # each pair is comma-separated; each range is - separated.
    tuples = [x.split('-') for x in s.split(',')]
    pair_of_ranges = [(range(int(t[0]), int(t[1]) + 1)) for t in tuples]
    return tuple(pair_of_ranges)

count = 0
with open('input.txt', 'r') as f:
    pairs_of_ranges = [extract_ranges(x.strip()) for x in list(f)]
    for p in pairs_of_ranges:
        common = list(set(p[0]) & set(p[1]))
        if len(common) == min(len(p[0]), len(p[1])):
            count +=1

#In how many assignment pairs does one range fully contain the other?
print(count)