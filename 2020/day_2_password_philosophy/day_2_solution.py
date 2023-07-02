#!/usr/bin/env python3

def is_password_valid_sled(policy, password):
    occurrence, letter = policy.split(' ')
    valid_occurrences = set(range(int(occurrence.split('-')[0]), int(occurrence.split('-')[1]) + 1))
    return password.strip().count(letter) in valid_occurrences

def is_password_valid_toboggan(policy, password):
    region_bounds, letter = policy.split(' ')
    first, second = region_bounds.split('-')
    count = password[int(first) - 1].count(letter) + password[int(second) - 1].count(letter)
    return count == 1

with open('/Users/awood/git_personal_repos/advent-of-code/./2020/day_2_password_philosophy/input.txt', 'r') as f:
    validity_sled = []
    validity_toboggan = []
    for l in list(f):
        policy, password = (l.strip().split(':')) 
        password = password.strip()
        validity_sled.append(is_password_valid_sled(policy, password))
        validity_toboggan.append(is_password_valid_toboggan(policy, password))
    print(f"sled policy: {sum(1 for x in validity_sled if x)}")
    print(f"toboggan policy: {sum(1 for x in validity_toboggan if x)}")