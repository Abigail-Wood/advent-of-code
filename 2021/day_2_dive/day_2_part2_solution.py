#!/usr/bin/env python3

horizontal_position = 0
depth = 0
aim = 0

with open ("2021/day_2_dive/input.txt", 'r') as f:
    lines = [(x.strip()).split(" ") for x in list(f)]
    for i in range(len(lines)):
        x,y =  lines[i]
        # if forward, add to horizontal_position count
        if x == "forward":
            horizontal_position += int(y)
            depth += aim * int(y)
        # if down, add to depth count. 
        if x == "down":
            aim += int(y)
        # if up, subtract from depth count.
        if x == "up":
            aim -= int(y)

# What is the multiple of final horizontal position and final depth?
print(horizontal_position * depth)