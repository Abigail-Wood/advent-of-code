#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    # signal is characters received one at a time.
    signal = f.read()
    packets = [signal[i:i+14] for i in range(len(signal))]
    # detect start-of-packet marker in datastream: sequence of four characters that are all different
    unique_list = [len(set(packet)) == 14 for packet in packets]
    # identify first position where four most recently received characters were all different (report number from beginning to end)
    print(unique_list.index(True) + 14)
