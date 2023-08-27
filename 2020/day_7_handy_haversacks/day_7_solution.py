#!/usr/bin/env python3

class Bag:
    def __init__(self, name, contained_by, contains):
        # tuple of adjective, colour
        self.name = name
        # list of tuples of adjective, colour
        self.contained_by = contained_by
        # list of tuples of adjective, colour, size
        self.contains = contains

def parse_input(file):
    bags = []
    bag_rules = [x.strip().split(" contain ") for x in list(f)]
    for c_b in bag_rules:
        container = c_b[0].split()
        contents = c_b[1].split(', ')
        parsed_contents = []
        for content in contents:
            if content != "no other bags.":
                size_adj_color_b = content.split(' ')
                parsed_contents.append(((size_adj_color_b[1], size_adj_color_b[2]), size_adj_color_b[0]))
        bags.append(Bag((container[0], container[1]), [], parsed_contents))
    return bags

# Here I have assumed all bag types have a rule, so they at least exist.
def populate_contains(bags):
    for bag in bags:
        for name, size in bag.contains:
            contained_bag = next((b for b in bags if b.name == name), None)
            contained_bag.contained_by.append(bag.name)

# Part One: How many bag colors can eventually contain at least one shiny gold bag?
def get_all_bags_that_can_contain(bag_name, bags):
    starting_bag = next((b for b in bags if b.name == bag_name), None)
    container_bags = set()

    def explore(bag_name):
        """
        Adds this bag to the container_bags, and explores anything that contains it.
        """
        bag = next((b for b in bags if bag_name == b.name), None)
        if bag.name != starting_bag.name:
            container_bags.add(bag.name)
        for b_name in bag.contained_by:
            explore(b_name)

    explore(bag_name)
    print(f"Part One Answer: {len(container_bags)}")

with open("/Users/awood/git_personal_repos/advent-of-code/2020/day_7_handy_haversacks/dummy_input.txt", 'r') as f:
    bags = parse_input(f)
    populate_contains(bags)
    get_all_bags_that_can_contain(("shiny", "gold"), bags)