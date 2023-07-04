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

## Day 3: Toboggan Trajectory

### Part One
You need to see which angles will take you near the fewest trees.
Trees in this area only grow on exact integer coordinates in a grid. 
You make a map of the open squares (.) and trees (#) you can see. 
The same pattern repeats to the right many times.
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
The toboggan can only follow a few specific slopes (rational numbers only).
An example is 'right 3, down 1' (this is a sequential move along the x and y axes respectively.)

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? 
Expectation for dummy input is 7.

### Part Two
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
