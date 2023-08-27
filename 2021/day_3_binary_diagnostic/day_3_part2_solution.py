#!/usr/bin/env python3

# Since input is a string, and we are building up gradually, keep it as a string
# and convert at the end, specifying base 2 system.
# gamma is most frequent bit, epsilon is least frequent bit.
gamma = ""
epsilon = ""

with open ("dummy_input.txt", 'r') as f:
        # Strip the file line; then turn each string into a list of characters.
        lines = [list(x.strip()) for x in list(f)]
        # gamma and epsilon will be of the same length as the number of digits in the first line.
        for x in range(len(lines[0])):
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

        o2 = ""
        co2 = ""
        # LOOK AT FIRST INDEX OF EACH LIST ELEMENT.
        # THEN:
        #     KEEP only elements that meet a criteria at that index
        #     IF the list of elements reaches size 1, stop.
        #    SET the rating value equal to that element.
        for x in range(len(gamma)):
            print("eek, time to stop")
        # o2_generator_rating (10111 23):
        #    DETERMINE most common value (0 or 1) in current bit; keep only numbers with that bit in that position.
        #        IF 0 and 1 are equally common at the current bit, keep bits with 1 in that position.

        # co2_scrubber_rating (01010 10):
        #    DETERMINE least common value (0 or 1) in current bit; keep only numbers with that bit in that position.
        #        IF 0 and 1 are equally common at the current bit, keep bits with 0 in that position.

# Convert the binary numbers to decimal
# Multiple is 230.
print(int(o2, 2) * int(co2, 2))
