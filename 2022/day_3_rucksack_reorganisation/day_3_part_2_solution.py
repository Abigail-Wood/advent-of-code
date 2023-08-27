#!/usr/bin/env python3
from itertools import zip_longest

def grouper(file, n, fillvalue=None):
    args = [iter(file)] * n
    return zip_longest(*args, fillvalue=fillvalue)

with open ("input.txt", 'r') as f:
    p = []
    # Assumes 1 rucksack (string) per line; 3 lines per elf group.
    for group in grouper(f, 3, ''):
        group = [x.strip() for x in group]
        # Find the item type that appears in rucksack of all elves in the group. 
        badge = set(group[0]) & set(group[1]) & set(group[2])
        # Extract the single element from the set as a string.
        e = badge.pop()
        # lowercase item a-z is prioritised 1-26 (alphabetical ordered numbering!)
        if (ord(e) >= 97 and ord(e) <= 122):
            p.append(int(ord(e) - 96))
        # uppercase item A-Z is prioritised 27-52 (alphabetical ordered numbering + 26!)
        else:
            p.append(int(ord(e.lower()) - 70))

# What is the sum of the priorities of those item types?
print(sum(p))