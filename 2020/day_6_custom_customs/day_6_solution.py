#!/usr/bin/env python3

with open("/Users/awood/git_personal_repos/advent-of-code/2020/day_6_custom_customs/input.txt", 'r') as f:
    groups = f.read().split("\n\n")
    group_strings = [g.replace("\n", "") for g in groups]

    ## Part 1
    count = 0
    for group in group_strings:
        count += len(set(group))
    print(f"Part One answer: {count}")

    ## Part 2
    groups_split = [g.split("\n") for g in groups]
    groups_size = [len(g) for g in groups_split]

    # Relies on lists being ordered! And that no-one 'double answered' the same question.
    zipped = list(zip(group_strings, groups_size))
    
    new_count = 0
    for g,s in zipped:
        for c in set(g):
            if (g.count(c) == s):
                new_count += 1
    print(f"Part Two answer: {new_count}")




