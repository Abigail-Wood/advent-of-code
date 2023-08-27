#!/usr/bin/env python3

# identify first position where four most recently received characters were all different (report number from beginning to end)
def evaluate(list):
    for b in unique_list:
        if b == True:
            # adding 4 accounts for the offset from the start of the list.
            return unique_list.index(b) + 4

with open("input.txt", 'r') as f:
    # signal is characters received one at a time.
    signal = f.read()
    packets = [signal[i:i+4] for i in range(len(signal))]
    # detect start-of-packet marker in datastream: sequence of four characters that are all different
    unique_list = [True if len(set(packet)) == 4 else False for packet in packets]
    print(evaluate(unique_list))
