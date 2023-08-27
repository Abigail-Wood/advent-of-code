#!/usr/bin/env python3

# Since input is a string, and we are building up gradually, keep it as a string
# and convert at the end, specifying base 2 system.
# gamma is most frequent bit, epsilon is least frequent bit.
gamma = ""
epsilon = ""

with open ("input.txt", 'r') as f:
        # Strip the file line; then turn each string into a list of characters.
        lines = [list(x.strip()) for x in list(f)]
        # gamma and epsilon will be of the same length as the number of digits in the first line.
        iterations = len(lines[0])
        for x in range(iterations):
            # Reset counts every time round the loop.
            off_value = 0
            on_value = 0
            for line in lines:
                # Take index[x] of each element of the list, count occurences of 1 and 0.
                if int(line[x]) == 1:
                    on_value += 1
                else:
                    off_value += 1
            # Assess counts after all lines evaluated. Note, this does not account for equal bit frequency.
            if on_value > off_value:
                gamma += ('1')
                epsilon += ('0')
            else:
                gamma += ('0')
                epsilon += ('1')

# Convert the binary numbers to decimal
# calculate the power consumption by multiplying the decimal gamma rate by the decimal epsilon rate.
print(int(gamma, 2) * int(epsilon, 2))
