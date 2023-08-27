#!/usr/bin/env python3

import itertools

def main():
    count = 0
    with open("input_part1.txt", 'r') as f:
        for x, y in itertools.pairwise(list(f)):
            if int(x) < int(y):
                count += 1
    print(count)

if __name__ == '__main__':
    main()
