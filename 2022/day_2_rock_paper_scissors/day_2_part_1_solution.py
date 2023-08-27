#!/usr/bin/env python3

# Store straightforward shape scores matched to keys.
shape_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Can convert A,B,C into X,Y,Z
conversion_dict = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

# X is Rock, Y is Paper, Z is Scissors.
scoring_dict = {
    ("Z", "Y"): 0,
    ("Y", "X"): 0,
    ("X", "Z"): 0,
    ("Y", "Z"): 6,
    ("Z", "X"): 6,
    ("X", "Y"): 6
}

shape_total = 0
outcome_score = 0
with open ("input.txt", 'r') as f:
    lines = [(x.strip()).split(" ") for x in list(f)]
    for line in lines:
        shape_total += shape_dict[line[1]]
        # Draw is 3.
        if line[1] == conversion_dict[line[0]]:
            outcome_score += 3
        # Look up loss or win.
        else:
            outcome_score += scoring_dict[(conversion_dict[line[0]],line[1])]

# score_round = shape_values + outcome_score
print(shape_total + outcome_score)
