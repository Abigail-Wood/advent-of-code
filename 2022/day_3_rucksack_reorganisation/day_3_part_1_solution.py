#!/usr/bin/env python3

# Assumes substrings are of equal size.
def split_string(s):
    mid = len(s)//2
    s1, s2 = s[:mid], s[mid:]
    return (s1, s2)

with open ("input.txt", 'r') as f:
    p = []
    # Assumes 1 rucksack (string) per line; 2 compartments (substrings) per rucksack.
    lines = [split_string(x.strip()) for x in list(f)]
    for line in lines:
        # Find the item type that appears in both compartments of each rucksack.
        # Assumes 1 or more shared items (characters) between rucksacks.
        shared = [i for i in set(line[0]) if i in line[1]]
        # Convert to ascii values.
        ascii = ([(ord(i), i) for i in shared])
        # lowercase item a-z is prioritised 1-26 (alphabetical ordered numbering!)
        [p.append(int(i[0] - 96)) if (i[0] >= 97 and i[0] <= 122)
        # uppercase item A-Z is prioritised 27-52 (alphabetical ordered numbering + 26!)
        else p.append(int(ord(i[1].lower()) - 70)) for i in ascii]

# What is the sum of the priorities of those item types?
print(sum(p))