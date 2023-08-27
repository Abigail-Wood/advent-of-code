#!/usr/bin/env python3

max = 0
with open ("2022/day_1_calorie_counting/dummy_input_part_1.txt", 'r') as f:
    count = 0
    for line in list(f):
        # If we've not yet hit an empty line, we're still on the same elf.
        if line.strip() != "":
            count += int(line)
        # Check whether your elf is the most calorific; either way, reset the calorie count.
        else:
            if count > max:
                max = count
            count = 0

# Handle the final elf.
if count > max:
    max = count

print(max)