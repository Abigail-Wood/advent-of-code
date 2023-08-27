#!/usr/bin/env python3

# stacks of supply crates need to be rearranged
# crates can be moved between stacks
# end state: desired crates will be at the top of each stack

def parse_input(s):
    # input is: starting state of crates (resembles N ordered lists of characters)
    lb = s.index('')
    stacks = s[:lb]
    total_stacks = int(stacks[-1].split()[-1])
    stack_lists = [[] for i in range(total_stacks)]
    for stack in stacks[:-1]:
        stack_row = ([stack[i:i+3] for i in range(0, total_stacks * 4, 4)])
        count = 0
        for crate in stack_row:
            if crate != '   ':
                stack_lists[count].append(crate[1])
            count += 1
    # Extract values from list of rearrangement moves, to be executed sequentially.
    # Form is: [1, 2, 1], where order is number of crates, origin stack, destination stack.
    raw_moves = s[lb + 1:]
    moves_split = [move.split(' ')for move in raw_moves]
    # -1 converts stack indexing from 1-based to 0-based
    move_lists = [[int(move[1]), int(move[3]) - 1, int(move[5]) - 1] for move in moves_split]
    return stack_lists, move_lists

def move_crates(stack_lists, move):
    # Move form is: [1, 2, 1], where order is number of crates, origin stack, destination stack.
    number_of_crates = move[0]
    origin_stack = stack_lists[move[1]]
    destination_stack = stack_lists[move[2]]
    crates_to_move = origin_stack[len(origin_stack) - number_of_crates :]
    [destination_stack.append(crate) for crate in crates_to_move]
    del origin_stack[len(origin_stack) - number_of_crates:]
    return stack_lists

with open("input.txt", 'r') as f:
    stack_lists, moves = parse_input(f.read().splitlines())
    # Reverse stack list ordering to allow appending.
    [list.reverse() for list in stack_lists]
    # crates are moved one at a time.
    for move in moves:
        stack_lists = move_crates(stack_lists, move)
    # read out last item in each list
    print("".join([stack[len(stack) - 1] for stack in stack_lists]))
    # print top of each stack.
