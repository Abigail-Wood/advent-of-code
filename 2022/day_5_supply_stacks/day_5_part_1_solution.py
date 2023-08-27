#!/usr/bin/env python3

def parse_input(s):
    # Create desired data structure: N ordered lists of characters.
    lb = s.index('')
    stacks = s[:lb]
    # Get the total number of stacks, and make a corresponding empty list of lists to be populated.
    total_stacks = int(stacks[-1].split()[-1])
    stack_lists = [[] for i in range(total_stacks)]
    for stack in stacks[:-1]:
        # 4 is the number of characters used to describe a column.
        stack_row = [stack[i:i+3] for i in range(0, total_stacks * 4, 4)]
        count = 0
        for crate in stack_row:
            if crate != '   ':
                stack_lists[count].append(crate[1])
            count += 1
    # Reverse stack list ordering to allow appending.
    [list.reverse() for list in stack_lists]
    # Move desired data structure is lists e.g. [1, 2, 1], where order is number of crates, origin stack, destination stack.
    moves = [move.split(' ')for move in s[lb + 1:]]
    # Extract values from list of rearrangement moves, to be executed sequentially.
    # -1 converts stack indexing from 1-based to 0-based
    moves = [[int(move[1]), int(move[3]) - 1, int(move[5]) - 1] for move in moves]
    return stack_lists, moves

def move_crates(stack_lists, n, origin, destination):
    # Move form is: [1, 2, 1], where order is number of crates, origin stack, destination stack.
    crates_to_move = stack_lists[origin][len(stack_lists[origin]) - n :]
    # Reverse is to move crates to destination stack in right order (one at a time).
    crates_to_move.reverse()
    # Perform move and remove operations on stacks.
    [stack_lists[destination].append(crate) for crate in crates_to_move]
    del stack_lists[origin][len(stack_lists[origin]) - n:]
    return stack_lists

with open("input.txt", 'r') as f:
    stack_lists, moves = parse_input(f.read().splitlines())
    for move in moves:
        stack_lists = move_crates(stack_lists, move[0], move[1], move[2])
    # Print out last item in each list (shows top of stacks)
    print("".join([stack[len(stack) - 1] for stack in stack_lists]))
