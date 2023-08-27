#!/usr/bin/env python3

# Store straightforward shape scores matched to keys.
shape_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

# Can convert X,Y,Z into A,B,C
conversion_dict = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

# Convert player instructions to outcome scoring.
score_dict = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

# Convert player instructions to specific move choice.
# X means lose; Y means draw; Z means win; Rock is A, Paper is B, Scissors is C.
move_dict = {
    ("A", "Y"): "A",
    ("B", "Y"): "B",
    ("C", "Y"): "C",
    ("A", "X"): "C",
    ("B", "X"): "A",
    ("C", "X"): "B",
    ("A", "Z"): "B",
    ("B", "Z"): "C",
    ("C", "Z"): "A"
}

shape_total = 0
outcome_score = 0
with open ("input.txt", 'r') as f:
    lines = [(x.strip()).split(" ") for x in list(f)]
    for line in lines:
        shape_total += shape_dict[move_dict[(line[0],line[1])]]
        outcome_score += score_dict[(line[1])]

# score_round = shape_values + outcome_score
print(shape_total + outcome_score)
