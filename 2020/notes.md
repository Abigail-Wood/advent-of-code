# AoC Notes

## Day 1: Report Repair

### Part One
Find two values in a list of integers that sum to a specified integer value, and multiply those two integers together.

### Part Two
Find three values in a list of integers that sum to a specified integer value, and multiple those three integers together.

## Day 2: Password Philosophy

### Part One
Data structure of input:
- Prior to :, password policy communicates the lowest and highest number of times a given letter must appear for a password to be valid.
- After : is the letter to which the policy of 'number of occurrences' applies.
How many passwords are valid according to their policies?

### Part Two
Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, and so on. (No "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

How many passwords are valid according to the new interpretation of the policies?
