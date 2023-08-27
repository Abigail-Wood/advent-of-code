#!/usr/bin/env python3

import itertools 

def main():
    count = 0
    with open("input_part1.txt", 'r') as f:
        # Read input file into a list of integers, with no newline characters.
        measurements = [int(x.strip()) for x in list(f)]
        sums = []
        window_size = 3
        # Generate a list of sums for each size-X sliding window.
        for i in range(len(measurements) - window_size + 1):
            sums.append(sum(measurements[i: i + window_size]))
        # Re-use iterator from part 1. 
        for x, y in itertools.pairwise(sums):
            if x < y:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
