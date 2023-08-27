#!/usr/bin/env python3

# ingest all elves, then sort, then take top 3
elves = []
with open ("2022/day_1_calorie_counting/input.txt", 'r') as f:
    count = 0
    for line in list(f):
        # If we've not yet hit an empty line, we're still on the same elf.
        if line.strip() != "":
            count += int(line)
        # otherwise, count your elves!
        else:
            elves.append(count)
            count = 0
# Handle the final elf.
elves.append(count)
# Sort them in descending order
elves.sort(reverse = True)
# Sum those who make the cut :)
print(sum(elves[0:3]))
